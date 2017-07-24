
from django.conf.urls import url
from ControlMyRent import views
from ControlMyRent.views import ImovelListView


app_name = 'Rent'
urlpatterns = [
    # INDEX PAGE
    url(r'^$', views.index, name='index'),
    # PERFIL PAGE
    url(r'^Perfil/$', views.perfil, name='perfildetail'),    # LOGIN
    url(r'^login/$', views.user_login, name='login'),
    # LOGOUT
    url(r'^$',views.logout, name='logout'),
    # REGISTER FORM
    url(r'^register/$', views.register, name='register'),
    # UPDATE FORM (DADOS USUARIO)
    
    #url(r'^edit/$', views.atualizar_cadastro_usuario, name="edit_profile"),
    # UPDATE FORM (SENHA USUARIO)

        
    # PAINEL DE CONTROLE INDEX
    url(r'^landing/$', views.landingPage, name='landing'),
    #LISTAR IMOVEIS
    url(r'^ListarImoveis/$', ImovelListView.as_view() , name='imovelList'),
    # ADD IMOVEL
    url(r'^CadastrarImovel/$', views.ImovelRegister, name='imoveladd'),
    # UPDATE USUARIO
    url(r'^Perfil/(?P<pk>\d+)$', views.perfilUpdateView.as_view(), name='perfilupdate'), 
    url(r'^PerfilUpdate/(?P<pk>\d+)$', views.perfilProfileUpdateView.as_view(), name='userupdate'),
    # DETALHE IMOVEL
    url(r'^DetalheImovel/(?P<pk>\d+)/$', views.ImovelDetailView.as_view() , name='imoveldetail'),
    url(r'^ListarImoveis/DetalheImovel/(?P<pk>\d+)/$', views.ImovelNoEditView.as_view() , name='imovelnoedit'),
    # UPDATE IMOVEL
    url(r'^EditarImovel/(?P<pk>\d+)$', views.ImovelUpdateView.as_view(), name='imoveledit'),
    #url(r'^EditarDadosImovel/(?P<pk>\d+)$', views.ImovelImageUpdateView.as_view(), name='imagem_imovel_edit'),
    # DELETAR IMOVEL
    url(r'^DeletarImovel/(?P<pk>\d+)/$', views.ImovelDeleteView.as_view() , name='imoveldelete'),
    # GRAFICOS
    url(r'^Graficos/', views.graficos , name='graficos')
]
