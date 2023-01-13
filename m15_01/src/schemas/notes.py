from datetime import datetime

from pydantic import BaseModel, Field


class NoteBase(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=150, description='description of note')
    done: bool = Field(default=False)


class NoteUpdate(NoteBase):
    done: bool


class NoteStatus(BaseModel):
    done: bool


class NoteResponse(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
