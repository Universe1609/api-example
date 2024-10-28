from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

app = FastAPI()

# Crear la base de datos
models.Base.metadata.create_all(bind=database.engine)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = database.get_db()):
    return crud.create_user(db, user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = database.get_db()):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = database.get_db()):
    return crud.update_user(db, user_id, user)

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = database.get_db()):
    return crud.delete_user(db, user_id=user_id)
