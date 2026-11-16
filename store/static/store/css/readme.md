framework do django já vem programado para ler arquivo pasta estatic dentro do app
e ela precisa de um name_space(pasta com mesmo nome do app)

pasta static -> pasta com name_space(pasta com mesmo nome do app - utilizado como padrão) -> pasta que pode ser de css, imagem, javascript, downloads

o projeto pode ter arquivos staticos que não estão atrelados a nenhum app ou seja colocando ele no static files dirs indique ao django onde buscar arquivos staticos

pasta fora do projeto -> base_static -> global(name_space) -> css -> arquivo


A equipe do django utiliza um comando para coletar todos os arquivos estaticos e juntar só em um arquivo
comando: py manage.py collectstatic 

para funcionar precisa configurar o staticRoot -> caminho da pasta que eu quero que salve todos
os arquivos estaticos da minha aplicação 

deve se configurar em settings