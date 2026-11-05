from django.contrib import admin
from django.urls import path, include

"""É a porta de entrada da minha aplicação indicar para o django onde ele vai encontrar
meu app ou a página ex: o path(caminho) incluindo a store.url (store é o nome do app)
que tem outra urls no app

Nunca começar um caminho com barra, pode terminar mas nunca começar"""

"""
Cliente faz http request e o site retorna com uma http response
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),]
