from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import SiparisDetay

class SiparisDetayType(DjangoObjectType):
    class Meta:
        model = SiparisDetay

class Query(graphene.ObjectType):
    siparisDetay = graphene.List(SiparisDetayType)

    def resolve_siparisDetay(root, info):
        return SiparisDetay.objects.all()
    


class SiparisDetayEkle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        siparis=graphene.String(required=True)
        urun=graphene.String(required=True)
        miktar=graphene.Int(required=True)
        fiyat=graphene.Decimal(required=True)
        toplam_tutar=graphene.Decimal(required=True)
    siparisDetay=Field(SiparisDetayType)

    @classmethod
    def mutate(cls, root,info, id,siparis,urun,miktar,fiyat,toplam_tutar):
        siparisDetay=SiparisDetay()
        siparisDetay.siparis=siparis
        siparisDetay.urun=urun
        siparisDetay.miktar=miktar
        siparisDetay.fiyat=fiyat
        siparisDetay.toplam_tutar=toplam_tutar
        siparisDetay.save()
        return SiparisDetayEkle(siparisDetay=siparisDetay)


class SiparisDetayGuncelle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        siparis=graphene.String(required=True)
        urun=graphene.String(required=True)
        miktar=graphene.Int(required=True)
        fiyat=graphene.Decimal(required=True)
        toplam_tutar=graphene.Decimal(required=True)
    siparisDetay=Field(SiparisDetayType)

    def mutate(cls,root, info, id, siparis, urun,miktar,fiyat,toplam_tutar):
        siparisDetay=SiparisDetay.objects.get(pk=id)
        siparisDetay.siparis=siparis
        siparisDetay.urun=urun
        siparisDetay.miktar=miktar
        siparisDetay.fiyat=fiyat
        siparisDetay.toplam_tutar=toplam_tutar
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