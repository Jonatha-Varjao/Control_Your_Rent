from django import forms
from django.contrib.auth.models import User
from ControlMyRent.models import UserProfile, Imovel

# FORM LOGUINS


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

# FORM DO USUARIO


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


# FORM IMOVEL
class ImovelUserForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ('nome', 'cep', 'uf', 'stats', 'position')


# ADICIONANDO FIELDS AO PADRAO USER
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('cpf', 'data_de_nascimento', 'sexo')  # userProfilePic

# EDITAR PERFIL DO USUARIO

class UserProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'cpf',
                  'data_de_nascimento', 'sexo')
    

    def save(self, commit=True):
        user = super(UserProfileEditForm, self).save(commit=False)


# editar senhas TODO


def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
        raise forms.ValidationError('Passwords don\'t match.')
    return cd['password2']

# TODO
# BUSCAR USUARIO/IMOVEIS
