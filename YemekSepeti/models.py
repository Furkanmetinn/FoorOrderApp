from django.db import models
from django.contrib.auth.models import User

from account.models import Kullanici


class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):  
        return self.name
class Restoran(models.Model):
    name = models.CharField(max_length=100)
    adres = models.CharField(max_length=255)
    telefon = models.CharField(max_length=15)
    acilisSaati = models.TimeField()
    kapanis_saati = models.TimeField()
    email=models.EmailField(blank=True)
    puan = models.FloatField(())
    resim = models.ImageField()
    min_tutar=models.FloatField(())
    category=models.CharField(max_length=20)
    

    def __str__(self):
        return self.name

class Urun(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField()
    fiyat = models.FloatField()
    detay = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    restoran = models.ForeignKey(Restoran, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.name
    

class Siparis(models.Model):
    siparis_tarihi = models.DateTimeField(auto_now_add=True)
    teslim_tarihi = models.DateField()
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    durum = models.CharField(max_length=20, choices=[("Bekliyor", "Bekliyor"), ("Onaylandı", "Onaylandı"), ("Tamamlandı", "Tamamlandı"), ("İptal Edildi", "İptal Edildi")])

    def __str__(self):
        return self.sip_id
    
class SiparisDetay(models.Model):
    miktar = models.PositiveIntegerField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    toplam_tutar = models.DecimalField(max_digits=10, decimal_places=2)
    siparis = models.ForeignKey(Siparis, on_delete=models.CASCADE, related_name='siparis_detaylari')
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.siparis} - {self.urun}"

class TeslimatAdresi(models.Model):
    il=models.CharField(max_length=50)
    ilce=models.CharField(max_length=50)
    mahalle=models.CharField(max_length=50)
    cadde=models.CharField(max_length=50)
    bina=models.CharField(max_length=50)
    kapi=models.CharField(max_length=50)
    kullanici=models.ForeignKey(Kullanici,on_delete=models.CASCADE)

    def __str__(self):
        return self.il


class OdemeBilgileri(models.Model):
    kart_sahibi=models.CharField(max_length=100)
    kart_numarasi=models.IntegerField()
    son_kullanma=models.IntegerField()
    cvv=models.IntegerField()

    def __str__(self):
        return self.kart_sahibi




    
    
