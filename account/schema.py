from .schemas.kullanici import kullanici_schema

import graphene

class Query(kullanici_schema.Query,graphene.ObjectType):
    pass

class Mutation (kullanici_schema.Mutation,graphene.ObjectType):
    pass

schema=graphene.Schema(query=Query, mutation=Mutation)