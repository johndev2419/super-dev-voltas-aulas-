from datetime import date
from pydantic import BaseModel

class SaboresCriar(BaseModel):
    sabor:str
 
class SaboresEditar(BaseModel):
    sabor:str

class ClienteCriar(BaseModel):
    nome:str
    cpf:str
    id_sabor:int

class ClienteEditar(BaseModel):
    nome:str
    cpf:str
    id_sabor:int