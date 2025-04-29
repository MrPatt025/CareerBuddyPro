from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db import get_session
from app.models import Job

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("/", response_model=list[Job])
def read_jobs(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)) -> list[Job]:
    jobs = session.exec(Job.select().offset(skip).limit(limit)).all()

