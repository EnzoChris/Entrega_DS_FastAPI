from repositories.notas_repository import NotasRepository
from repositories.aluno_repository import AlunoRepository
from repositories.professor_repository import ProfessorRepository
from model.notas import Nota
from uuid import UUID

class NotasService:

    def __init__(self, notas_repository:NotasRepository):
        self.notas_repository = notas_repository

    def listar_notas(self):
            notas = self.notas_repository.list()
            return [
                {
                    "n1":nota.n1,
                    "n2":nota.n2,
                    "matricula_aluno":nota.matricula_aluno,
                    "cod_materia":nota.cod_materia
                } for nota in notas
            ]


    def carregar_nota(self, email:str):
            
            notas = self.notas_repository.carregar_nota(email)
            return [
                {
                    "n1":nota.n1,
                    "n2":nota.n2,
                    "matricula_aluno":nota.matricula_aluno,
                    "cod_materia":nota.cod_materia
                } for nota in notas
            ]
         

    def atualizar_nota(self, matricula:str, nota:Nota):
            
        matricula_uuid = UUID(matricula)
        return self.notas_repository.atualizar_nota(matricula_uuid, nota)
                  

    def buscar_notas_por_professor(self, usuario_professor:str):

        self.notas_repository.buscar_notas_por_professor(usuario_professor)



