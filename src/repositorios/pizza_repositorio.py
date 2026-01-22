from sqlalchemy.orm import Session,contains_eager

from src.database.models import Sabores

def cadastrar(db:Session, sabor:str):
    pedido = Sabores(
        sabor=sabor
        )
    
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido


def editar(db:Session, id:int, sabor:str):
    pedido = db.query(Sabores).filter(Sabores.id == id).first()
    if not pedido:
        return 0
    pedido.sabor = sabor
    db.commit()
    return 1 
