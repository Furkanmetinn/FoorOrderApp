import graphene
from account.schema_account import login_schema
from schema_graphql.Musteri import musteri_schema
from schema_graphql.Restoran import restoran_schema
from schema_graphql.RestoranDetay import restoranDetay_schema
from schema_graphql.Siparis import siparis_schema 
from schema_graphql.SiparisDetay import siparisDetay_schema
from schema_graphql.Urun import urun_schema
from schema_graphql.Category import kategori_schema
from schema_graphql.TeslimatAdresi import teslimat_schema
from schema_graphql.OdemeBilgisi import odeme_schema

from graphene import Mutation


class Query(graphene.ObjectType):
    musteri=graphene.Field(musteri_schema.query)
    restoran=graphene.Field(restoran_schema.query)
    restoranDetay=graphene.Field(restoranDetay_schema.query)
    siparis=graphene.Field(siparis_schema.query)
    siparisDetay=graphene.Field(siparisDetay_schema.query)
    urun=graphene.Field(urun_schema.query)
    login=graphene.Field(login_schema.query)
    kategori=graphene.Field(kategori_schema.query)
    teslimat=graphene.Field(teslimat_schema.query)
    odeme=graphene.Field(odeme_schema.query)



class Mutation (graphene.ObjectType):
    musteri=graphene.Field(musteri_schema.mutation)
    restoran=graphene.Field(restoran_schema.mutation)
    restoranDetay=graphene.Field(restoranDetay_schema.mutation)
    siparis=graphene.Field(siparis_schema.mutation)
    siparisDetay=graphene.Field(siparisDetay_schema.mutation)
    urun=graphene.Field(urun_schema.mutation)
    login=graphene.Field(login_schema.mutation)
    kategori=graphene.Field(kategori_schema.mutation)
    teslimat=graphene.Field(teslimat_schema.mutation)
    odeme=graphene.Field(odeme_schema.query)

schema=graphene.Schema(query=Query, mutation=Mutation)