import os
from datetime import datetime, timezone

from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import or_
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Attachment, CatalogItem, Comment, Motd, Ticket, TicketEvent, User
from schemas import (
    AttachmentCreate,
    CatalogIn,
    CommentCreate,
    IncidentCreate,
    MotdIn,
    RequestCreate,
    TicketUpdate,
    UserIn,
)
from seed import new_sys_id, next_number, seed

STATUS_MAP = {
    1: "New",
    2: "In Progress",
    3: "Pending",
    6: "Resolved",
    7: "Closed",
    8: "Cancelled",
    9: "Assigned",
}

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MeridianDesk ITSM Microservice",
    version="1.0.0",
    description="Custom ITSM API for the Meridian AEX agent (replaces ServiceNow).",
    openapi_tags=[
        {"name": "Health", "description": "Service health checks."},
        {"name": "Users", "description": "Employee and user profile lookup."},
        {"name": "Announcements", "description": "Current message of the day."},
        {"name": "Catalog", "description": "Available service catalog items and search."},
        {"name": "Incidents", "description": "Create incidents for employee issues."},
        {"name": "Tickets", "description": "Employee ticket lifecycle and collaboration."},
        {"name": "Admin", "description": "Internal ticket fulfilment and audit operations."},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    if os.getenv("SEED_ON_START", "true").lower() == "true":
        db = next(get_db())
        try:
            seed(db)
        finally:
            db.close()


def now():
    return datetime.now(timezone.utc)


def require_user(db: Session, user_id: str) -> User:
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def require_ticket(db: Session, number: str) -> Ticket:
    ticket = db.get(Ticket, number)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


def enforce_owner(ticket: Ticket, user_id: str) -> None:
    if ticket.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorised for this ticket")


def comment_blob(ticket: Ticket) -> str:
    lines = []
    for c in sorted(ticket.comments, key=lambda x: x.created_at):
        kind = "system" if c.is_system else "user"
        lines.append(f"[{c.created_at.isoformat()}] ({kind}) {c.author}: {c.text}")
    return "\n".join(lines)


def ticket_dict(ticket: Ticket, technical: bool = True) -> dict:
    payload = {
        "number": ticket.number,
        "ticket_type": ticket.ticket_type,
        "state": ticket.state,
        "status": STATUS_MAP.get(ticket.state, str(ticket.state)),
        "priority": ticket.priority,
        "urgency": ticket.urgency,
        "short_description": ticket.short_description,
        "description": ticket.description,
        "assigned_to": ticket.assigned_to,
        "opened_at": ticket.opened_at,
        "sys_updated_on": ticket.sys_updated_on,
        "comments_and_work_notes": comment_blob(ticket),
        "catalog_item_id": ticket.catalog_item_id,
        "category": ticket.category,
        "subcategory": ticket.subcategory,
        "user_id": ticket.user_id,
    }
    if technical:
        payload["sys_id"] = ticket.sys_id
        payload["assignment_group"] = ticket.assignment_group
    return payload


def record_event(db: Session, number: str, event_type: str, summary: str) -> None:
    db.add(TicketEvent(ticket_number=number, event_type=event_type, summary=summary))


def open_duplicate(db: Session, user_id: str, short_description: str):
    active_states = [1, 2, 3, 9]
    return (
        db.query(Ticket)
        .filter(
            Ticket.user_id == user_id,
            Ticket.short_description == short_description,
            Ticket.state.in_(active_states),
        )
        .order_by(Ticket.sys_updated_on.desc())
        .first()
    )


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}


# --- Users ---
@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: str, db: Session = Depends(get_db)):
    return require_user(db, user_id)


@app.get("/users", tags=["Users"])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.user_id).all()


# --- MOTD ---
@app.get("/motd", tags=["Announcements"])
def get_motd(db: Session = Depends(get_db)):
    rows = (
        db.query(Motd)
        .filter(Motd.active.is_(True))
        .order_by(Motd.created_at.desc())
        .limit(2)
        .all()
    )
    return [{"id": r.id, "message": r.message} for r in rows]


# --- Catalogue ---
@app.get("/catalog/search", tags=["Catalog"])
def catalog_search(q: str = "", db: Session = Depends(get_db)):
    query = db.query(CatalogItem).filter(CatalogItem.active.is_(True))
    if q.strip():
        like = f"%{q.strip()}%"
        query = query.filter(
            or_(
                CatalogItem.name.ilike(like),
                CatalogItem.description.ilike(like),
                CatalogItem.category.ilike(like),
                CatalogItem.id.ilike(like),
            )
        )
    items = query.order_by(CatalogItem.name).all()
    return [
        {
            "id": i.id,
            "name": i.name,
            "link": i.link,
            "description": i.description,
            "category": i.category,
        }
        for i in items
    ]


@app.get("/catalog", tags=["Catalog"])
def list_catalog(db: Session = Depends(get_db)):
    return db.query(CatalogItem).order_by(CatalogItem.name).all()


# --- Incidents / Requests ---
@app.post("/incidents", status_code=201, tags=["Incidents"])
def create_incident(body: IncidentCreate, db: Session = Depends(get_db)):
    user = require_user(db, body.on_behalf_of)
    dup = open_duplicate(db, user.user_id, body.short_description)
    if dup:
        return {
            "duplicate": True,
            "message": "An open ticket already exists for this issue.",
            "ticket": ticket_dict(dup),
        }

    number = next_number(db, "incident")
    ticket = Ticket(
        number=number,
        ticket_type="incident",
        user_id=user.user_id,
        short_description=body.short_description,
        description=body.description,
        state=1,
        priority=body.priority or "3",
        urgency=body.urgency,
        category=body.category,
        subcategory=body.subcategory,
        assignment_group=body.assignment_group,
        sys_id=new_sys_id(),
    )
    db.add(ticket)
    if body.business_phone_number and not user.phone:
        user.phone = body.business_phone_number
    record_event(db, number, "created", f"Incident {number} created")
    db.commit()
    db.refresh(ticket)
    return {"duplicate": False, "ticket": ticket_dict(ticket)}


