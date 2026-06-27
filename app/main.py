from fastapi import FastAPI

from app.api.jobs import router as job_router

from app.core.database import Base
from app.core.database import engine

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Backend DevOps Assignment",
    version="1.0.0"
)

app.include_router(job_router)


@app.get("/")
def home():
    return {
        "message": "Backend DevOps Assignment API is Running"
    }