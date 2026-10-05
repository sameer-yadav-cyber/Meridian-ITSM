from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserIn(BaseModel):
    user_id: str
    name: str
    email: str
    phone: Optional[str] = None
    role: str = "employee"


class UserOut(UserIn):
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CatalogIn(BaseModel):
    id: str
    name: str
    description: str
    link: str
    category: str
    active: bool = True


class CatalogOut(CatalogIn):
    class Config:
        from_attributes = True


class IncidentCreate(BaseModel):
    on_behalf_of: str
    short_description: str
    description: str
    business_phone_number: Optional[str] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
    urgency: Optional[str] = None
    priority: Optional[str] = None
    assignment_group: Optional[str] = None


class RequestCreate(BaseModel):
    on_behalf_of: str
    catalog_item_id: str
    short_description: Optional[str] = None
    description: str
    business_phone_number: Optional[str] = None
    urgency: Optional[str] = None
    priority: Optional[str] = None


class CommentCreate(BaseModel):
    text: str
    author: Optional[str] = "aex-agent"
    is_system: bool = False


class AttachmentCreate(BaseModel):
    filename: str
    content_base64: str


class TicketUpdate(BaseModel):
    state: Optional[int] = None
    assigned_to: Optional[str] = None
    priority: Optional[str] = None
    urgency: Optional[str] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None


class MotdIn(BaseModel):
    message: str
    active: bool = True


class TicketPublic(BaseModel):
    number: str
    ticket_type: str
    state: int
    status: str
    priority: Optional[str] = None
    urgency: Optional[str] = None
    short_description: str
    description: str
    assigned_to: Optional[str] = None
    opened_at: datetime
    sys_updated_on: datetime
    comments_and_work_notes: str = ""
    catalog_item_id: Optional[str] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None


class TicketTechnical(TicketPublic):
    sys_id: str
    user_id: str
    assignment_group: Optional[str] = None
