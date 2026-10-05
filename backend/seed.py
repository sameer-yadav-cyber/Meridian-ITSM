import uuid

from sqlalchemy.orm import Session

from models import CatalogItem, Motd, Sequence, User

USERS = [
    {
        "user_id": "1001",
        "name": "Jordan Smith",
        "email": "jordan.smith@meridian.example",
        "phone": "+1-555-0101",
        "role": "employee",
    },
    {
        "user_id": "1002",
        "name": "Asha Patel",
        "email": "asha.patel@meridian.example",
        "phone": "+1-555-0102",
        "role": "employee",
    },
    {
        "user_id": "1003",
        "name": "Mei Chen",
        "email": "mei.chen@meridian.example",
        "phone": "+1-555-0103",
        "role": "contractor",
    },
    {
        "user_id": "1004",
        "name": "Rafael Garcia",
        "email": "rafael.garcia@meridian.example",
        "phone": "+1-555-0104",
        "role": "it_agent",
    },
    {
        "user_id": "1005",
        "name": "Nora Williams",
        "email": "nora.williams@meridian.example",
        "phone": "+1-555-0105",
        "role": "manager",
    },
    {
        "user_id": "1006",
        "name": "David Kim",
        "email": "david.kim@meridian.example",
        "phone": "+1-555-0106",
        "role": "employee",
    },
]

CATALOG = [
    {
        "id": "cat-software-install",
        "name": "Request software installation",
        "description": "Install an approved application from the Meridian software catalogue.",
        "link": "https://meridiandesk.internal/catalog/software-install",
        "category": "Software",
    },
    {
        "id": "cat-vpn-access",
        "name": "Request VPN access",
        "description": "Grant remote VPN entitlement for the corporate network.",
        "link": "https://meridiandesk.internal/catalog/vpn-access",
        "category": "Access",
    },
    {
        "id": "cat-new-laptop",
        "name": "Request new laptop",
        "description": "Order a standard Meridian laptop for a new or replacement device.",
        "link": "https://meridiandesk.internal/catalog/new-laptop",
        "category": "Hardware",
    },
    {
        "id": "cat-shared-mailbox",
        "name": "Request shared mailbox",
        "description": "Create or grant access to a shared mailbox.",
        "link": "https://meridiandesk.internal/catalog/shared-mailbox",
        "category": "Messaging",
    },
    {
        "id": "cat-peripherals",
        "name": "Request IT peripheral",
        "description": "Order a standard monitor, headset, keyboard, mouse, or webcam.",
        "link": "https://meridiandesk.internal/catalog/peripherals",
        "category": "Hardware",
    },
    {
        "id": "cat-licence",
        "name": "Request software licence",
        "description": "Assign a Microsoft 365 or other approved software licence.",
        "link": "https://meridiandesk.internal/catalog/licence",
        "category": "Licence",
    },
    {
        "id": "cat-data-access",
        "name": "Request file or SharePoint access",
        "description": "Request read or edit access to a file share or SharePoint site.",
        "link": "https://meridiandesk.internal/catalog/data-access",
        "category": "Data",
    },
    {
        "id": "cat-mfa-reset",
        "name": "Request MFA reset",
        "description": "Identity-verified reset of authenticator enrolment. Human fulfilment required.",
        "link": "https://meridiandesk.internal/catalog/mfa-reset",
        "category": "Identity",
    },
    {
        "id": "cat-privileged-access",
        "name": "Request privileged access",
        "description": "Request time-bound local admin or privileged role. Requires approval.",
        "link": "https://meridiandesk.internal/catalog/privileged-access",
        "category": "Access",
    },
    {
        "id": "cat-joiner-bundle",
        "name": "New joiner IT bundle",
        "description": "Standard joiner access: mailbox, M365, VPN entitlement, and laptop request.",
        "link": "https://meridiandesk.internal/catalog/joiner-bundle",
        "category": "Joiner",
    },
    {
        "id": "cat-charger",
        "name": "Request replacement charger",
        "description": "Order a replacement power adapter for a Meridian-issued laptop.",
        "link": "https://meridiandesk.internal/catalog/charger",
        "category": "Hardware",
    },
]

MOTD = [
    "Scheduled Wi-Fi maintenance in HQ Building A, Saturday 18:00–20:00 local time.",
    "Company Portal now lists the updated VPN client. Please install before next week.",
]


def seed(db: Session) -> None:
    if db.query(User).count() == 0:
        for row in USERS:
            db.add(User(**row))

    if db.query(CatalogItem).count() == 0:
        for row in CATALOG:
            db.add(CatalogItem(**row))

    if db.query(Motd).count() == 0:
        for message in MOTD:
            db.add(Motd(message=message, active=True))

    if db.get(Sequence, "incident") is None:
        db.add(Sequence(name="incident", value=1000))
    if db.get(Sequence, "ritm") is None:
        db.add(Sequence(name="ritm", value=1000))

    db.commit()


def next_number(db: Session, kind: str) -> str:
    seq = db.get(Sequence, kind)
    if seq is None:
        seq = Sequence(name=kind, value=1000)
        db.add(seq)
        db.flush()
    seq.value += 1
    prefix = "INC" if kind == "incident" else "RITM"
    return f"{prefix}{seq.value:07d}"


def new_sys_id() -> str:
    return str(uuid.uuid4())