@app.post("/requests", status_code=201, tags=["Catalog"])
def create_request(body: RequestCreate, db: Session = Depends(get_db)):
    user = require_user(db, body.on_behalf_of)
    item = db.get(CatalogItem, body.catalog_item_id)
    if item is None or not item.active:
        raise HTTPException(status_code=404, detail="Catalogue item not found")

    short = body.short_description or item.name
    dup = open_duplicate(db, user.user_id, short)
    if dup:
        return {
            "duplicate": True,
            "message": "An open request already exists for this item.",
            "ticket": ticket_dict(dup),
        }

    number = next_number(db, "ritm")
    ticket = Ticket(
        number=number,
        ticket_type="ritm",
        user_id=user.user_id,
        short_description=short,
        description=body.description,
        state=1,
        priority=body.priority or "3",
        urgency=body.urgency,
        category="Service Request",
        subcategory=item.category,
        catalog_item_id=item.id,
        sys_id=new_sys_id(),
    )
    db.add(ticket)
    if body.business_phone_number and not user.phone:
        user.phone = body.business_phone_number
    record_event(db, number, "created", f"Request {number} created")
    db.commit()
    db.refresh(ticket)
    return {"duplicate": False, "ticket": ticket_dict(ticket)}


@app.get("/tickets", tags=["Tickets"])
def list_tickets(user_id: str, db: Session = Depends(get_db)):
    require_user(db, user_id)
    rows = (
        db.query(Ticket)
        .filter(Ticket.user_id == user_id)
        .order_by(Ticket.sys_updated_on.desc())
        .limit(10)
        .all()
    )
    return [ticket_dict(t) for t in rows]


@app.get("/tickets/{number}", tags=["Tickets"])
def get_ticket(number: str, user_id: str, db: Session = Depends(get_db)):
    require_user(db, user_id)
    ticket = require_ticket(db, number)
    enforce_owner(ticket, user_id)
    return ticket_dict(ticket)


@app.post("/tickets/{number}/comments", status_code=201, tags=["Tickets"])
def add_comment(
    number: str,
    body: CommentCreate,
    user_id: Optional[str] = Query(default=None),
    db: Session = Depends(get_db),
):
    ticket = require_ticket(db, number)
    if user_id:
        enforce_owner(ticket, user_id)
    comment = Comment(
        ticket_number=number,
        author=body.author or (user_id or "aex-agent"),
        text=body.text,
        is_system=body.is_system,
    )
    ticket.sys_updated_on = now()
    db.add(comment)
    record_event(db, number, "comment", body.text)
    db.commit()
    db.refresh(comment)
    return {
        "id": comment.id,
        "ticket_number": number,
        "author": comment.author,
        "text": comment.text,
        "is_system": comment.is_system,
        "created_at": comment.created_at,
        "ticket": ticket_dict(ticket),
    }


@app.post("/tickets/{number}/attachments", status_code=201, tags=["Tickets"])
def add_attachment(
    number: str,
    body: AttachmentCreate,
    user_id: Optional[str] = Query(default=None),
    db: Session = Depends(get_db),
):
    ticket = require_ticket(db, number)
    if user_id:
        enforce_owner(ticket, user_id)
    att = Attachment(
        ticket_number=number,
        filename=body.filename,
        content_base64=body.content_base64,
    )
    ticket.sys_updated_on = now()
    db.add(att)
    record_event(db, number, "attachment", f"Attachment added: {body.filename}")
    db.commit()
    db.refresh(att)
    return {
        "id": att.id,
        "ticket_number": number,
        "filename": att.filename,
        "created_at": att.created_at,
    }


@app.get("/tickets/{number}/attachments", tags=["Tickets"])
def list_attachments(
    number: str, user_id: str, db: Session = Depends(get_db)
):
    ticket = require_ticket(db, number)
    enforce_owner(ticket, user_id)
    return [
        {"id": a.id, "filename": a.filename, "created_at": a.created_at}
        for a in ticket.attachments
    ]


# --- Admin / fulfilment simulation (not for the chat agent) ---
@app.patch("/admin/tickets/{number}", tags=["Admin"])
def admin_patch(number: str, body: TicketUpdate, db: Session = Depends(get_db)):
    ticket = require_ticket(db, number)
    changes = []
    data = body.model_dump(exclude_unset=True)
    for key, value in data.items():
        old = getattr(ticket, key)
        if old != value:
            changes.append(f"{key}: {old} -> {value}")
            setattr(ticket, key, value)
    ticket.sys_updated_on = now()
    summary = "; ".join(changes) if changes else "No field changes"
    record_event(db, number, "updated", summary)
    db.commit()
    db.refresh(ticket)
    return {"ticket": ticket_dict(ticket), "what_changed": summary, "changes": changes}


@app.get("/admin/tickets", tags=["Admin"])
def admin_list_all(
    skip: int = 0, limit: int = 50, db: Session = Depends(get_db)
):
    rows = (
        db.query(Ticket)
        .order_by(Ticket.sys_updated_on.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return [ticket_dict(t) for t in rows]


@app.get("/admin/events", tags=["Admin"])
def admin_events(ticket_number: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(TicketEvent)
    if ticket_number:
        q = q.filter(TicketEvent.ticket_number == ticket_number)
    return q.order_by(TicketEvent.created_at.desc()).limit(100).all()


