from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db import get_session
from app.models import Job
from app.schemas.job import JobCreate, JobRead  # เพิ่มการนำเข้า

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("/", response_model=list[Job])
def read_jobs(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)) -> list[Job]:
    return session.exec(Job.select().offset(skip).limit(limit)).all()

@router.post("/", response_model=JobRead)
def create_job(job: JobCreate, session: Session = Depends(get_session)) -> JobRead:
    db_job = Job.from_orm(job)
    session.add(db_job)
    session.commit()
    session.refresh(db_job)
    return db_job
