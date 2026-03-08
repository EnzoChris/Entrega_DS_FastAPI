from sqlalchemy import Column, String,Integer
from sqlalchemy.orm import relationship
from enum import Enum

from model.base import Base
from model.professor_disciplina import professor_disciplina


class Disciplina(Base):

    __tablename__ = "disciplina"

    codigo = Column(Integer, primary_key=True)
    nome = Column(String, name=False)

    notas = relationship("Nota", back_populates="disciplinas")
    professores = relationship("Professor",secondary=professor_disciplina, back_populates="disciplinas")