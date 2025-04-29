from fastapi import FastAPI
from app.core.config import settings
from app.modules.jobs.router import router as jobs_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(jobs_router)
