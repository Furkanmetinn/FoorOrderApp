import graphene
from graphene_django import DjangoObjectType
from .models import User
from django.contrib.auth import authenticate

class UserNode(DjangoObjectType):
    class Meta:
        model = User

class Mutation(graphene.ObjectType):
    login = graphene.Field(graphene.String, username=graphene.String(required=True), password=graphene.String(required=True))

    @graphene.resolve_login
    def resolve_login(self, info, username, password):
        user = authenticate(username=username, password=password)
        if user:
            token = authenticate(username=username, password=password)
            return token
        else:
            raise Exception('Geçersiz kimlik bilgileri')
