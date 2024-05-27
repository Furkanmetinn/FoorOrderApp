from django.db import models


class Kullanici(models.Model):
    isim = models.CharField(max_length=255)
    soyisim = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    sifre = models.CharField(max_length=255)
    hesap_tipi=models.CharField(max_length=20, choices=[("Kullanici","Kullanici"),("Restoran","Restoran")])
    

    def __str__(self):
        return f"{self.isim} {self.soyisim}"
