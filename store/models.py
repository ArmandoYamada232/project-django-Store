from django.db import models

# Create your models here.

class store(models.Model):
    title = models.CharField(max_length=50)
    store_name = models.CharField(max_length=20)
    slug = models.SlugField()
    price = models.FloatField()
    cover = models.ImageField(upload_to = 'store/covers/%Y/%M/%d/')
    
