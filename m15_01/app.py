from typing import Optional

from fastapi import FastAPI, Query, Path, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from db.connect import get_db
from src.routers import notes

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


app.include_router(notes.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Notes APP"}
