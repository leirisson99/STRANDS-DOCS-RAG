from typing import Literal
from pydantic import BaseModel, Field


class Ticket(BaseModel):
    titulo: str = Field(description="Resumo do problema em uma linha")
    categoria: Literal["rede", "hardware", "software", "acesso"]
    prioridade: Literal["baixa", "media", "alta"]
    descricao: str = Field(description="O que foi relatado e o que foin tentando")
