from django.db import models

# Create your models here.
class mainpage(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок', blank=True)
    description = models.CharField(max_length=200, verbose_name='короткий опис', blank=True)
    text_1 = models.CharField(max_length=200, verbose_name='картка 1', blank=True)
    text_2 = models.CharField(max_length=200, verbose_name='картка 2', blank=True)
    text_3 = models.CharField(max_length=200, verbose_name='картка 3', blank=True)
    text_4 = models.CharField(max_length=200, verbose_name='картка 4', blank=True)
    text_5 = models.CharField(max_length=200, verbose_name='картка 5', blank=True)
    
    # field1 = models.TextField(verbose_name='короткий опис', blank=True)