from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import RestoranDetay

class RestoranDetayType(DjangoObjectType):
    class Meta:
        model = RestoranDetay
        fields=["id"]

class Query(graphene.ObjectType):
    restoranDetay = graphene.List(RestoranDetayType)
    restoranDetay_id=graphene.Field(RestoranDetayType, id=graphene.String())

    def resolve_restoranDetay(self, info):
        return RestoranDetay.objects.all()
    
    def resolve_restoranDetay_id(root,info,id):
        return RestoranDetay.objects.get(pk=id)


class RestoranDetayEkle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        restoran_name = graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
        acilis_saati=graphene.Time(required=True)
        kapanis_saati=graphene.Time(required=True)
        email=graphene.String()
        puan=graphene.Decimal(required=True)
        resim=graphene.String(required=True)
        min_tutar=graphene.Decimal(required=True)
    restoranDetay=Field(RestoranDetayType)
        
    @classmethod
    def mutate(cls,root,info,id,restoran_name,adres,telefon,acilis_saati,kapanis_saati,email,puan,resim,min_tutar):
        restoranDetay=RestoranDetay.objects.get(pk=id)
        restoranDetay.restoran_name=restoran_name
        restoranDetay.adres=adres
        restoranDetay.telefon=telefon
        restoranDetay.acilis_saati=acilis_saati
        restoranDetay.kapanis_saati=kapanis_saati
        restoranDetay.email=email
        restoranDetay.puan=puan
        restoranDetay.resim=resim
        restoranDetay.min_tutar=min_tutar
        restoranDetay.save()
        return RestoranDetayEkle(restoranDetay=RestoranDetay)
        
class RestoranDetayGuncelle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        restoran_name = graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
        acilis_saati=graphene.Time(required=True)
        kapanis_saati=graphene.Time(required=True)
        email=graphene.String()
        puan=graphene.Decimal(required=True)
        resim=graphene.String(required=True)
        min_tutar=graphene.Decimal()
    restoranDetay=Field(RestoranDetayType)

    @classmethod
    def mutate(cls, root, info, id,restoran_name, adres,telefon, acilis_saati, kapanis_saati, email, puan, resim,min_tutar):
        restoranDetay=RestoranDetay.objects.get(pk=id)
        restoranDetay.restoran_name=restoran_name
        restoranDetay.adres=adres
        restoranDetay.telefon=telefon
        restoranDetay.acilis_saati=acilis_saati
        restoranDetay.kapanis_saati=kapanis_saati
        restoranDetay.email=email
        restoranDetay.puan=puan
        restoranDetay.resim=resim
        restoranDetay.min_tutar=min_tutar
        restoranDetay.save()
        return RestoranDetayGuncelle(restoranDetay=restoranDetay)

class RestoranDetaySil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    RestoranDetay=Field(RestoranDetayType)

    @classmethod
    def mutate(cls, root, info, id):
        restoranDetay=RestoranDetay.objects.get(pk=id)
        return RestoranDetaySil(restoranDetay=restoranDetay)
    
class Mutation(graphene.ObjectType):
    restoranDetay_ekle=RestoranDetayEkle.Field()
    restoranDetay_guncelle=RestoranDetayGuncelle.Field()
    restoranDetay_sil=RestoranDetaySil.Field()

  
restoranDetay_schema = graphene.Schema(query=Query, mutation=Mutation)