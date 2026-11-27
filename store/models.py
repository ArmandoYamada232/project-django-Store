from django.db import models
# O user importado aqui é uma tabela no banco de dados
from django.contrib.auth.models import User

# Criar classe -> dar um nome para o classe(model) -> classe tem que herdar de models.Model
# criar o campo(colunas que são como atributos de classe) = models.variavel semelhante ao mysql(parametro: charfiel etc..)

# category é 1 categoria para muitas receitas
# Essa category é uma chave estrangeira
# Esse on_delete é para quando apagar a categoria apagar as receitas da categoria
class Category(models.Model):
    name = models.CharField (max_length=50)

class store(models.Model):
    title = models.CharField(max_length=50)
    store_name = models.CharField(max_length=20)
    slug = models.SlugField()
    price = models.FloatField()
    cover = models.ImageField(upload_to = 'store/covers/%Y/%M/%d/')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    auth = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
