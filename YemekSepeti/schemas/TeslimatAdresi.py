from graphene import Field,ObjectType
import graphene 
from graphene_django import DjangoObjectType 
from YemekSepeti.models import TeslimatAdresi
from account.models import Kullanici

class TeslimatType(DjangoObjectType):
    class Meta:
        model = TeslimatAdresi

class Query(graphene.ObjectType):
    teslimatlar = graphene.List(TeslimatType)

    def resolve_teslimatlar(root, info):
        return TeslimatAdresi.objects.all()
    
class KullaniciInput(graphene.InputObjectType):
    isim=graphene.String(required=True)
    soyisim=graphene.String(required=True)
    email=graphene.String(required=True)
    sifre=graphene.String(required=True)
    sifre_dogrulama=graphene.String(required=True)
    hesap_tipi=graphene.String(required=True)


class TeslimatEkle(graphene.Mutation):
    class Arguments:
        il = graphene.String()
        ilce = graphene.String()
        mahalle=graphene.String()
        cadde=graphene.String()
        bina=graphene.String()
        kapi=graphene.String()
        kullanici=graphene.Int()
    Teslimat_Adresi=Field(TeslimatType)

    @classmethod
    def mutate(cls, root, info, il, ilce,mahalle,cadde,bina,kapi,kullanici):
        teslimat=TeslimatAdresi()
        teslimat.il=il
        teslimat.ilce=ilce
        teslimat.mahalle=mahalle
        teslimat.cadde=cadde
        teslimat.bina=bina
        teslimat.kapi=kapi
        teslimat.id=kullanici
        teslimat.save()
        return TeslimatEkle(teslimat=teslimat)

class TeslimatGuncelle(graphene.Mutation):
    class Arguments:
        il = graphene.String(required=True)
        ilce = graphene.String(required=True)
        mahalle=graphene.String(required=True)
        cadde=graphene.String(required=True)
        bina=graphene.String(required=True)
        kapi=graphene.String(required=True)
        kullanici=graphene.Int(required=True)

    teslimat=Field(TeslimatType)

    @classmethod
    def mutate(cls,root,info,il,ilce,mahalle,cadde,bina,kapi,kullanici):
        teslimat=TeslimatAdresi.objects.get(pk=id)
        if il is not None:
            teslimat.il=il
        if ilce is not None:
            teslimat.ilce=ilce
        if mahalle is not None:
            teslimat.mahalle=mahalle
        if cadde is not None:
            teslimat.cadde=cadde
        if bina is not None:
            teslimat.bina=bina
        if kapi is not None:
            teslimat.kapi=kapi
        if kullanici is not None:
            teslimat.id=kullanici
        teslimat.save()
        return TeslimatGuncelle(teslimat=teslimat)
        
class TeslimatSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    teslimat=Field(TeslimatType)

    @classmethod
    def mutate(cls,root,info,id):
        teslimat=TeslimatAdresi.objects.get(pk=id)
        teslimat.delete()
        return TeslimatSil(teslimat=teslimat)
    
class Mutation(graphene.ObjectType):
    teslimat_ekle = TeslimatEkle.Field()
    teslimat_guncelle=TeslimatGuncelle.Field()
    teslimat_sil=TeslimatSil.Field()

teslimat_schema = graphene.Schema(query=Query, mutation=Mutation)