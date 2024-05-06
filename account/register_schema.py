from graphene import Field
import graphene
from graphene_django import DjangoObjectType
from account.models import Kullanici

class KullaniciType(DjangoObjectType):
    class Meta:
        model= Kullanici
        fields= '__all__'

class Query(graphene.ObjectType):
    kullanicilar=graphene.List(KullaniciType)

    def resolve_kullanicilar(root,info):
        return Kullanici.objects.all()
    
class KullaniciEkle(graphene.Mutation):
    class Arguments:
        isim=graphene.String(required=True)
        soyisim=graphene.String(required=True)
        email=graphene.String(required=True)
        sifre=graphene.String(required=True)
        sifre_dogrulama=graphene.String(required=True)
        hesap_tipi=graphene.String(required=True)
    kullanici=Field(KullaniciType)

    @classmethod
    def mutate(cls,root,info,isim,soyisim,email,sifre,sifre_dogrulama, hesap_tipi):
        kullanici=Kullanici.objects.get(pk=isim)
        kullanici.soyisim=soyisim
        kullanici.email=email
        kullanici.sifre=sifre
        kullanici.sifre_dogrulama=sifre_dogrulama
        kullanici.hesap_tipi=hesap_tipi
        kullanici.save()
        return KullaniciEkle(kullanici=kullanici)
    
class Mutation(graphene.ObjectType):
    kullanici_ekle=KullaniciEkle.Field()

kullanici_schema=graphene.Schema(query=Query,mutation=Mutation)
