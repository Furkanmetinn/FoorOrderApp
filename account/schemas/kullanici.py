from graphene import Field
import graphene
from django.contrib.auth import authenticate,login
from graphene_django import DjangoObjectType
import graphql_jwt
from YemekSepeti.models import Restoran
from YemekSepeti.schemas.Restoran import RestoranType
from account.models import Kullanici
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User
from django.core.mail import send_mail



class KullaniciType(DjangoObjectType):
    class Meta:
        model= Kullanici

class Query(graphene.ObjectType):
    kullanicilar = graphene.List(KullaniciType)

    def resolve_kullanicilar(root, info):
        return Kullanici.objects.all()
    
    
class KullaniciEkle(graphene.Mutation):
    class Arguments:
        isim=graphene.String(required=True)
        soyisim=graphene.String(required=True)
        email=graphene.String(required=True)
        sifre=graphene.String(required=True)
        hesap_tipi=graphene.String(required=True)
    kullanici=Field(KullaniciType)

    @classmethod
    def mutate(cls,root,info,isim,soyisim,email,sifre, hesap_tipi):
        kullanici=Kullanici()
        kullanici.isim=isim
        kullanici.soyisim=soyisim
        kullanici.email=email
        kullanici.sifre=sifre
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
        hesap_tipi=graphene.String(required=True)
    kullanici=Field(KullaniciType)

    @classmethod
    def mutate(cls, root, info, id,isim,soyisim,email,sifre,hesap_tipi):
        kullanici=Kullanici.objects.get(pk=id)
        kullanici.isim=isim
        kullanici.soyisim=soyisim
        kullanici.email=email
        kullanici.sifre=sifre
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
        kullanici.delete()
        return KullaniciSil(kullanici=kullanici)

class Login(graphene.Mutation):
    class Arguments:
        email=graphene.String(required=True)
        sifre=graphene.String(required=True)
    kullanici=graphene.Field(KullaniciType)
    
    @classmethod
    def mutate(cls, root, info, email,sifre):
        
        try:
            kullanici = Kullanici.objects.get(email=email,sifre=sifre)
        except:
            raise Exception("geçersiz kimlik bilgileri")
            
        
        return Login(kullanici=kullanici)

    
class ResetPassword(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return ResetPassword(success=False)

        token_generator = PasswordResetTokenGenerator()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

        # E-posta gönderme işlemi
        send_mail(
            'Şifre Sıfırlama',
            f'Merhaba {user.username}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

        return ResetPassword(success=True)
    
    

class GetKullanici(graphene.Mutation):
    class Arguments:
        email=graphene.String(required=True)
    kullanici=Field(KullaniciType)

    @classmethod
    def mutate(cls, root, info, email):
        kullanici=Kullanici.objects.get(email=email)
        return GetKullanici(kullanici=kullanici)
    
class GetRestoran(graphene.Mutation):
    class Arguments:
        email=graphene.String(required=True)
    restoran=Field(RestoranType)

    @classmethod
    def mutate(cls,root,info,email):
        restoran=Restoran.objects.get(email=email)
        return GetRestoran(restoran=restoran)
    
class Mutation(graphene.ObjectType):
    kullanici_ekle=KullaniciEkle.Field()
    kullanici_guncelle=KullaniciGuncelle.Field()
    kullanici_sil=KullaniciSil.Field()
    login=Login.Field()
    reset_password = ResetPassword.Field()
    get_kullanici = GetKullanici.Field()
    get_restoran=GetRestoran.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

kullanici_schema=graphene.Schema(query=Query,mutation=Mutation)
