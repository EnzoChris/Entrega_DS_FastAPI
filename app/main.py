from model.observacoes import Observacoes
from model.notas import Nota

from repositories.professor_repository import ProfessorRepository
from repositories.aluno_repository import AlunoRepository
from repositories.notas_repository import NotasRepository
from repositories.observacoes_repository import ObervacoesRepository

from services.professor_service import ProfessorService
from services.aluno_service import AlunoService
from services.notas_service import NotasService
from services.observacoes_service import ObservacoesService
from core.init_db import init_db


from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse


app = FastAPI()


professor_service = ProfessorService(ProfessorRepository())
aluno_service = AlunoService(AlunoRepository())
notas_service = NotasService(NotasRepository())
observacoes_service = ObservacoesService(ObervacoesRepository())


@app.on_event("startup")
def startup():
    init_db()


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Erro interno no servidor"
        }
    )


@app.get("/api/login-professor/{usuario}/{senha}")
def get_veri_professor(usuario:str, senha:str):

    professor = professor_service.login_professor(usuario, senha)
    alunos = aluno_service.buscar_alunos_por_professor(usuario)
    qnt_notas = professor_service.contar_notas_lancadas(usuario)
    media_alunos = professor_service.calc_media_geral(usuario)

    return {
        "professor":professor,
        "qnt_professores":qnt_notas,
        "media_alunos":media_alunos,
        "alunos":alunos
    }


@app.get("/api/login-aluno/{email}/{senha}")
def get_veri_aluno(email:str, senha:str):
    aluno = aluno_service.login_aluno(email, senha)
    notas_aluno = notas_service.carregar_nota(email)
    observacoes_aluno = observacoes_service.carregar_obervacoes(email)

    return {
        "aluno":aluno,
        "notas": notas_aluno,
        "observacoes_aluno":observacoes_aluno
    }


@app.post("/api/enviar-observacao/")
def enviar_observcao(observacao:Observacoes):
    observacao = observacoes_service.registrar_observacao(observacao)

    return {"observacao":observacao}


@app.delete("/api/enviar-observacao/{usuario}")
def apagar_observcao(usuario:str):
    observacoes_service.apagar_observacao(usuario)


@app.post("/api/lancar-nota/{matricula}")
def lancar_nota(matricula:str, nota:Nota):

    nota_resp = notas_service.atualizar_nota(matricula, nota)

    return {"nota":nota_resp}


@app.post("/api/completar-cadastro/{matricula}/{email}/{senha}")
def completar_cadastro_endpoint(matricula:str, email:str, senha:str):

    resposta = aluno_service.completar_cadatro(matricula, email, senha)

    return {"aluno":resposta}
