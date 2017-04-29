# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout



from django.urls import reverse
from django.views.generic import DetailView
from .forms import *
from .models import *


# INDEX PAGE


def index(request):
    return render(request, 'Dashboard/landing.html')

def landingPage(request):
    return render(request, 'Dashboard/landing.html')

#REGISTER IMOVEL PAGE

def ImovelRegister(request):
    registered = False
    if request.method == 'POST':
        form = ImovelUserForm(data=request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_imovel = form.save(commit=False)
            new_imovel.user = request.user
            new_imovel.save()
            registered = True
            #DEU CERTO
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
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # save the userprofile
            new_user_profile = profile_form.save(commit=False)
            # set the userprofile = user
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
                    # PASSA A VIEW DASHBOARD
                    return render(request, 'Dashboard/landing.html')
                else:
                    # PASSA A VIEW ERRO/CONTA DESATIVADA
                    return HttpResponse('Conta Desativada')
            else:
                # LOGUIN INVALIDO -> FUNÇÃO JS
                return HttpResponse('Senha Incorreta')
    else:
        form = LoginForm()
    return render(request, 'Registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#LIST VIEW 
def imovel_list(request):
    return None


# DETAIL VIEW
class ImovelDetail(DetailView):
    model = Imovel
    template_name='Dashboard/detail.html'
