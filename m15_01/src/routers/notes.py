from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.connect import get_db
from src.libs.oath2 import get_current_user
from src.models import User
from src.schemas.notes import NoteBase, NoteUpdate, NoteStatus, NoteResponse
from src.repository import notes as repository_notes

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", response_model=List[NoteResponse])
async def get_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    notes = await repository_notes.get_all_notes(skip, limit, current_user, db)
    return notes


@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = await repository_notes.get_note(note_id, current_user, db)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return note


@router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
async def create_note(note: NoteBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = await repository_notes.create_note(note, current_user, db)
    return note


@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    note = await repository_notes.update_note(note_id, note, current_user, db)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return note


@router.patch("/{note_id}", response_model=NoteResponse)
async def update_status_note(note_id: int, note: NoteStatus, db: Session = Depends(get_db),
                             current_user: User = Depends(get_current_user)):
    note = await repository_notes.update_status_note(note_id, note, current_user, db)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = await repository_notes.get_note(note_id, current_user, db)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return note
