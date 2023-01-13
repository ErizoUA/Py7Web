from typing import Optional

from fastapi import FastAPI, Query, Path, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from db import get_db

app = FastAPI()


@app.get("/api/healthchecker")
async def healthchecker(db: Session = Depends(get_db)):
    try:
        r = db.execute('SELECT 1').fetchone()
        if r is None:
            raise HTTPException(status_code=500, detail='Database is not configured correctly')
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='Error connection to database')


@app.get("/notes")
async def read_notes(skip: int = 0, limit: int = Query(default=10, ge=10, le=100), q: Optional[str] = None):
    return {"message": f"Read all notes skip: {skip} limit: {limit}"}


@app.get("/notes/{note_id}")
async def read_note(note_id: int = Path(description='The ID note', gt=0, le=10)):
    return {"note": note_id}


class Note(BaseModel):
    name: str
    description: str
    done: Optional[bool] = Field(default=False)


@app.post("/notes")
async def create_note(note: Note):
    return {"name": note.name, "description": note.description, "status": note.done}


