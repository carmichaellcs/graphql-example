from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from .models import Pessoa, Livro, engine


def create_pessoa(name: str, age: int):
    pessoa = Pessoa(name=name, age=age)
    with Session(engine) as session:
        session.add(pessoa)
        session.commit()
        session.refresh(pessoa)

    return pessoa

def all_pessoa():
    query = select(Pessoa)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result

def create_livro(title: str, pessoa_id: int):
    livro = Livro(title=title, pessoa_id=pessoa_id)
    with Session(engine) as session:
        session.add(livro)
        session.commit()
        session.refresh(livro)

        session.expunge_all()
        livro = session.query(Livro).options(joinedload(Livro.pessoa)).filter_by(id=livro.id).first()

    return livro

def all_livro():
    query = select(Livro).options(joinedload('*'))
    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result