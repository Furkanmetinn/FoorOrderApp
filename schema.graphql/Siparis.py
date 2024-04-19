from graphene import Field
import graphene 
from graphene_django import DjangoObjectType 
from YemekSepeti.models import Siparis

class SiparisType(DjangoObjectType):
    class Meta:
        model = Siparis

class SiparisType(graphene.ObjectType):
    sip_id=graphene.ID(required=True)
    mus_id=graphene.ID(required=True)
    siparis_tarihi=graphene.DateTime(required=True)
    teslim_tarihi=graphene.DateTime(required=True)
    tutar=graphene.Decimal(required=True)
    durum=graphene.String(required=True)

class SiparisMutasyon(graphene.Mutation):
    class SiparisEkle(graphene.Mutation):
        class Arguments:
            sip_id=graphene.ID(required=True)
            mus_id=graphene.ID(required=True)
            siparis_tarihi=graphene.DateTime(required=True)
            teslim_tarihi=graphene.DateTime(required=True)
            tutar=graphene.Decimal(required=True)
            durum=graphene.String(required=True)
        siparis=Field(SiparisType)

    class SiparisGuncelle(graphene.Mutation):
        class Arguments:
            sip_id=graphene.ID(required=True)
            mus_id=graphene.ID(required=True)
            siparis_tarihi=graphene.DateTime(required=True)
            teslim_tarihi=graphene.DateTime(required=True)
            tutar=graphene.Decimal(required=True)
            durum=graphene.String(required=True)
        siparis=Field(SiparisType)

    class SiparisSil(graphene.Mutation):
        class Arguments:
            id=graphene.ID(required=True)

class Query(graphene.ObjectType):
    siparisler = graphene.List(SiparisType)

    def resolve_siparisler(self, info):
        return Siparis.objects.all()



schema = graphene.Schema(query=Query, mutation=SiparisMutasyon)