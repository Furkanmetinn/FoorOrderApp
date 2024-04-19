from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import SiparisDetay

class SiparisDetayType(DjangoObjectType):
    class Meta:
        model = SiparisDetay

class SiaprisDetayType(graphene.ObjectType):
    siparis=graphene.String(required=True)
    urun=graphene.String(required=True)
    miktar=graphene.Int(required=True)
    fiyat=graphene.Decimal(required=True)
    toplam_tutar=graphene.Decimal(required=True)

class SiparisDetayMutasyon(graphene.Mutation):
    class Arguments:
        siparis=graphene.String(required=True)
        urun=graphene.String(required=True)
        miktar=graphene.Int(required=True)
        fiyat=graphene.Decimal(required=True)
        toplam_tutar=graphene.Decimal(required=True)
    siparisDetay=Field(SiparisDetayType)

    
class Query(graphene.ObjectType):
    siparisDetay = graphene.List(SiparisDetayType)

    def resolve_siparisDetay(self, info):
        return SiparisDetay.objects.all()



schema = graphene.Schema(query=Query, mutation=SiparisDetayMutasyon)