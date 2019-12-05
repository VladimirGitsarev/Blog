from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('Article title', max_length = 200)
    text = models.TextField('Article text')
    date = models.DateTimeField('Publication date')

    
