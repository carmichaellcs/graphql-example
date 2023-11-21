from typing import Optional, List
import strawberry
from strawberry.fastapi import GraphQLRouter
from .db_function import (
    create_pessoa,
    all_pessoa,
    create_livro,
    all_livro
)

# Schema
@strawberry.type
class PessoaSchema:
    id: Optional[int]
    name: str
    age: int
    livros: List['LivroSchema']


@strawberry.type
class LivroSchema:
    id: Optional[int]
    title: str
    pessoa: PessoaSchema


@strawberry.type
class Query:
    all_pessoa: List[PessoaSchema] = strawberry.field(resolver=all_pessoa)
    all_livro: List[LivroSchema] = strawberry.field(resolver=all_livro)


@strawberry.type
class Mutation:
    create_pessoa: PessoaSchema = strawberry.field(resolver=create_pessoa)
    create_livro: LivroSchema = strawberry.field(resolver=create_livro)



schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)