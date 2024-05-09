from graphene import Field
import graphene
from django.contrib.auth import authenticate
from graphene_django import DjangoObjectType
from account.models import Kullanici


class KullaniciType(DjangoObjectType):
    class Meta:
        model= Kullanici

    
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
        kullanici=Kullanici()
        kullanici.soyisim=soyisim
        kullanici.email=email
        kullanici.sifre=sifre
        kullanici.sifre_dogrulama=sifre_dogrulama
        kullanici.hesap_tipi=hesap_tipi
        kullanici.save()
        return KullaniciEkle(kullanici=kullanici)


class Mutation(graphene.ObjectType):
    kullanici_ekle=KullaniciEkle.Field()

class Query(graphene.ObjectType):
    login = graphene.Field(
        KullaniciType, email=graphene.String(), sifre=graphene.String()
    )
    kullanicilar = graphene.List(KullaniciType)

    def resolve_kullanicilar(self, info):
        return Kullanici.objects.all()

    def resolve_login(self, info, email, sifre, **kwargs):
        auth_user = authenticate(email=email, sifre=sifre)

        if auth_user == None:
            raise Exception("Geçersiz kimlik bilgileri")

        return Kullanici

kullanici_schema=graphene.Schema(query=Query,mutation=Mutation)
