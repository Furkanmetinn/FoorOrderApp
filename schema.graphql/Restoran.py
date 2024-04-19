from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import Restoran

class RestoranType(DjangoObjectType):
    class Meta:
        model = Restoran

class RestoranType(graphene.ObjectType):
    id=graphene.ID(required=True)
    name = graphene.String(required=True)
    address=graphene.String(required=True)
    phone_number=graphene.String(required=True)

class RestoranMutasyon(graphene.Mutation):
    class RestoranEkle(graphene.Mutation):
        class Arguments:
            name = graphene.String(required=True)
            surname = graphene.String(required=True)
            address=graphene.String(required=True)
            phone_number=graphene.String(required=True)
        restoran=Field(RestoranType)

    class RestoranGuncelle(graphene.Mutation):
        class Arguments:
            name = graphene.String(required=True)
            surname = graphene.String(required=True)
            address=graphene.String(required=True)
            phone_number=graphene.String(required=True)
        restoran=Field(RestoranType)

    class RestoranSil(graphene.Mutation):
        class Arguments:
            id=graphene.ID(required=True)

class Query(graphene.ObjectType):
    restoranlar = graphene.List(RestoranType)

    def resolve_restoranlar(self, info):
        return Restoran.objects.all()



schema = graphene.Schema(query=Query, mutation=RestoranMutasyon)