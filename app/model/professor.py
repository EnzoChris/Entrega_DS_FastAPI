from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from model.base import Base
from model.professor_disciplina import professor_disciplina

class Professor(Base):

    __tablename__ = "professor"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    
    nome = Column(String(100), nullable=False)
    usuario = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)

    observacoes = relationship("Observacoes", back_populates="professores")
    disciplinas = relationship("Disciplina",secondary=professor_disciplina, back_populates="professores")


    def to_dict(self):
        return {
            "id": str(self.id),
            "nome": self.nome,
            "usuario": self.usuario,
            "senha": self.senha
        }