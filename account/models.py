from django.db import models

class Kullanici(models.Model):
    isim = models.CharField(max_length=255)
    soyisim = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    parola = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.isim} {self.soyisim}"