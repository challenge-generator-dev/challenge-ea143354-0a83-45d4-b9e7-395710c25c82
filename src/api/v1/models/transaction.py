from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from src.api.v1.config.database import Base


class TransactionStatus(PyEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    idempotency_key = Column(String, unique=True, nullable=True)

    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, status={self.status})>"


# Modelo User para relación (ya existe en otro lote, solo referencia)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    transactions = relationship("Transaction", back_populates="user")