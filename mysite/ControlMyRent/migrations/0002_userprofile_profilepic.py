# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlMyRent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(default='img/default/nophotouser.png', upload_to='img/'),
        ),
    ]
