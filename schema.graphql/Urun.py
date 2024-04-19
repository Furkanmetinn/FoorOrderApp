from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import Urun

class UrunType(DjangoObjectType):
    class Meta:
        model = Urun

class UrunType(graphene.ObjectType):
    id=graphene.ID(required=True)
    name = graphene.String(required=True)
    image=graphene.String()
    price=graphene.Decimal(required=True)
    description=graphene.String(required=True)

class UrunMutasyon(graphene.Mutation):
    class UrunEkle(graphene.Mutation):
        class Arguments:
            name = graphene.String(required=True)
            image=graphene.String()
            price=graphene.Decimal(required=True)
            description=graphene.String(required=True)
        urun=Field(UrunType)

    class UrunGuncelle(graphene.Mutation):
        class Arguments:
            name = graphene.String(required=True)
            image=graphene.String()
            price=graphene.Decimal(required=True)
            description=graphene.String(required=True)
        urun=Field(UrunType)

    class UrunSil(graphene.Mutation):
        class Arguments:
            id=graphene.ID(required=True)

class Query(graphene.ObjectType):
    urunler = graphene.List(UrunType)

    def resolve_urunler(self, info):
        return Urun.objects.all()



schema = graphene.Schema(query=Query, mutation=UrunMutasyon)