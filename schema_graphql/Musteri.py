from graphene import Field,ObjectType
import graphene 
from graphene_django import DjangoObjectType 
from YemekSepeti.models import Musteri

class MusteriType(DjangoObjectType):
    class Meta:
        model = Musteri
        fields=["id"]

class Query(graphene.ObjectType):
    musteriler = graphene.List(MusteriType)
    musteriler_id=graphene.Field(MusteriType, id=graphene.String())

    def resolve_musteriler(root, info):
        return Musteri.objects.all()
    
    def resolve_musteriler_id(root,info, id):
        return Musteri.objects.get(pk=id)


class MusteriEkle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        name = graphene.String(required=True)
        surname = graphene.String(required=True)
        email=graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
    musteri=Field(MusteriType)

    @classmethod
    def mutate(cls, root, info, id, name, surname,adres,email, telefon):
        musteri=Musteri.objects.get(pk=id)
        musteri.name=name
        musteri.surname=surname
        musteri.adres=adres
        musteri.email=email
        musteri.telefon=telefon
        musteri.save()
        return MusteriEkle(musteri=musteri)

class MusteriGuncelle(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        name = graphene.String(required=True)
        surname = graphene.String(required=True)
        email=graphene.String(required=True)
        adres=graphene.String(required=True)
        telefon=graphene.String(required=True)
    musteri=Field(MusteriType)

    @classmethod
    def mutate(cls,root,info,id, name, surname, adres, email, telefon):
        musteri=Musteri.objects.get(pk=id)
        musteri.name=name
        musteri.surname=surname
        musteri.adres=adres
        musteri.email=email
        musteri.telefon=telefon
        musteri.save()
        return MusteriGuncelle(musteri=musteri)
        
class MusteriSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    musteri=Field(MusteriType)

    @classmethod
    def mutate(cls,root,info,id):
        musteri=Musteri.objects.get(pk=id)
        return MusteriSil(musteri=musteri)
    
class Mutation(graphene.ObjectType):
    musteri_ekle = MusteriEkle.Field()
    musteri_guncelle=MusteriGuncelle.Field()
    musteri_sil=MusteriSil.Field()

musteri_schema = graphene.Schema(query=Query, mutation=Mutation)