import uuid

from sqlalchemy import Column, String

from .database import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)
    nickname = Column(String(120), nullable=True)
    family = Column(String(120), nullable=False)
    rank = Column(String(80), nullable=False)
    status = Column(String(40), nullable=False, default="active")
