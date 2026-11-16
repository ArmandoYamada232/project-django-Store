framework do django já vem programado para ler arquivo pasta estatic dentro do app
e ela precisa de um name_space(pasta com mesmo nome do app)

pasta static -> pasta com name_space(pasta com mesmo nome do app - utilizado como padrão) -> pasta que pode ser de css, imagem, javascript, downloads

o projeto pode ter arquivos staticos que não estão atrelados a nenhum app ou seja colocando ele no static files dirs indique ao django onde buscar arquivos staticos

pasta fora do projeto -> base_static -> global(name_space) -> css -> arquivo