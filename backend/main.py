from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel

from db import SessionLocal, engine, Base
import models
from schemas import *

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Default"])
def default():
    return RedirectResponse(url="/docs")    

@app.delete("/user/", tags=["User"])
def delete_users(db: Session = Depends(get_db)):
    db.query(models.Users).delete()
    db.commit()

@app.post("/user/", tags=["User"])
def create_user(user: UsersCreate, db: Session = Depends(get_db)):
    new_user = models.Users(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "✅ Usuario creado con éxito", "task": new_user}

@app.get("/user/", tags=["User"])
def show_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all() 

@app.get("/user/{id}", tags=["User"])
def show_user(id:int,db: Session = Depends(get_db)):
    return db.query(models.Users).filter_by(id=id).first()

@app.delete("/user/{id}", tags=["User"])
def delete_user(id:int, db:Session=Depends(get_db)):
    db.query(models.Users).filter_by(id=id).delete()
    db.commit()

@app.put("/user/{id}", tags=["User"])
def update_user(id:int, user: UserResponse,db:Session=Depends(get_db)):
    person=db.query(models.Users).filter_by(id=id).first()
    if not person:
        return{"message": "User does not exist."}
    
    update_user=user.model_dump(exclude_unset=True)

    if "id" in update_user:
        update_user.pop("id")   

    for key, value in update_user():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)





@app.post("/task/", tags=["Task"])
def create_task(task: TaskBase, db: Session = Depends(get_db)):
    new_task = models.Tasks(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "✅ Tarea creada con éxito", "task": new_task}


@app.get("/task/", tags=["Task"])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Tasks).all()

@app.delete("/task/", tags=["Task"])
def delete_tasks(db:Session = Depends(get_db)):
    db.query(models.Tasks).delete()
    db.commit()

@app.get("/task/{id}", tags=["Task"])
def get_task(id:int, db: Session = Depends(get_db)):
    return db.query(models.Tasks).filter_by(id=id).first()    

@app.delete("/task/{id}", tags=["Task"])
def delete_task(id:int, db:Session = Depends(get_db)):
    db.query(models.Tasks).filter_by(id=id).delete()
    db.commit()

@app.get("/task-user/{user_id}", tags=["Task"])
def get_user_tasks(user_id:int, db:Session = Depends(get_db)):
    return db.query(models.Tasks).filter(models.Tasks.UserId==user_id).all()   

@app.delete("/task-user/{user_id}", tags=["Task"])
def remove_all_tasks_from_user(user_id:int, db:Session = Depends(get_db)):
    db.query(models.Tasks).filter(models.Tasks.UserId==user_id).delete()
    db.commit()

@app.put("/task/{id}", tags=["Task"])
def update_task(id:int, db:Session = Depends(get_db)):
    pass