from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class Membro(Base):
    __tablename__ = "membros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    idade = Column(Integer)
    sexo = Column(String(20))
    profissao = Column(String(150))
    data_nasc = Column(Date)
    telefone = Column(String(20))
    rede_social = Column(String(255))
    foto = Column(String(255))
    id_celula = Column(Integer)
    
    create_by = Column(Integer)
    created_date = Column(TIMESTAMP, server_default=func.now())
    updated_by = Column(Integer)
    update_date = Column(TIMESTAMP, onupdate=func.now())
    
# Adicione no final do models.py
class Visitante(Base):
    __tablename__ = "visitantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=True)
    sexo = Column(String, nullable=True)
    profissao = Column(String, nullable=True)
    data_nasc = Column(Date, nullable=True)
    telefone = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    data_visita = Column(Date, nullable=True)
    
    # Campos de Auditoria
    create_by = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=func.now())
    updated_by = Column(Integer, nullable=True)
    update_date = Column(DateTime, nullable=True, onupdate=func.now())
