# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView, DeleteView
from .forms import *
from .models import *

# INDEX PAGE


def index(request):
    return render(request, 'Dashboard/landing.html')

# LAND PAGE


def landingPage(request):
    ImovelCount = Imovel.objects.count()
    return render(request, 'Dashboard/landing.html',{'imovelcount':ImovelCount})

# REGISTER IMOVEL PAGE


def ImovelRegister(request):
    registered = False
    if request.method == 'POST':
        form = ImovelUserForm(data=request.POST)
        if form.is_valid():
            new_imovel = form.save(commit=False)
            new_imovel.user = request.user
            new_imovel.save()
            registered = True
            # DEU CERTO
        else:
            print form.errors
    else:
        form = ImovelUserForm()
    return render(request,
                  'Dashboard/forms.html',
                  {'form': form,
                   'registered': registered})


# REGISTER USER PAGE
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            # SALVA A SENHA
            new_user.set_password(user_form.cleaned_data['password'])
            # SALVO O OBJETO USER
            new_user.save()
            # SALVO O OBJETO USERPROFILE
            new_user_profile = profile_form.save(commit=False)
            # USERPROFILE = USER
            new_user_profile.user = new_user
            if 'picture' in request.FILES:
                new_user_profile.picture = request.FILES['picture']
            new_user_profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request,
                  'Registration/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
# TROCAR SENHA


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Sua senha foi Atualizada !')
            return redirect('Rent:change_password')
        else:
            messages.error(request, 'Corrija o erro abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Registration/change_password.html', {
        'form': form
    })


# LOGUIN PAGE
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            user = authenticate(
                username=cleanedData['username'], password=cleanedData['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # PASSA A VIEW DASHBOARD=
                    ImovelCount = Imovel.objects.count()
                    img = UserProfile.objects.get(pk=id)
                    return render(request, 'Dashboard/landing.html',{'imovelcount':ImovelCount,
                                                                    'userprofile':img})
                else:
                    # PASSA A VIEW ERRO/CONTA DESATIVADA
                    return HttpResponse('Conta Desativada')
            else:
                # LOGUIN INVALIDO -> FUNÇÃO JS
                return HttpResponse('Senha Incorreta')
    else:
        form = LoginForm()
    return render(request, 'Registration/login.html', {'form': form})

# LOGOUT PAGE


def user_logout(request):
    logout(request)
    messages.success(request, 'Deslogado com Sucesso')
    return HttpResponseRedirect(reverse('index'))


# LISTAR OS IMOVEIS VIEW
class ImovelListView(ListView):
    model = Imovel
    template_name = 'Dashboard/listarimoveis.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ImovelListView, self).get_context_data(**kwargs)
        return context

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        return self.request.GET.get('paginate_by', self.paginate_by)

# DETAIL VIEW


class ImovelDetailView(DetailView):
    model = Imovel
    template_name = 'Dashboard/Imovel/detail.html'


class ImovelNoEditView(DetailView):
    model = Imovel
    template_name = 'Dashboard/Imovel/detailnoedit.html'

# PERFIL PAGE


def perfil(request):
    return render(request, 'Dashboard/Perfil/landing.html')

# EDITAR PERFIL


class perfilUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'Dashboard/Perfil/edit.html'
    success_url = reverse_lazy('Rent:landing')


class perfilProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['uf_user', 'cpf', 'sexo', 'data_de_nascimento','profilePic']
    template_name = 'Dashboard/Perfil/edituser.html'
    success_url = reverse_lazy('Rent:landing')


# DETAIL PERFIL
class perfilDetailView(DetailView):
    model = UserProfile
    template_name = 'Dashboard/Perfil/landing.html'

# VIEW PRA DELETAR IMOVEIS


class ImovelDeleteView(DeleteView):
    model = Imovel
    template_name = 'Dashboard/Imovel/delet.html'
    success_url = reverse_lazy('Rent:landing')


# VIEW PARA UPDATE IMOVEIS
class ImovelUpdateView(UpdateView):
    model = Imovel
    template_name = 'Dashboard/Imovel/edit.html'
    form_class = ImovelUserForm
    success_url = reverse_lazy('Rent:landing')

# VIEWTESTE PARA GRAFICOS


def graficos(request):
    return render(request, 'Dashboard/graficos.html')
