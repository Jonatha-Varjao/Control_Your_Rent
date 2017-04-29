
from django.conf.urls import url
from ControlMyRent import views


app_name = 'Rent'
urlpatterns = [
    # INDEX PAGE
    url(r'^$', views.index, name='index'),
    # LOGIN
    url(r'^login/$', views.user_login, name='login'),
    # LOGOUT
    #
    # REGISTER FORM
    url(r'^register/$', views.register, name='register'),
    # UPDATE FORM
    # PAINEL DE CONTROLE INDEX
    url(r'^landing/$', views.landingPage, name='landing'),
    # ADD IMOVEL
    url(r'^CadastrarImovel/$', views.ImovelRegister, name='imoveladd'),
    # DETALHE IMOVEL
    url(r'^Imovel/(?P<pk>[-\w]+)/$', views.imovel_detail, name='imovel_detail')
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
]
