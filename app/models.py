from typing import Optional, List
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Relationship
)

# Conecção com BD
engine = create_engine('sqlite:///database.db')

# Model
class Pessoa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int

    livros: List['Livro'] = Relationship(back_populates='pessoa')


class Livro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str

    pessoa_id: Optional[int] = Field(default=None, foreign_key='pessoa.id')
    pessoa: Optional[Pessoa] = Relationship(back_populates='livros')


# Instancia BD
SQLModel.metadata.create_all(engine)
