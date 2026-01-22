from sqlalchemy.orm import Session, contains_eager
from src.database.models import Cliente


def cadastrar(db: Session, nome: str, cpf:str, id_sabor: int):
    cliente = Cliente(nome=nome, cpf=cpf, id_sabor=id_sabor)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


