# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse


# Create your models here.

# USUÁRIO....
class UserProfile(models.Model):
    SEXO_CHOICES = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
    )
    UF_CHOICES = (
        (u'AC', u'Acre'),
        (u'AL', u'Alagoas'),
        (u'AP', u'Amapá'),
        (u'AM', u'Amazonas'),
        (u'BA', u'Bahia'),
        (u'CE', u'Ceará'),
        (u'DF', u'Distrito Federal'),
        (u'ES', u'Espirito Santo'),
        (u'GO', u'Goiás'),
        (u'MA', u'Maranhão'),
        (u'MT', u'Mato Grosso'),
        (u'MS', u'Mato Grosso do Sul'),
        (u'MG', u'Minas Gerais'),
        (u'PA', u'Pará'),
        (u'PB', u'Paraíba'),
        (u'PR', u'Paraná'),
        (u'PE', u'Pernambuco'),
        (u'PI', u'Piauí'),
        (u'RJ', u'Rio de Janeiro'),
        (u'RN', u'Rio Grande do Norte'),
        (u'RS', u'Rio Grande do Sul'),
        (u'RO', u'Rondônia'),
        (u'RR', u'Roraima'),
        (u'SC', u'Santa Catarina'),
        (u'SP', u'São Paulo'),
        (u'SE', u'Sergipe'),
        (u'TO', u'Tocantins'),
    )
    uf_user = models.CharField(max_length=2, default='ZZ', choices=UF_CHOICES)
    cpf = models.CharField(max_length=11, null=False)
    data_de_nascimento = models.DateField(null=False)
    sexo = models.CharField(max_length=1, null=False, choices=SEXO_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # userProfilePic


class Imovel(models.Model):
    UF_CHOICES = (
        (u'AC', u'Acre'),
        (u'AL', u'Alagoas'),
        (u'AP', u'Amapá'),
        (u'AM', u'Amazonas'),
        (u'BA', u'Bahia'),
        (u'CE', u'Ceará'),
        (u'DF', u'Distrito Federal'),
        (u'ES', u'Espirito Santo'),
        (u'GO', u'Goiás'),
        (u'MA', u'Maranhão'),
        (u'MT', u'Mato Grosso'),
        (u'MS', u'Mato Grosso do Sul'),
        (u'MG', u'Minas Gerais'),
        (u'PA', u'Pará'),
        (u'PB', u'Paraíba'),
        (u'PR', u'Paraná'),
        (u'PE', u'Pernambuco'),
        (u'PI', u'Piauí'),
        (u'RJ', u'Rio de Janeiro'),
        (u'RN', u'Rio Grande do Norte'),
        (u'RS', u'Rio Grande do Sul'),
        (u'RO', u'Rondônia'),
        (u'RR', u'Roraima'),
        (u'SC', u'Santa Catarina'),
        (u'SP', u'São Paulo'),
        (u'SE', u'Sergipe'),
        (u'TO', u'Tocantins'),
    )
    STATUS_CHOICES = (
        ('alugar', 'Alugar'),
        ('vender', 'Vender'),
    )

    nome = models.CharField(max_length=40, null=False)
    user = models.ForeignKey(User, related_name="imovel", default=1)
    cep = models.CharField(max_length=8)
    uf = models.CharField(max_length=2, default='ZZ',
                          null=False, choices=UF_CHOICES)
    stats = models.CharField(max_length=7, default='NO',
                             null=False, choices=STATUS_CHOICES)
    # TODO googleMaps API
    latitude = models.FloatField(max_length=15, default=0)
    longitude = models.FloatField(max_length=15, default=0)

    def get_absolute_url(self):
        return reverse('Rent:Imovel',
                       args=[self.imovel.year,
                             self.imovel.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])                        
