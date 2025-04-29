from sqlmodel import SQLModel, Field
from datetime import datetime

class Job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    company: str
    date_applied: datetime
    status: str
    applied_via: str | None = None
    url: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
