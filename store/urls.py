from django.urls import path
from . import views
""" De Store import a views tem que ser a pasta que está a views
 Tem que criar outra view se quiser outra página e depois que criar a view cria o caminho que
aponta a view

para colocar o id na minha página é só colocar <id>/ depois da barra / e na view que é relacionada
a página com id criar um parametro id lá na função do lado de request 
"""
urlpatterns = [
    path('', views.home, name='home'),
    path('store/<id>/', views.store, name='store'),
]
