from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    urun = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):  
        return self.name


class Musteri(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=100)
    email=models.EmailField()
    telefon = models.CharField(max_length=11)
    adres = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Restoran(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    adres = models.CharField(max_length=255)
    telefon = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class RestoranDetay(models.Model):
    restoran_name = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    telefon = models.CharField(max_length=10)
    acilis_saati = models.TimeField()
    kapanis_saati = models.TimeField()
    puan = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    resim = models.ImageField()


    def __str__(self):
        return self.restoran_name

class Urun(models.Model):
    urun_id=models.IntegerField()
    name = models.CharField(max_length=100)
    image=models.ImageField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    # category = models.CharField(max_length=50)
    # restaurant = models.ForeignKey(Restoran, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Siparis(models.Model):
    sip_id=models.IntegerField()
    mus_id = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    siparis_tarihi = models.DateTimeField(auto_now_add=True)
    teslim_tarihi = models.DateField()
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    durum = models.CharField(max_length=20, choices=[("Bekliyor", "Bekliyor"), ("Onaylandı", "Onaylandı"), ("Tamamlandı", "Tamamlandı"), ("İptal Edildi", "İptal Edildi")])

    def __str__(self):
        return self.sip_id
    
class SiparisDetay(models.Model):
    siparis = models.ForeignKey(Siparis, on_delete=models.CASCADE, related_name='siparis_detaylari')
    urun = models.ForeignKey('Urun', on_delete=models.CASCADE)
    miktar = models.PositiveIntegerField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    toplam_tutar = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.siparis} - {self.urun}"