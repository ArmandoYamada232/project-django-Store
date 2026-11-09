from django.shortcuts import render

"""
Função render tem como função ler um arquivo e renderizar ele

faz a função com nome da página com request e depois retorna o render e a request
e logo após entre aspas o caminho do template

logo após informar a pasta no Dirs lá no settings do projeto
"""

# Create your views here.

"""
Na views adicionar o name_space que eu criei na função ao lado do caminho da página html

esse store antes do index.html é o name_space criado
dentro da pasta template para evitar colisão de nomes

posso criar um name_space para arquivos globais com o name space global
"""

# Pode criar uma variável para ir para o template usando context
def home(request):
    return render(request, 'store/pages/index.html', status=200, context={
        'name':'Armando Yamada'
    })