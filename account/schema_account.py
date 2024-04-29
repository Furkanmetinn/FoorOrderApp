import graphene
from graphene_django import DjangoObjectType
from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    user_by_id = graphene.Field(UserType, id=graphene.Int())
    user_by_username = graphene.Field(UserType, username=graphene.String())

    def resolve_user_by_id(self, info, id):
        return User.objects.get(id=id)

    def resolve_user_by_username(self, info, username):
        return User.objects.get(username=username)

class Mutation(graphene.ObjectType):
    register_user = graphene.Field(graphene.String, username=graphene.String(), email=graphene.String(), password=graphene.String())
    login_user = graphene.Field(graphene.String, username=graphene.String(), password=graphene.String())

    def resolve_register_user(self, info, username, email, password):
        new_user = User(username=username, email=email, password=password)
        new_user.save()
        return "New user registered successfully!"

    def resolve_login_user(self, info, username, password):
        try:
            user = User.objects.get(username=username, password=password)
            return f"Login successful for {user.username}!"
        except User.DoesNotExist:
            return "Invalid username or password."

login_schema = graphene.Schema(query=Query, mutation=Mutation)
