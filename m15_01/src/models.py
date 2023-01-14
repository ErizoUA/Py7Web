from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, func
from sqlalchemy.sql.sqltypes import DateTime

from db.connect import Base
from src.constants import USERNAME_LENGTH


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String(USERNAME_LENGTH))
    description = Column(String(250))
    done = Column(Boolean, default=False)
    created_at = Column('crated_at', DateTime, default=func.now())
    user = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), default=None)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column('crated_at', DateTime, default=func.now())
    avatar = Column(String(255), nullable=False)
