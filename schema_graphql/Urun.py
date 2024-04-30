from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import Urun

class UrunType(DjangoObjectType):
    class Meta:
        model = Urun
        fields=["id"]

class Query(graphene.ObjectType):
    urunler = graphene.List(UrunType)
    urunler_id=graphene.Field(UrunType, id=graphene.String())

    def resolve_urunler(root, info):
        return Urun.objects.all()
    
    def resolve_urunler_id(root,info,id):
        return Urun.objects.get(pk=id)

class UrunEkle(graphene.Mutation):
    class Arguments:
        urun_id=graphene.ID()
        name = graphene.String(required=True)
        image=graphene.String()
        fiyat=graphene.Decimal(required=True)
        detay=graphene.String(required=True)
        category=graphene.String(required=True)
    urun=Field(UrunType)

    @classmethod
    def mutate(cls,root,info,urun_id,name,image,fiyat,detay,category):
        urun=Urun.objects.get(pk=urun_id)
        urun.name=name
        urun.image=image
        urun.fiyat=fiyat
        urun.detay=detay
        urun.category=category
        urun.save()
        return UrunEkle(urun=urun)

class UrunGuncelle(graphene.Mutation):
    class Arguments:
        urun_id=graphene.ID()
        name = graphene.String(required=True)
        image=graphene.String()
        fiyat=graphene.Decimal(required=True)
        detay=graphene.String(required=True)
        category=graphene.String(required=True)
    urun=Field(UrunType)

    @classmethod
    def mutate(cls,root,info,urun_id,name,image,fiyat,detay,category):
        urun=Urun.objects.get(pk=urun_id)
        urun.name=name
        urun.image=image
        urun.fiyat=fiyat
        urun.detay=detay
        urun.category=category
        urun.save()
        return UrunGuncelle(urun=urun)
        
class UrunSil(graphene.Mutation):
    class Arguments:
        urun_id=graphene.ID(required=True)
    urun=Field(UrunType)

    @classmethod
    def mutate(cls,root,info,urun_id):
        urun=Urun.objects.get(pk=urun_id)
        return UrunSil(urun=urun)
    
class Mutation(graphene.ObjectType):
    urun_ekle=UrunEkle.Field()
    urun_guncelle=UrunGuncelle.Field()
    urun_sil=UrunSil.Field()
        

urun_schema = graphene.Schema(query=Query, mutation=Mutation)