from sqlalchemy import Table, Column,ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from model.base import Base

professor_disciplina = Table(
"professor_disciplina",
Base.metadata,
Column("professor_id", UUID, ForeignKey("professor.id"), primary_key=True),
Column("disciplina_id", Integer, ForeignKey("disciplina.codigo"), primary_key=True)
)