from .schemas.Category import kategori_schema as category_schema
from .schemas.OdemeBilgileri import odeme_schema as odeme_bilgileri_schema
from .schemas.Restoran import restoran_schema as restoran_schema
from .schemas.RestoranDetay import restoranDetay_schema as restoran_detay_schema
from .schemas.Siparis import siparis_schema as siparis_schema
from .schemas.SiparisDetay import siparisDetay_schema as siparis_detay_schema
from .schemas.TeslimatAdresi import teslimat_schema as teslimat_schema
from .schemas.Urun import urun_schema as urun_schema

import graphene

class Query(
            category_schema.Query,
            odeme_bilgileri_schema.Query,
            restoran_schema.Query,
            restoran_detay_schema.Query,
            siparis_schema.Query,
            siparis_detay_schema.Query,
            teslimat_schema.Query,
            urun_schema.Query,
            graphene.ObjectType
            ):
    pass

class Mutation(
            category_schema.Mutation,
            odeme_bilgileri_schema.Mutation,
            restoran_schema.Mutation,
            restoran_detay_schema.Mutation,
            siparis_schema.Mutation,
            siparis_detay_schema.Mutation,
            teslimat_schema.Mutation,
            urun_schema.Mutation,
            graphene.ObjectType
            ):
    pass

schema=graphene.Schema(query=Query, mutation=Mutation)