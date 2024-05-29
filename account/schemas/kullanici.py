from graphene import Field
import graphene
from django.contrib.auth import authenticate,login
from graphene_django import DjangoObjectType
import graphql_jwt
import graphql_jwt.shortcuts
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
        telefon_no=graphene.String(required=True)
        hesap_tipi=graphene.String(required=True)
    kullanici=Field(KullaniciType)

    @classmethod
    def mutate(cls,root,info,isim,soyisim,email,sifre,telefon_no,hesap_tipi):
        kullanici=Kullanici()
        kullanici.isim=isim
        kullanici.soyisim=soyisim
        kullanici.email=email
        kullanici.sifre=sifre
        kullanici.telefon_no=telefon_no
        kullanici.hesap_tipi=hesap_tipi
        kullanici.save()
        return KullaniciEkle(kullanici=kullanici)


class KullaniciGuncelle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        isim=graphene.String()
        soyisim=graphene.String()
        email=graphene.String()
        sifre=graphene.String()
        telefon_no=graphene.String()
        hesap_tipi=graphene.String()
    kullanici=Field(KullaniciType)

    @classmethod
    def mutate(cls, root, info, id,isim,soyisim,email,sifre,telefon_no,hesap_tipi):
        kullanici=Kullanici.objects.get(pk=id)
        kullanici.isim=isim
        kullanici.soyisim=soyisim
        kullanici.email=email
        kullanici.sifre=sifre
        kullanici.telefon_no=telefon_no
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
        email = graphene.String(required=True)
        sifre = graphene.String(required=True)

    kullanici = graphene.Field(KullaniciType)
    token = graphene.String()

    @classmethod
    def mutate(cls, root, info, email, sifre):
        try:
            kullanici = Kullanici.objects.get(email=email, sifre=sifre)
        except Kullanici.DoesNotExist:
            raise Exception("Geçersiz kimlik bilgileri")

        token = graphql_jwt.shortcuts.get_token(kullanici)

        return Login(kullanici=kullanici, token=token)




from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.crypto import salted_hmac
from django.utils.http import base36_to_int, int_to_base36

class CustomTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        Parola değiştiğinde kullanıcının şifresinin güncel olduğunu kontrol etmek için kullanılır.
        """
        # Şifrenin değeri boş olabilir, bu nedenle boş olup olmadığını kontrol etmek gerekir.
        # Parola None olabilir çünkü bazı kullanıcılar parola kullanmamış olabilirler.
        # Bu nedenle, şifre yoksa 'X' ile değiştiriyoruz.
        password = getattr(user, 'password', None)
        if password is None:
            password = 'X'
        
        # Kullanıcı ID'sini, şifreyi ve timestamp'i birleştirerek bir hash değeri oluşturuyoruz.
        # Timestamp, kullanıcı şifresi değiştiğinde değişmesini sağlar.
        return '{}{}{}{}'.format(
            user.pk, password, timestamp, user.is_active
        )

custom_token_generator = CustomTokenGenerator()


class ResetPassword(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, email):
        try:
            # Kullanıcıyı e-posta adresine göre al
            user = Kullanici.objects.get(email=email)
        except Kullanici.DoesNotExist:
            # Eğer e-posta adresiyle bir kullanıcı bulunamazsa, başarısızlık döndür
            return ResetPassword(success=False)

        # Şifre sıfırlama token'ı oluştur
        token_generator = CustomTokenGenerator()
        token = token_generator.make_token(user)
        # token = default_token_generator(user)

        # Token'ı içeren sıfırlama linkini oluştur
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_link = f"https://example.com/reset-password/?uid={uid}&token={token}"

        # Sıfırlama linkini e-posta ile kullanıcıya gönder
        send_mail(
            'Şifre Sıfırlama',
            f'Lütfen şifrenizi sıfırlamak için aşağıdaki linke gidin: {reset_link}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

        # Başarılı olduğunu belirt
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

kullanici_schema=graphene.Schema(query=Query,mutation=Mutation)
