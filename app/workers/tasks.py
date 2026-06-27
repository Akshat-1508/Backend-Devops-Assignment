from app.core.celery_app import celery
from app.core.database import SessionLocal
from app.utils.logger import logger
from app.models.job import Job
from app.models.transaction import Transaction
from app.models.summary import Summary

from app.services.pipeline import process_pipeline


@celery.task
def process_csv(job_id, file_path):

    logger.info(f"Processing Job {job_id}")
    db = SessionLocal()

    try:

        job = db.query(Job).filter(Job.id == job_id).first()

        job.status = "PROCESSING"

        db.commit()

        df, ai_summary = process_pipeline(file_path)

        for _, row in df.iterrows():

            transaction = Transaction(
                transaction_id=str(row["transaction_id"]),
                merchant=row["merchant"],
                amount=float(row["amount"]),
                currency=row["currency"],
                category=row["category"],
                status=row["status"],
                anomaly=row["anomaly"]
            )

            db.add(transaction)

        report = Summary(
            job_id=job.id,
            report=ai_summary
        )

        report = (
            db.query(Summary)
            .filter(Summary.job_id == job_id)
            .first()
        )

        db.add(report)

        with open(f"reports/report_{job.id}.txt", "w", encoding="utf-8") as file:
            file.write(ai_summary)
            
        job.status = "COMPLETED"

        db.commit()

    except Exception as e:

        print(f"Processing Error: {e}")

        if job:
            job.status = "FAILED"
            db.commit()

    finally:

        db.close()