# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User

# USUARIO....
class UserProfile(models.Model):
    SEXO_ESCOLHA = (
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
    sexo = models.CharField(max_length=1, null=False, choices=SEXO_ESCOLHA)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.ImageField(upload_to ='profile_image', blank=True)

    def __str__(self):
        return self.user.username

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
        ('Alugar', 'Alugar'),
        ('Vender', 'Vender'),
    )
    nome = models.CharField(max_length=40, null=False)
    user = models.ForeignKey(User, related_name="imovel", default=1)
    cep = models.CharField(max_length=8)
    uf = models.CharField(max_length=2, default='ZZ', null=False, choices=UF_CHOICES)
    stats = models.CharField(max_length=7, null=False, choices=STATUS_CHOICES)
    position = GeopositionField()
    profilePic = models.ImageField(upload_to ='imovel_image', blank=True)

    class Meta:
        verbose_name_plural = 'Imoveis'
        #ORDENAR POR LIKE TODO
        #ordering = ["likesImovel"]

#TODO CLASS PARA VARIAS IMAGENS ASSOCIADA AO IMOVEL(FK)
#class ImagensImovel(models.Model):
#    imovel = models.ForeignKey(Imovel,blank=True)
#    imagem = models.ImageField(upload_to ='imovel_image', blank=True, verbose_name='Imagem')

#TODO CLASS LIKE PRA ORDENAR NA LISTA IMOVEIS
#class like(models.Model):
#likes = models.ForeignKey(imovel, related_name="imovel", blank=True)