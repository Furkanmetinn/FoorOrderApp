from django.db import models


class Kullanici(models.Model):
    isim = models.CharField(max_length=255)
    soyisim = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    sifre = models.CharField(max_length=255)
    telefon_no=models.CharField(max_length=11,default="")
    hesap_tipi=models.CharField(max_length=20, choices=[("Kullanici","Kullanici"),("Restoran","Restoran")])

    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['isim', 'soyisim']

    def __str__(self):
        return f"{self.isim} {self.soyisim}"
    

    def get_username(self):
        return self.email
    
    def get_email_field_name(self):
        return 'email'