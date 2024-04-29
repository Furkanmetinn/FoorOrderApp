from graphene import Field
import graphene 
from graphene_django import DjangoObjectType
from YemekSepeti.models import Restoran

class RestoranType(DjangoObjectType):
    class Meta:
        model = Restoran
        fields=["id"]

class Query(graphene.ObjectType):
    restoranlar = graphene.List(RestoranType)
    restoranlar_id=graphene.Field(RestoranType, id=graphene.String())

    def resolve_restoranlar(root, info):
        return Restoran.objects.all()
    def resolve_restoranlar_id(root,info,id):
        return Restoran.objects.get(pk=id)



class RestoranEkle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        name = graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
    restoran=Field(RestoranType)
        
    @classmethod
    def mutate(cls, root, info, id, name, adres, telefon):
        restoran=Restoran.objects.get(pk=id)
        restoran.name=name
        restoran.adres=adres
        restoran.telefon=telefon
        restoran.save()
        return RestoranEkle(restoran=restoran)

class RestoranGuncelle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        name = graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
    restoran=Field(RestoranType)

    @classmethod
    def mutate(cls, root,info,id,name, adres, telefon ):
        restoran=Restoran.objects.get(pk=id)
        restoran.name=name
        restoran.adres=adres
        restoran.telefon=telefon
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