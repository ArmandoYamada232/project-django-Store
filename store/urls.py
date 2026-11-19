from django.urls import path
from . import views
""" De Store import a views tem que ser a pasta que está a views
 Tem que criar outra view se quiser outra página e depois que criar a view cria o caminho que
aponta a view

para criar url dinâmicas

para colocar o id na minha página é só colocar conversor antes dos : <slug:id>/ depois da barra / e na view que é relacionada
a página com id criar um parametro id lá na função do lado de request

slug, int etc

Para formar url dinâmicamente precisa do parametro name pode chamar essas urls
onde quiser e quando quiser

pode criar app_names também que é outra forma de criar urls dinâmicos

vai ficar store_app_name:store
"""
app_name = 'store_app_name'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/<int:id>/', views.store, name='store'),
]
