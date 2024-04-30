import graphene
from graphene_django import DjangoObjectType
import jwt
from .models import Kullanici

class KullaniciTipi(DjangoObjectType):
    class Meta:
        model = Kullanici

class GirisMutasyonu(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        parola = graphene.String(required=True)

    class Meta:
        description = "Kullanıcıyı giriş yapma"

    token = graphene.String()

    @classmethod
    def mutate(self, info, email, parola):
        try:
            kullanici = Kullanici.objects.get(email=email)
        except Kullanici.DoesNotExist:
            raise Exception("Kullanıcı Bulunamadı")

        if not kullanici.check_password(parola):
            raise Exception("Yanlış Parola")

        token = jwt.encode({'user_id': kullanici.id}, 'secret', algorithm='HS256')
        return GirisMutasyonu(token=token)

login_schema = graphene.Schema(query=KullaniciTipi, mutation=GirisMutasyonu)
