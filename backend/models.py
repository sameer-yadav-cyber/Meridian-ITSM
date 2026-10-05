from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from database import Base


def utcnow():
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    role = Column(String, nullable=False, default="employee")
    created_at = Column(DateTime(timezone=True), default=utcnow)

    tickets = relationship("Ticket", back_populates="requester")


class CatalogItem(Base):
    __tablename__ = "catalog_items"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    link = Column(String, nullable=False)
    category = Column(String, nullable=False)
    active = Column(Boolean, default=True)


class Ticket(Base):
    __tablename__ = "tickets"

    number = Column(String, primary_key=True)
    ticket_type = Column(String, nullable=False)  # incident | ritm
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    short_description = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    state = Column(Integer, nullable=False, default=1)
    priority = Column(String, nullable=True)
    urgency = Column(String, nullable=True)
    category = Column(String, nullable=True)
    subcategory = Column(String, nullable=True)
    assigned_to = Column(String, nullable=True)
    assignment_group = Column(String, nullable=True)
    catalog_item_id = Column(String, ForeignKey("catalog_items.id"), nullable=True)
    sys_id = Column(String, nullable=False)
    opened_at = Column(DateTime(timezone=True), default=utcnow)
    sys_updated_on = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow)

    requester = relationship("User", back_populates="tickets")
    comments = relationship("Comment", back_populates="ticket", cascade="all, delete-orphan")
    attachments = relationship(
        "Attachment", back_populates="ticket", cascade="all, delete-orphan"
    )


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_number = Column(String, ForeignKey("tickets.number"), nullable=False)
    author = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    is_system = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=utcnow)

    ticket = relationship("Ticket", back_populates="comments")


class Attachment(Base):
    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_number = Column(String, ForeignKey("tickets.number"), nullable=False)
    filename = Column(String, nullable=False)
    content_base64 = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utcnow)

    ticket = relationship("Ticket", back_populates="attachments")


class Motd(Base):
    __tablename__ = "motd"

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(Text, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=utcnow)


class Sequence(Base):
    __tablename__ = "sequences"
    __table_args__ = (UniqueConstraint("name", name="uq_sequence_name"),)

    name = Column(String, primary_key=True)
    value = Column(Integer, nullable=False, default=0)


class TicketEvent(Base):
    __tablename__ = "ticket_events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_number = Column(String, nullable=False)
    event_type = Column(String, nullable=False)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utcnow)
