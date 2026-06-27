from celery import Celery

from app.core.config import REDIS_URL

celery = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)