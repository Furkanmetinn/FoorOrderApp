from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import Urun,Category,Restoran

class UrunType(DjangoObjectType):
    class Meta:
        model = Urun

class Query(graphene.ObjectType):
    urunler = graphene.List(UrunType)

    def resolve_urunler(root, info):
        return Urun.objects.all()
    
class CategoryInput(graphene.InputObjectType):
    name=graphene.String()

class RestoranInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    adres=graphene.String(required=True)
    telefon=graphene.String(required=True)
    acilis_saati=graphene.Time(required=True)
    kapanis_saati=graphene.Time(required=True)
    email=graphene.String()
    puan=graphene.Float(required=True)
    resim=graphene.String(required=True)
    min_tutar=graphene.Float(required=True)
    category=graphene.String(required=True)

class UrunEkle(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        image=graphene.String()
        fiyat=graphene.Float(required=True)
        detay=graphene.String(required=True)
        category=CategoryInput(required=True)
        restoran=RestoranInput(required=True)
    urun=Field(UrunType)

    @classmethod
    def mutate(cls,root,info,name,image,fiyat,detay,category,restoran):
        urun=Urun()
        urun.name=name
        urun.image=image
        urun.fiyat=fiyat
        urun.detay=detay
        category=Category(name=category.name)
        category.save()
        urun.category_id=category.id
        restoran=Restoran(name=restoran.name,adres=restoran.adres,telefon=restoran.telefon, acilis_saati=restoran.acilis_saati,kapanis_saati=restoran.kapanis_saati,email=restoran.email,puan=restoran.puan,resim=restoran.resim,min_tutar=restoran.min_tutar,category=restoran.category)
        restoran.save()
        urun.restoran_id=restoran.id
        urun.save()
        return UrunEkle(urun=urun)

class UrunGuncelle(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        image=graphene.String()
        fiyat=graphene.Decimal(required=True)
        detay=graphene.String(required=True)
        category=CategoryInput(required=True)
        restoran=RestoranInput(required=True)
    urun=Field(UrunType)

    @classmethod
    def mutate(cls,root,info,name,image,fiyat,detay,category):
        urun=Urun.objects.get(pk=id)
        urun.name=name
        urun.image=image
        urun.fiyat=fiyat
        urun.detay=detay
        category=Category(name=category.name)
        category.save()
        urun.id=category.id
        restoran=Restoran(name=restoran.name,adres=restoran.adres,telefon=restoran.telefon, acilis_saati=restoran.acilis_saati,kapanis_saati=restoran.kapanis_saati,email=restoran.email,puan=restoran.puan,resim=restoran.resim,min_tutar=restoran.min_tutar,category=restoran.category)
        restoran.save()
        urun.id=restoran.id
        urun.save()
        return UrunGuncelle(urun=urun)
        
class UrunSil(graphene.Mutation):
    class Arguments:
        urun_id=graphene.ID(required=True)
    urun=Field(UrunType)

    @classmethod
    def mutate(cls,root,info,id):
        urun=Urun.objects.get(pk=id)
        return UrunSil(urun=urun)
    
class Mutation(graphene.ObjectType):
    urun_ekle=UrunEkle.Field()
    urun_guncelle=UrunGuncelle.Field()
    urun_sil=UrunSil.Field()
        

urun_schema = graphene.Schema(query=Query, mutation=Mutation)