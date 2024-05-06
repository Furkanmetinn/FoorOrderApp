from graphene import Field,ObjectType
import graphene 
from graphene_django import DjangoObjectType 
from YemekSepeti.models import TeslimatAdresi

class TeslimatType(DjangoObjectType):
    class Meta:
        model = TeslimatAdresi
        fields=["id"]

class Query(graphene.ObjectType):
    teslimatlar = graphene.List(TeslimatType)
    teslimatlar_id=graphene.Field(TeslimatType, id=graphene.String())

    def resolve_teslimatlar(root, info):
        return TeslimatAdresi.objects.all()
    
    def resolve_teslimatlar_id(root,info, id):
        return TeslimatAdresi.objects.get(pk=id)


class TeslimatEkle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        il = graphene.String(required=True)
        ilce = graphene.String(required=True)
        mahalle=graphene.String(required=True)
        cadde=graphene.String(required=True)
        bina=graphene.String(required=True)
        kapi=graphene.String(required=True)
        musteri=graphene.String(required=True)
    Teslimat_Adresi=Field(TeslimatType)

    @classmethod
    def mutate(cls, root, info, id, il, ilce,mahalle,cadde,bina,kapi,musteri):
        teslimat=TeslimatAdresi.objects.get(pk=id)
        teslimat.il=il
        teslimat.ilce=ilce
        teslimat.mahalle=mahalle
        teslimat.cadde=cadde
        teslimat.bina=bina
        teslimat.kapi=kapi
        teslimat.musteri=musteri
        teslimat.save()
        return TeslimatEkle(teslimat=teslimat)

class TeslimatGuncelle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        il = graphene.String(required=True)
        ilce = graphene.String(required=True)
        mahalle=graphene.String(required=True)
        cadde=graphene.String(required=True)
        bina=graphene.String(required=True)
        kapi=graphene.String(required=True)
        musteri=graphene.String(required=True)


    teslimat=Field(TeslimatType)

    @classmethod
    def mutate(cls,root,info,id,il,ilce,mahalle,cadde,bina,kapi,musteri):
        teslimat=TeslimatAdresi.objects.get(pk=id)
        teslimat.il=il
        teslimat.ilce=ilce
        teslimat.mahalle=mahalle
        teslimat.cadde=cadde
        teslimat.bina=bina
        teslimat.kapi=kapi
        teslimat.musteri=musteri
        teslimat.save()
        return TeslimatGuncelle(teslimat=teslimat)
        
class TeslimatSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    teslimat=Field(TeslimatType)

    @classmethod
    def mutate(cls,root,info,id):
        teslimat=TeslimatAdresi.objects.get(pk=id)
        return TeslimatSil(teslimat=teslimat)
    
class Mutation(graphene.ObjectType):
    teslimat_ekle = TeslimatEkle.Field()
    teslimat_guncelle=TeslimatGuncelle.Field()
    teslimat_sil=TeslimatSil.Field()

teslimat_schema = graphene.Schema(query=Query, mutation=Mutation)