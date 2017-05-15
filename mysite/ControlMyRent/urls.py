
from django.conf.urls import url
from ControlMyRent import views
from ControlMyRent.views import ImovelListView


app_name = 'Rent'
urlpatterns = [
    # INDEX PAGE
    url(r'^$', views.index, name='index'),
    # PERFIL PAGE
    url(r'^Perfil/$', views.perfil, name='perfildetail'),
    # LOGIN
    url(r'^login/$', views.user_login, name='login'),
    # LOGOUT
    
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
    # DETALHE IMOVEL
    url(r'^DetalheImovel/(?P<pk>\d+)/$', views.ImovelDetailView.as_view() , name='imoveldetail'),
    # UPDATE IMOVEL

    # DELETAR IMOVEL
    url(r'^DeletarImovel/(?P<pk>\d+)/$', views.imovelDeleteView.as_view() , name='imoveldelete'),
    # GRAFICOS
    url(r'^Graficos/', views.graficos , name='graficos')
]
