from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session

from db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def default():
    return RedirectResponse(url="/docs")    