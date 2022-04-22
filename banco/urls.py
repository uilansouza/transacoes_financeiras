from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('envia_arquivo', views.enviar_arquivo, name="envia_arquivo"),
    path('acessa_transacoes', views.acessa_transacoes, name="consulta_trasacao")
]