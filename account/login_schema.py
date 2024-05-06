# from graphql_jwt.decorators import jwt_required
from graphql_jwt.utils import jwt_payload, jwt_encode
from graphene_django import DjangoObjectType
from django.contrib.auth import authenticate
from .models import Kullanici
from account.models import GirisYap
import graphene

class GirisYapType(DjangoObjectType):
    class Meta:
        model = GirisYap
        fields = '__all__'

class GirisYapMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        sifre = graphene.String(required=True)

    token = graphene.String()
    giris = graphene.Field(GirisYapType)

    # @jwt_required
    def mutate(self, root, info, email, sifre):
        giris = authenticate(email=email, sifre=sifre)

        if giris:
            payload = jwt_payload(giris)
            token = jwt_encode(payload)
            return GirisYapMutation(token=token, giris=GirisYapType(giris))
        else:
            raise Exception("E-posta veya şifre hatalı")

class Mutation(graphene.ObjectType):
    giris_yap = GirisYapMutation.Field()

login_schema=graphene.Schema(mutation=Mutation)
