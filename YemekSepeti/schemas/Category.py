from graphene import Field
import graphene
from graphene_django import DjangoObjectType
from YemekSepeti.models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category

class Query(graphene.ObjectType):
    kategoriler=graphene.List(CategoryType)
    def resolve_kategoriler(root,info):
        print("_______________")
        return Category.objects.all()
    
    
    
class KategoriEkle(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
    kategori=Field(CategoryType)

    @classmethod
    def mutate(cls,root,info,id,name):
        kategori=Category()
        kategori.name=name
        kategori.save()
        return KategoriEkle(kategori=kategori)
    
class KategoriGuncelle(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
    kategori=Field(CategoryType)

    @classmethod
    def mutate(cls,root,info,id,name):
        kategori=Category.objects.get(pk=id)
        kategori.name=name
        kategori.save()
        return KategoriGuncelle(kategori=kategori)
    
class KategorSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    kategori=Field(CategoryType)

    @classmethod
    def mutate(cls,root,info,id):
        kategori=Category.objects.get(pk=id)
        return KategorSil(kategori=kategori)
    
class Mutation(graphene.ObjectType):
    kategori_ekle=KategoriEkle.Field()
    kategori_guncelle=KategoriGuncelle.Field()
    kategori_sil=KategorSil.Field()

kategori_schema=graphene.Schema(query=Query,mutation=Mutation)