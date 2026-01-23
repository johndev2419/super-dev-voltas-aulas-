from sqlalchemy.orm import Session, contains_eager
from src.database.models import Cliente


def cadastrar(db: Session, nome: str, cpf:str, id_sabor: int, tamanho: str):
    cliente = Cliente(nome=nome, cpf=cpf, id_sabor=id_sabor, tamanho = tamanho)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


def editar(db: Session, id: int, nome: str, id_sabor: int, tamanho: str ):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        return 0 
    cliente.nome = nome 
    cliente.id_sabor = id_sabor
    cliente.tamanho = tamanho
    db.commit()
    return 1


def apagar(db:Session,id: int):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        return 0 
    db.delete(cliente)
    db.commit()
    return 1


def obter_todos(db: Session):
    cliente = db.query(Cliente).options(contains_eager(Cliente.sabor)).all()
    return cliente


def obter_por_id(db:Session, id: int):
    cliente = db.query(Cliente)\
    .options(contains_eager(Cliente.sabor))\
    .filter(Cliente.id == id)\
    .first()
    return cliente