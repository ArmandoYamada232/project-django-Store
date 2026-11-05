from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

"""É a porta de entrada da minha aplicação indicar para o django onde ele vai encontrar
meu app ou a página ex: o path(caminho) incluindo a store.url (store é o nome do app)
que tem outra urls no app

Nunca começar um caminho com barra, pode terminar mas nunca começar"""

"""
Cliente faz http request e o site retorna com uma http response
"""
def home(request):
    return HttpResponse ('home')

def sobre(request):
    return HttpResponse ('Sobre')

def contato(request):
    return HttpResponse ('contato')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('home/', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
