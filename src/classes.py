
from pydantic import BaseModel

class SaboresCriar(BaseModel):
    sabor:str
    tamanho:str
 
class SaboresEditar(BaseModel):
    sabor:str
    tamanho:str

class ClienteCriar(BaseModel):
    nome:str
    cpf:str
    id_sabor:int
    tamanho: str
    

class ClienteEditar(BaseModel):
    nome:str
    cpf:str
    id_sabor:int
    tamanho: str 
