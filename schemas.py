from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class MembroBase(BaseModel):
    nome: str
    idade: Optional[int] = None
    sexo: Optional[str] = None
    profissao: Optional[str] = None
    data_nasc: Optional[date] = None
    telefone: Optional[str] = None
    rede_social: Optional[str] = None
    foto: Optional[str] = None
    id_celula: Optional[int] = None

class MembroCreate(MembroBase):
    create_by: Optional[int] = 1 

class MembroUpdate(MembroBase):
    updated_by: Optional[int] = 1

class MembroResponse(MembroBase):
    id: int
    created_date: Optional[datetime] = None
    update_date: Optional[datetime] = None

    class Config:
        from_attributes = True
