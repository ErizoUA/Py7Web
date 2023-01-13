from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, func
from sqlalchemy.sql.sqltypes import DateTime

from db.connect import Base


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(250))
    done = Column(Boolean, default=False)
    created_at = Column('crated_at', DateTime, default=func.now())
