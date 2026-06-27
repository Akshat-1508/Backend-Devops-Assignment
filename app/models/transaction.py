from sqlalchemy import Column, Integer, Float, String
from app.core.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(String, unique=True, nullable=False)

    merchant = Column(String)

    amount = Column(Float)

    currency = Column(String)

    category = Column(String)

    status = Column(String)

    anomaly = Column(String, default="No")