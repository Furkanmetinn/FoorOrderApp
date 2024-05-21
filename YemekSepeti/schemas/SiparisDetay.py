from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import Siparis, SiparisDetay, Urun

class SiparisDetayType(DjangoObjectType):
    class Meta:
        model = SiparisDetay

class Query(graphene.ObjectType):
    siparisDetay = graphene.List(SiparisDetayType)

    def resolve_siparisDetay(root, info):
        return SiparisDetay.objects.all()
    
class SiparisInput(graphene.InputObjectType):  
    siparis_tarihi=graphene.DateTime()
    teslim_tarihi=graphene.DateTime()
    tutar=graphene.Float()
    durum=graphene.String()

class UrunInput(graphene.InputObjectType):
    name = graphene.String()
    image=graphene.String()
    fiyat=graphene.Float()
    detay=graphene.String()
class SiparisDetayEkle(graphene.Mutation):
    class Arguments:
        miktar=graphene.Int(required=True)
        toplam_tutar=graphene.Float(required=True)
        siparis=SiparisInput(required=True)
        urun=UrunInput(required=True)
    siparisDetay=Field(SiparisDetayType)

    @classmethod
    def mutate(cls, root,info,siparis,urun,miktar,toplam_tutar):
        siparisDetay=SiparisDetay()
        siparisDetay.miktar=miktar
        siparisDetay.toplam_tutar=toplam_tutar
        siparis=Siparis(siparis_tarihi=siparis.siparis_tarihi,teslim_tarihi=siparis.teslim_tarihi,tutar=siparis.tutar,durum=siparis.durum)
        siparis.save()
        siparisDetay.siparis_id=siparis.id
        urun=Urun(name=urun.name,image=urun.image,fiyat=urun.fiyat,detay=urun.detay)
        urun.save()
        siparisDetay.urun_id=urun.id
        siparisDetay.save()
        return SiparisDetayEkle(siparisDetay=siparisDetay)


class SiparisDetayGuncelle(graphene.Mutation):
    class Arguments:
        miktar=graphene.Int(required=True)
        toplam_tutar=graphene.Float(required=True)
        siparis=SiparisInput(required=True)
        urun=UrunInput(required=True)
    siparisDetay=Field(SiparisDetayType)

    def mutate(cls,root, info, siparis, urun,miktar,toplam_tutar):
        siparisDetay=SiparisDetay.objects.get(pk=id)
        siparisDetay.siparis=siparis
        siparisDetay.urun=urun
        siparisDetay.miktar=miktar
        siparisDetay.toplam_tutar=toplam_tutar
        siparis=Siparis(siparis_tarihi=siparis.siparis_tarihi,teslim_tarihi=siparis.teslim_tarihi,tutar=siparis.tutar,durum=siparis.durum)
        siparis.save()
        siparisDetay.siparis_id=siparis.id
        urun=Urun(name=urun.name,image=urun.image,fiyat=urun.fiyat,detay=urun.detay)
        urun.save()
        siparisDetay.siparis_id=urun.id
        siparisDetay.save()
        return SiparisDetayGuncelle(siparisDetay=siparisDetay)
        
        
        
class SiparisDetaySil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    siparisDetay=Field(SiparisDetayType)
    
    @classmethod
    def mutate(cls,root,info,id):
        siparisDetay=SiparisDetay.objects.get(pk=id)
        return SiparisDetaySil(siparisDetay=siparisDetay)
    
class Mutation(graphene.ObjectType):
    siparisDetay_ekle=SiparisDetayEkle.Field()
    siparisDetay_guncelle=SiparisDetayGuncelle.Field()
    siparisDetay_sil=SiparisDetaySil.Field()


siparisDetay_schema = graphene.Schema(query=Query, mutation=Mutation)