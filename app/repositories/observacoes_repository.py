from model.observacoes import Observacoes
from model.aluno import Aluno
from model.professor import Professor
from repositories.aluno_repository import AlunoRepository
from repositories.professor_repository import ProfessorRepository
from uuid import UUID

aluno_repository = AlunoRepository()
professor_repository = ProfessorRepository()

class ObervacoesRepository:

    def __init__(self, db):
        self.db = db


    def list(self):
        return self.db.query(Observacoes).all()



    
    def carregar_obervacoes(self, email:str):

        aluno = aluno_repository.buscar_por_email(email)

        return (self.db.query(Observacoes.id_remetente, Observacoes.mensagem, Observacoes.data_envio)
                .filter(Observacoes.id_destinatario == aluno.matricula)
                .all()
                )


    
    def registrar_observacao(self, observacao:Observacoes):
        self.db.add(observacao)

        self.db.commit()

        return observacao




    def buscar_por_remetente(self, id_remetente:UUID):

        observacoes = self.db.query(Observacoes).filter(
            Observacoes.id_remetente == id_remetente
        ).all()
        return observacoes
    



    def apagar_observacao(self, usuario_professor:str):
        professor = professor_repository.buscar_por_usuario(usuario_professor)
        observacao = self.db.query(Observacoes).filter(
            Observacoes.id_remetente == professor.id
        ).first()

        if not observacao:
            return None
    
        self.db.delete(observacao)
        self.db.commit()




