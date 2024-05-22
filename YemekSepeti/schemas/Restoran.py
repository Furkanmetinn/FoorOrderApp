from graphene import Decimal, Field, ObjectType
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import Restoran,Urun

class RestoranType(DjangoObjectType):
    class Meta:
        model = Restoran

class Query(graphene.ObjectType):
    restoranlar = graphene.List(RestoranType)

    def resolve_restoranlar(root, info):
        return Restoran.objects.all()


class RestoranEkle(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
        acilis_saati=graphene.Time(required=True)
        kapanis_saati=graphene.Time(required=True)
        email=graphene.String()
        sifre=graphene.String()
        puan=graphene.Float(required=True)
        resim=graphene.String(required=True)
        min_tutar=graphene.Float(required=True)
        category=graphene.String(required=True)
        hesap_tipi=graphene.String(required=True)

    restoran=Field(RestoranType)
        
    @classmethod
    def mutate(cls,root,info,name,adres,telefon,acilis_saati,kapanis_saati,email,sifre,puan,resim,min_tutar,category,hesap_tipi):
        restoran=Restoran()
        restoran.name=name
        restoran.adres=adres
        restoran.telefon=telefon
        restoran.acilis_saati=acilis_saati
        restoran.kapanis_saati=kapanis_saati
        restoran.email=email
        restoran.sifre=sifre
        restoran.puan=puan
        restoran.resim=resim
        restoran.min_tutar=min_tutar
        restoran.category=category
        restoran.hesap_tipi=hesap_tipi
        restoran.save()
        return RestoranEkle(restoran=restoran)

class RestoranGuncelle(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
        acilisSaati=graphene.Time(required=True)
        kapanis_saati=graphene.Time(required=True)
        email=graphene.String()
        sifre=graphene.String()
        puan=graphene.Decimal(required=True)
        resim=graphene.String(required=True)
        min_tutar=graphene.Decimal(required=True)
        category=graphene.String(required=True)
        hesap_tipi=graphene.String(required=True)
    restoran=Field(RestoranType)

    @classmethod
    def mutate(cls,root,info,name,adres,telefon,acilis_saati,kapanis_saati,email,sifre,puan,resim,min_tutar,category,hesap_tipi):
        restoran=Restoran.objects.get(pk=id)
        restoran.name=name
        restoran.adres=adres
        restoran.telefon=telefon
        restoran.acilis_saati=acilis_saati
        restoran.kapanis_saati=kapanis_saati
        restoran.email=email
        restoran.sifre=sifre
        restoran.puan=puan
        restoran.resim=resim
        restoran.min_tutar=min_tutar
        restoran.category=category
        restoran.hesap_tipi=hesap_tipi
        restoran.save()
        return RestoranGuncelle(restoran=restoran)
          
        
class RestoranSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    restoran=Field(RestoranType)

    @classmethod
    def mutate(cls,root,info,id):
        restoran=Restoran.objects.get(pk=id)
        return RestoranSil(restoran=restoran)
    
class Mutation(graphene.ObjectType):
    restoran_ekle=RestoranEkle.Field()
    restoran_guncelle=RestoranGuncelle.Field()
    restoran_sil=RestoranSil.Field()

       
restoran_schema = graphene.Schema(query=Query, mutation=Mutation)