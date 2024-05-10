from graphene import Field
import graphene
from django.contrib.auth import authenticate
from graphene_django import DjangoObjectType
from account.models import Kullanici
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


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
        kullanici.isim=isim
        kullanici.soyisim=soyisim
        kullanici.email=email
        kullanici.sifre=sifre
        kullanici.sifre_dogrulama=sifre_dogrulama
        kullanici.hesap_tipi=hesap_tipi
        kullanici.save()
        return KullaniciEkle(kullanici=kullanici)


class KullaniciGuncelle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        isim=graphene.String(required=True)
        soyisim=graphene.String(required=True)
        email=graphene.String(required=True)
        sifre=graphene.String(required=True)
        sifre_dogrulama=graphene.String(required=True)
        hesap_tipi=graphene.String(required=True)
    kullanici=Field(KullaniciType)

    @classmethod
    def mutate(cls, root, info, id,isim,soyisim,email,sifre,sifre_dogrulama,hesap_tipi):
        kullanici=Kullanici.objects.get(pk=id)
        kullanici.isim=isim
        kullanici.soyisim=soyisim
        kullanici.email=email
        kullanici.sifre=sifre
        kullanici.sifre_dogrulama=sifre_dogrulama
        kullanici.hesap_tipi=hesap_tipi
        kullanici.save()
        return KullaniciGuncelle(kullanici=kullanici)
    
class KullaniciSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    kullanici=Field(KullaniciType)

    @classmethod
    def mutate(cls,root,info,id):
        kullanici=Kullanici.objects.get(pk=id)
        return KullaniciSil(kullanici=kullanici)

class Login(graphene.Mutation):
    class Arguments:
        email=graphene.String(required=True)
        sifre=graphene.String(required=True)
    login=Field(KullaniciType)

    def resolve_login(self, info, email, sifre, **kwargs):
        auth_user = authenticate(email=email, sifre=sifre)

        if auth_user == None:
            raise Exception("Geçersiz kimlik bilgileri")

        return Kullanici
    
    @classmethod
    def mutate(cls, root, info, email,sifre):
        login=Login()
        login.email=email
        login.sifre=sifre
        login.save()
        return Login(login=login)
    
class ResetPassword(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, email):
        user_model = Kullanici()
        try:
            user = user_model.objects.get(email=email)
        except user_model.DoesNotExist:
            return ResetPassword(success=False)

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)

        return ResetPassword(success=True)

class Mutation(graphene.ObjectType):
    kullanici_ekle=KullaniciEkle.Field()
    kullanici_guncelle=KullaniciGuncelle.Field()
    kullanici_sil=KullaniciSil.Field()
    login=Login.Field()
    reset_password = ResetPassword.Field()

kullanici_schema=graphene.Schema(mutation=Mutation)
