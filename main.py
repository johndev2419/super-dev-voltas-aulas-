from fastapi import Depends, FastAPI, HTTPException


from classes import SaboresCriar, SaboresEditar
from src.database.conexao import get_db
from src.repositorios import pizza_repositorio
from sqlalchemy.orm import Session
app = FastAPI()

#listar tudo
@app.get("/api/v1/sabores", tags=["Sabores"])
def listar_todos(db:Session = Depends(get_db)):
    pedido = pizza_repositorio.obter_todos(db)
    return pedido

#cadastrar
@app.post("api/v1/sabores",tags=["Sabores"])
def cadastrar_sabor(pedido:SaboresCriar,db:Session = Depends(get_db)):
    pizza_repositorio.cadastrar(db, pedido.sabor,pedido.tamanho)
    return{
        "Status":"Ok"
    }

#editar
@app.put("api/v1/sabores/{id}",tags=["Sabores"])
def alterar_sabor(id:int, pedido:SaboresEditar,db:Session = Depends(get_db)):
    linhas_afetadas = pizza_repositorio.editar(db,id,pedido.sabor,pedido.tamanho)
    if linhas_afetadas !=1:
        raise HTTPException(status_code=404,detail="Sabor de pizza não encontrado")
    return{
        "Status":"Ok"
    }

#apagar
@app.delete("api/v1/sabores/{id}",tags=["Sabores"])
def apagar_sabor(id:int,db:Session = Depends(get_db)):
    linhas_afetadas = pizza_repositorio.apagar(db,id)
    if linhas_afetadas !=1:
        raise HTTPException(status_code=404,detail="Sabor de pizza não encontrado")
    return{
        "Status":"Ok"
    }

#obter por id
@app.get("api/v1/sabores/{id}",tags=["Sabores"])
def obter_sabor_por_id(id:int,db:Session = Depends(get_db)):
    pedido = pizza_repositorio.obter_por_id(db,id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Sabor de pizza não encontrado")
    return pedido