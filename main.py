from fastapi import Depends, FastAPI, HTTPException


from src.classes import ClienteCriar, ClienteEditar, SaboresCriar, SaboresEditar
from src.database.conexao import get_db
from src.repositorios import pizza_repositorio, cliente_repositorio
from sqlalchemy.orm import Session


app = FastAPI()



#listar tudo
@app.get("/api/v1/sabores", tags=["Sabores"])
def listar_todos(db:Session = Depends(get_db)):
    pedido = pizza_repositorio.obter_todos(db)
    return pedido

#cadastrar
@app.post("/api/v1/sabores",tags=["Sabores"])
def cadastrar_sabor(pedido:SaboresCriar,db:Session = Depends(get_db)):
    pedido = pizza_repositorio.cadastrar(db, pedido.sabor,pedido.tamanho)
    return pedido

#editar
@app.put("/api/v1/sabores/{id}",tags=["Sabores"])
def alterar_sabor(id:int, pedido:SaboresEditar,db:Session = Depends(get_db)):
    linhas_afetadas = pizza_repositorio.editar(db,id,pedido.sabor,pedido.tamanho)
    if linhas_afetadas !=1:
        raise HTTPException(status_code=404,detail="Sabor de pizza não encontrado")
    return{
        "Status":"Ok"
    }

#apagar
@app.delete("/api/v1/sabores/{id}",tags=["Sabores"])
def apagar_sabor(id:int,db:Session = Depends(get_db)):
    linhas_afetadas = pizza_repositorio.apagar(db,id)
    if linhas_afetadas !=1:
        raise HTTPException(status_code=404,detail="Sabor de pizza não encontrado")
    return{
        "Status":"Ok"
    }

#obter por id
@app.get("/api/v1/sabores/{id}",tags=["Sabores"])
def obter_sabor_por_id(id:int,db:Session = Depends(get_db)):
    pedido = pizza_repositorio.obter_por_id(db,id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Sabor de pizza não encontrado")
    return pedido


@app.get("/api/v1/cliente", tags=["Clientes"])
def obter_todos_clientes(db: Session = Depends (get_db)):
    clientes = cliente_repositorio.obter_todos(db)
    return clientes  


@app.post("/api/v1/cliente", tags=["Clientes"])
def cadastrar_clientes(cliente: ClienteCriar, db: Session = Depends(get_db)):
    cliente_repositorio.cadastrar(db,cliente.nome, cliente.cpf, cliente.id_sabor, cliente.tamanho)
    return {"status" : "ok"}


@app.put("/api/v1/cliente/{id}", tags=["Clientes"])
def editar_clientes(cliente: ClienteEditar, id: int, db: Session = Depends(get_db)):
    linhas_afetadas = cliente_repositorio.editar(db, id, cliente.nome,cliente.cpf,cliente.id_sabor, cliente.tamanho)
    if linhas_afetadas !=1 :
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return{
        "status" : "ok"
    }


@app.get("/api/v1/cliente/{id}", tags=["Clientes"])
def obter_cliente_por_id(id:int, db: Session = Depends(get_db)) :
    cliente = cliente_repositorio.obter_por_id(db,id)
    if cliente is None :
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


@app.delete("/api/v1/cliente/{id}", tags=["Clientes"])
def apagar_clientes(id:int, db: Session = Depends(get_db)):
    linhas_afetadas = cliente_repositorio.apagar(db,id)
    if linhas_afetadas != 1:
         raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return{"status" : "ok"}
        
    

