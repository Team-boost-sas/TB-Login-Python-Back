from src.config.databases import Base
from sqlalchemy import Column, Integer, String, Float


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    password = Column(String)
    phone = Column(String)
    secret = Column(String)
    updated_at = Column(String)
    created_at = Column(String)
    status = Column(String)
    status_email = Column(String)
    status_phone = Column(String)