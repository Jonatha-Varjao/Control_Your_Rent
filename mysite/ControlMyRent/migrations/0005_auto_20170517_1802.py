# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlMyRent', '0004_imagensimovel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagensimovel',
            name='imovel',
        ),
        migrations.AddField(
            model_name='imovel',
            name='imovelPic',
            field=models.ImageField(blank=True, upload_to='Imovel_image'),
        ),
        migrations.DeleteModel(
            name='ImagensImovel',
        ),
    ]