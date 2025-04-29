from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db import get_session
from app.models import Job
from app.schemas.job import JobCreate, JobRead

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

@router.put("/{job_id}", response_model=JobRead)
def update_job(job_id: int, job: JobCreate, session: Session = Depends(get_session)) -> JobRead:
    db_job = session.get(Job, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    for key, value in job.dict().items():
        setattr(db_job, key, value)
    session.add(db_job)
    session.commit()
    session.refresh(db_job)
    return db_job

@router.delete("/{job_id}")
def delete_job(job_id: int, session: Session = Depends(get_session)):
    db_job = session.get(Job, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    session.delete(db_job)
    session.commit()
    return {"ok": True}
