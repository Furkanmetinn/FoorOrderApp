import graphene
import YemekSepeti.schema as yemek_sepeti_schema
import account.schema as account_schema

class Query(
            yemek_sepeti_schema.Query,
            # account_schema.Query,
            graphene.ObjectType):
    pass


class Mutation(
            yemek_sepeti_schema.Mutation,
            account_schema.Mutation,
            graphene.ObjectType):
    pass

schema=graphene.Schema(query=Query, mutation=Mutation)