from sqlalchemy import Column, Date, Double, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Sabores(Base):

    __tablename__="sabores"

    id = Column(Integer, primary_key = True, autoincrement=True)
    sabor = Column(String(100), nullable=False)

class Clientes(Base):

    __tablename__="cliente"

    id = Column(Integer, primary_key = True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(14), nullable=False)

    id_sabor = Column(Integer, ForeignKey("sabores.id") )

    sabor = relationship("sabores", back_populates="cliente")