# Generated by Django 5.0.6 on 2024-05-29 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_kullanici_sifre_dogrulama'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='telefon_no',
            field=models.CharField(default='', max_length=11),
        ),
    ]
