from sqlalchemy.orm import Session
from src.database.models import Cliente






def obter_todos(db: Session):
     clientes = db.query(Cliente).all()
     return clientes


def cadastrar(db: Session, nome: str, cpf:str, id_sabor: int):
    cliente = Cliente(nome=nome, cpf=cpf, id_sabor=id_sabor)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


def editar(db: Session, id: int, nome: str,cpf: str, id_sabor: int):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        return 0 
    cliente.cpf = cpf
    cliente.nome = nome 
    cliente.id_sabor = id_sabor

    db.commit()
    return 1


def apagar(db:Session,id: int):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        return 0 
    db.delete(cliente)
    db.commit()
    return 1












def obter_por_id(db:Session, id: int):
    cliente = (db.query(Cliente)
    .filter(Cliente.id == id)
    .first()
    )
    return cliente  