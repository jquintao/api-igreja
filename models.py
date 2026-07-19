from sqlalchemy import Column, Integer, String, Date, ForeignKey, TIMESTAMP
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
