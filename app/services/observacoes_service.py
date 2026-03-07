from repositories.observacoes_repository import ObervacoesRepository 
from services.aluno_service import AlunoService
from model.aluno import Aluno
from model.observacoes import Observacoes
from repositories.professor_repository import ProfessorRepository
from uuid import UUID

class ObservacoesService:

    def __init__(self, observacoes_repository:ObervacoesRepository):
        self.observacoes_repository = observacoes_repository


    def listar_observacoes(self):
        observacoes = self.observacoes_repository.list()
        return [
                {
                "mensagem": observacao.mensagem,
                "data_envio": observacao.data_envio,
                "id_destinatario": observacao.id_destinatario,
                "id_remetente": observacao.id_remetente
                } for observacao in observacoes
        ]
    

    def carregar_obervacoes(self, email:str):
            
        observacoes = self.observacoes_repository.carregar_obervacoes(email)
        return [
            {
                "mensagem": observacao.mensagem,
                "data_envio": observacao.data_envio,
                "id_destinatario": observacao.id_destinatario,
                "id_remetente": observacao.id_remetente
            } for observacao in observacoes
        ]


    def registrar_observacao(self, observacao:Observacoes):
        
        return self.observacoes_repository.registrar_observacao(observacao)
            

    def buscar_por_remetente(self, id_remetente:str):
        
        id_remetente_uuid = UUID(id_remetente)
        return (self.observacoes_repository.buscar_por_remetente(id_remetente_uuid))
        
    
    def apagar_observacao(self, usuario:str):

        self.observacoes_repository.apagar_observacao(usuario)

