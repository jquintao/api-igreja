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

# Adicione junto com as outras rotas no main.py

@app.post("/visitantes/", response_model=schemas.VisitanteResponse)
def create_visitante(visitante: schemas.VisitanteCreate, db: Session = Depends(get_db)):
    db_visitante = models.Visitante(**visitante.model_dump()) # ou .dict() se a versão do pydantic for mais antiga
    db.add(db_visitante)
    db.commit()
    db.refresh(db_visitante)
    return db_visitante

@app.get("/visitantes/", response_model=list[schemas.VisitanteResponse])
def read_visitantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    visitantes = db.query(models.Visitante).offset(skip).limit(limit).all()
    return visitantes
