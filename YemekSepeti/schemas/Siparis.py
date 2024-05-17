from graphene import Field
import graphene 
from graphene_django import DjangoObjectType 
from YemekSepeti.models import Siparis

class SiparisType(DjangoObjectType):
    class Meta:
        model = Siparis
class Query(graphene.ObjectType):
    siparisler = graphene.List(SiparisType)

    def resolve_siparisler(root, info):
        return Siparis.objects.all()



class SiparisEkle(graphene.Mutation):
    class Arguments:
        siparis_tarihi=graphene.DateTime(required=True)
        teslim_tarihi=graphene.DateTime(required=True)
        tutar=graphene.Float(required=True)
        durum=graphene.String(required=True)
    siparis=Field(SiparisType)

    @classmethod
    def mutate(cls, root, info,siparis_tarihi,teslim_tarihi, tutar,durum):
        siparis=Siparis()
        siparis.siparis_tarihi=siparis_tarihi
        siparis.teslim_tarihi=teslim_tarihi
        siparis.tutar=tutar
        siparis.durum=durum
        siparis.save()
        return SiparisEkle(siparis=siparis)

class SiparisGuncelle(graphene.Mutation):
    class Arguments:
        siparis_tarihi=graphene.DateTime(required=True)
        teslim_tarihi=graphene.DateTime(required=True)
        tutar=graphene.Float(required=True)
        durum=graphene.String(required=True)
    siparis=Field(SiparisType)

    @classmethod
    def mutate(cls,root, info,siparis_tarihi,teslim_tarihi,tutar,durum):
        siparis=Siparis.objects.get(pk=id)
        siparis.siparis_tarihi=siparis_tarihi
        siparis.teslim_tarihi=teslim_tarihi
        siparis.tutar=tutar
        siparis.durum=durum
        siparis.save()
        return SiparisGuncelle(siparis=siparis)


class SiparisSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    siparis=Field(SiparisType)

    @classmethod
    def mutate(cls,root,info,id):
        siparis=Siparis.objects.get(pk=id)
        return SiparisSil(siparis=siparis)

class Mutation(graphene.ObjectType):
    siparis_ekle=SiparisEkle.Field()
    siparis_guncelle=SiparisGuncelle.Field()
    siparis_sil=SiparisSil.Field()       



siparis_schema = graphene.Schema(query=Query, mutation=Mutation)