from datetime import datetime

from pydantic import Base
from sqlalchemy import Column, DateTime, func


class CommonFields(Base):
    """공통 필드 클래스"""

    __abstract__ = True

    created_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    updated_at = Column(
        DateTime,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )

    class Config:
        orm_mode = True
