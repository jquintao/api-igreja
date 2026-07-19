from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, get_db

app = FastAPI(title="API Sistema da Igreja")

@app.post("/membros/", response_model=schemas.MembroResponse)
def create_membro(membro: schemas.MembroCreate, db: Session = Depends(get_db)):
    db_membro = models.Membro(**membro.model_dump())
    db.add(db_membro)
    db.commit()
    db.refresh(db_membro)
    return db_membro

@app.get("/membros/", response_model=List[schemas.MembroResponse])
def read_membros(db: Session = Depends(get_db)):
    return db.query(models.Membro).all()
