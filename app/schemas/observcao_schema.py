from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class observacaoCrete(BaseModel):
    id:UUID
    mensagem:str
    data_envio:datetime
    id_destinatario:UUID
    id_remetente:UUID