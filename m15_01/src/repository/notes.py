from sqlalchemy.orm import Session

from src.models import Note
from src.schemas.notes import NoteBase, NoteUpdate, NoteStatus, NoteResponse


async def get_all_notes(skip, limit, db: Session):
    notes = db.query(Note).offset(skip).limit(limit).all()
    return notes


async def get_note(note_id: int, db:Session):
    note = db.query(Note).filter(Note.id == note_id).first()
    return note


async def create_note(body: NoteBase, db: Session) -> NoteResponse:
    new_note = Note(title=body.title, description=body.description, done=body.done)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    print(new_note)
    return new_note


async def update_note(note_id: int, body: NoteUpdate, db: Session):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        note.title = body.title
        note.description = body.description
        note.done = body.done
        db.commit()
    return note


async def update_status_note(note_id: int, body: NoteStatus, db: Session):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        note.done = body.done
        db.commit()
    return note


async def delete_note(note_id: int, db: Session):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
    return note
