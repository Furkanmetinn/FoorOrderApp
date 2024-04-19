from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import RestoranDetay

class RestoranDetayType(DjangoObjectType):
    class Meta:
        model = RestoranDetay

class RestoranDetayType(graphene.ObjectType):
    id=graphene.ID(required=True)
    restoran_name = graphene.String(required=True)
    adres=graphene.String(required=True)
    telefon=graphene.String(required=True)
    acilis_saati=graphene.Time(required=True)
    kapanis_saati=graphene.Time(required=True)
    puan=graphene.Decimal(required=True)
    resim=graphene.String(required=True)

class RestoranDetayMutasyon(graphene.Mutation):
    class Arguments:
        restoran_name = graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
        acilis_saati=graphene.Time(required=True)
        kapanis_saati=graphene.Time(required=True)
        puan=graphene.Decimal(required=True)
        resim=graphene.String(required=True)
    restoranDetay=Field(RestoranDetayType)

    
class Query(graphene.ObjectType):
    restoranDetay = graphene.List(RestoranDetayType)

    def resolve_restoranDetay(self, info):
        return RestoranDetay.objects.all()



schema = graphene.Schema(query=Query, mutation=RestoranDetayMutasyon)