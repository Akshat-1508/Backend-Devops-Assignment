import os

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.config import UPLOAD_FOLDER

from app.models.job import Job
from app.models.summary import Summary

from app.utils.helper import save_uploaded_file
from app.workers.tasks import process_csv
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post("/upload")
def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.filename.endswith(".csv"):
        return {"error": "Only CSV files are allowed"}

    filename, filepath = save_uploaded_file(
        file,
        UPLOAD_FOLDER
    )

    job = Job(
        filename=filename,
        status="PENDING"
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    process_csv.delay(
        job.id,
        filepath
    )

    return {
        "job_id": job.id,
        "status": job.status
    }


@router.get("/")
def get_jobs(
    db: Session = Depends(get_db)
):

    return db.query(Job).all()


@router.get("/{job_id}/status")
def job_status(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = db.query(Job).filter(Job.id == job_id).first()

    return job


@router.get("/{job_id}/results")
def get_results(
    job_id: int,
    db: Session = Depends(get_db)
):

    report = (
        db.query(Summary)
        .filter(Summary.job_id == job_id)
        .first()
    )

    if report is None:
        return {
            "message": "No report found for this job."
        }

    return report

@router.get("/{job_id}/download")
def download_report(job_id: int):

    report_path = f"reports/report_{job_id}.txt"

    if not os.path.exists(report_path):
        return {
            "message": "Report not found."
        }

    return FileResponse(
        report_path,
        media_type="text/plain",
        filename=f"report_{job_id}.txt"
    )