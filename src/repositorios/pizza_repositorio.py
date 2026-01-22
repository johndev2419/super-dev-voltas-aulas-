from sqlalchemy.orm import Session,contains_eager

from src.database.models import Sabores

def cadastrar(db:Session, sabor:str, tamanho:str):
    pedido = Sabores(
        sabor=sabor,
        tamanho=tamanho
        )
    
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido


def editar(db:Session, id:int, sabor:str,tamanho:str):
    pedido = db.query(Sabores).filter(Sabores.id == id).first()
    if not pedido:
        return 0
    pedido.sabor = sabor
    pedido.tamanho = tamanho
    db.commit()
    return 1 

def apagar(db:Session, id:int) -> int:

    pedido = db.query(Sabores).filter(Sabores.id == id).first()
    if not pedido:
        return 0 
    db.delete(pedido)
    db.commit()
    return 1

def obter_por_id(db:Session, id:int):
    pedido = db.query(Sabores).filter(Sabores.id == id).first()
    return pedido
