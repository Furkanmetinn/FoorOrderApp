from graphene import Field,ObjectType
import graphene 
from graphene_django import DjangoObjectType 
from YemekSepeti.models import OdemeBilgileri

class OdemeType(DjangoObjectType):
    class Meta:
        model = OdemeBilgileri
        

class Query(graphene.ObjectType):
    odemeler = graphene.List(OdemeType)

    def resolve_odemeler(root, info):
        return OdemeBilgileri.objects.all()
    

class OdemeEkle(graphene.Mutation):
    class Arguments:
        kart_sahibi = graphene.String(required=True)
        kart_numarasi = graphene.String(required=True)
        son_kullanma=graphene.String(required=True)
        cvv=graphene.String(required=True)

    Odeme_Bilgileri=Field(OdemeType)

    @classmethod
    def mutate(cls, root, info, id,kart_sahibi,kart_numarasi,son_kullanma,cvv):
        odeme=OdemeBilgileri()
        odeme.kart_sahibi=kart_sahibi
        odeme.kart_numarasi=kart_numarasi
        odeme.son_kullanma=son_kullanma
        odeme.cvv=cvv
        odeme.save()
        return OdemeEkle(odeme=odeme)

class OdemeGuncelle(graphene.Mutation):
    class Arguments:
        kart_sahibi = graphene.String(required=True)
        kart_numarasi = graphene.String(required=True)
        son_kullanma=graphene.String(required=True)
        cvv=graphene.String(required=True)
        


    odeme=Field(OdemeType)

    @classmethod
    def mutate(cls,root,info,kart_sahibi,kart_numarasi,son_kullanma,cvv):
        odeme=OdemeBilgileri.objects.get(pk=id)
        odeme.kart_sahibi=kart_sahibi
        odeme.kart_numarasi=kart_numarasi
        odeme.son_kullanma=son_kullanma
        odeme.cvv=cvv
        odeme.save()
        return OdemeGuncelle(odeme=odeme)
        
class OdemeSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    odeme=Field(OdemeType)

    @classmethod
    def mutate(cls,root,info,id):
        odeme=OdemeBilgileri.objects.get(pk=id)
        odeme.delete()
        return OdemeSil(odeme=odeme)
    
class Mutation(graphene.ObjectType):
    odeme_ekle = OdemeEkle.Field()
    odeme_guncelle=OdemeGuncelle.Field()
    odeme_sil=OdemeSil.Field()

odeme_schema = graphene.Schema(query=Query, mutation=Mutation)