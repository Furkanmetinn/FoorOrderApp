from django.db import models
from django.db import models

class Kullanici(models.Model):
    isim = models.CharField(max_length=255)
    soyisim = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True)
    sifre = models.CharField(max_length=255)
    sifre_dogrulama=models.CharField(max_length=20)
    hesap_tipi=models.CharField(max_length=20, choices=[("Kullanici","Kullanici"),("Restoran","Restoran")])

    def __str__(self):
        return f"{self.isim} {self.soyisim}"
    
