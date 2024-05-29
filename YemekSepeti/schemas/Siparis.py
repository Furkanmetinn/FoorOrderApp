from graphene import Field
import graphene 
from graphene_django import DjangoObjectType 
from YemekSepeti.models import Siparis, SiparisItem

class SiparisType(DjangoObjectType):
    toplam_tutar=graphene.Float()
    class Meta:
        model = Siparis

    def resolve_toplam_tutar(self,info):
        return self.toplam_tutar
class Query(graphene.ObjectType):
    siparisler = graphene.List(SiparisType)

    def resolve_siparisler(root, info):
        return Siparis.objects.all()

class SiparisItemInput(graphene.InputObjectType):
    siparis_tarihi=graphene.DateTime(required=True)
    teslim_tarihi=graphene.DateTime(required=True)
    tutar=graphene.Float(required=True)
    durum=graphene.String(required=True)
    urun=graphene.Int(required=True)
    miktar=graphene.Int(required=True)

class SiparisEkle(graphene.Mutation):
    class Arguments:
        siparis_items = graphene.List(SiparisItemInput)
    siparis=Field(SiparisType)

    @classmethod
    def mutate(cls, root, info,siparis_items):
        siparis=Siparis()
        siparis.save()

        for item in siparis_items:
            siparis_item =SiparisItem(siparis=siparis)
            siparis_item.siparis_tarihi=item.siparis_tarihi
            siparis_item.teslim_tarihi=item.teslim_tarihi
            siparis_item.tutar=item.tutar
            siparis_item.durum=item.durum
            siparis_item.miktar=item.miktar
            siparis_item.urun_id=item.urun
            siparis_item.save()
        
        return SiparisEkle(siparis=siparis)

class SiparisGuncelle(graphene.Mutation):
    class Arguments:
        siparis_items = graphene.List(SiparisItemInput)
    siparis=Field(SiparisType)

    def mutate(cls, root, info,siparis_items):
        siparis=Siparis.objects.get(pk=id)
        siparis.save()

        for item in siparis_items:
            siparis_item =SiparisItem(siparis=siparis)
            siparis_item.siparis_tarihi=item.siparis_tarihi
            siparis_item.teslim_tarihi=item.teslim_tarihi
            siparis_item.tutar=item.tutar
            siparis_item.durum=item.durum
            siparis_item.miktar=item.miktar
            siparis_item.urun_id=item.urun
            siparis_item.save()
        
        return SiparisEkle(siparis=siparis)


class SiparisSil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    siparis=Field(SiparisType)

    @classmethod
    def mutate(cls,root,info,id):
        siparis=Siparis.objects.get(pk=id)
        siparis.delete()
        return SiparisSil(siparis=siparis)

class Mutation(graphene.ObjectType):
    siparis_ekle=SiparisEkle.Field()
    siparis_guncelle=SiparisGuncelle.Field()
    siparis_sil=SiparisSil.Field()       



siparis_schema = graphene.Schema(query=Query, mutation=Mutation)