from sqlalchemy import Column, Integer, Text, ForeignKey
from app.core.database import Base


class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)

    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)

    report = Column(Text, nullable=False)