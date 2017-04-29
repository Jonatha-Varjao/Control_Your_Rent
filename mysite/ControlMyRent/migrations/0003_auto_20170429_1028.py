# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-29 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlMyRent', '0002_imovel_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='imovel',
            name='stats',
            field=models.IntegerField(choices=[(0, 'Alugar'), (0, 'Alugado'), (1, 'Vender'), (11, 'Vendido')], default=0),
        ),
    ]