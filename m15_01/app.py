from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db.connect import get_db
from src.routers import notes, auth, users

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/api/healthchecker")
async def healthchecker(db: Session = Depends(get_db)):
    try:
        r = db.execute("SELECT 1").fetchone()
        if r is None:
            raise HTTPException(
                status_code=500, detail="Database is not configured correctly"
            )
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connection to database")


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(notes.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Notes APP v1.0"}
