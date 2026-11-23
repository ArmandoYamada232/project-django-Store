from django.db import models

# Criar classe -> dar um nome para o classe(model) -> classe tem que herdar de models.Model
# criar o campo(colunas que são como atributos de classe) = models.variavel semelhante ao mysql(parametro: charfiel etc..)

class store(models.Model):
    title = models.CharField(max_length=50)
    store_name = models.CharField(max_length=20)
    slug = models.SlugField()
    price = models.FloatField()
    cover = models.ImageField(upload_to = 'store/covers/%Y/%M/%d/')
    is_published = models.BooleanField(default=False)
    #category = models.
