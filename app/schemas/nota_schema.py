from pydantic import BaseModel
from uuid import UUID

class notaCreate(BaseModel):
    codigo:int
    n1:float
    n2:float
    matricula_aluno:UUID
    cod_materia:int