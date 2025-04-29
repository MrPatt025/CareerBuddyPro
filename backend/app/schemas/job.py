from datetime import datetime
from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
    company: str
    date_applied: datetime
    status: str
    applied_via: str | None = None
    url: str | None = None

class JobCreate(JobBase):
    pass

class JobRead(JobBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


        orm_mode = True 
