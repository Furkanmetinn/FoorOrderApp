from graphene import Field
import graphene 
from graphene_django import DjangoObjectType 
from YemekSepeti.models import Musteri

class MusteriType(DjangoObjectType):
    class Meta:
        model = Musteri

class MusteriType(graphene.ObjectType):
    id=graphene.ID(required=True)
    name = graphene.String(required=True)
    surname = graphene.String(required=True)
    address=graphene.String(required=True)
    phone_number=graphene.String(required=True)

class MusteriMutasyon(graphene.Mutation):
    class MusteriEkle(graphene.Mutation):
        class Arguments:
            name = graphene.String(required=True)
            surname = graphene.String(required=True)
            address=graphene.String(required=True)
            phone_number=graphene.String(required=True)
        musteri=Field(MusteriType)

    class MusteriGuncelle(graphene.Mutation):
        class Arguments:
            name = graphene.String(required=True)
            surname = graphene.String(required=True)
            email=graphene.String(required=True)
            address=graphene.String(required=True)
            phone_number=graphene.String(required=True)
        musteri=Field(MusteriType)

    class MusteriSil(graphene.Mutation):
        class Arguments:
            id=graphene.ID(required=True)

class Query(graphene.ObjectType):
    müşteriler = graphene.List(MusteriType)

    def resolve_müşteriler(self, info):
        return Musteri.objects.all()



schema = graphene.Schema(query=Query, mutation=MusteriMutasyon)