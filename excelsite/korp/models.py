from django.db import models
from django.urls import reverse

# Create your models here.
class Pages (models.Model):
    title=models.CharField(max_length=255, verbose_name='Название')
    content=models.TextField(blank=True, verbose_name='контент')
    photo=models.ImageField(upload_to="photos/%Y/%m/%d",default='', verbose_name='Фото')
    time_create=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_update=models.DateTimeField(auto_now=True, verbose_name='Модифицировано')
    is_published=models.BooleanField(default=True, verbose_name='Публикация')
    cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url (self):
        return reverse('proj_ref',kwargs={'post_id':self.pk})

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name='Страница'
        verbose_name_plural= 'Страницы'
        ordering=['time_create','title']





class Menu (models.Model):
    title=models.CharField(max_length=255)
    url=models.TextField(blank=True)
    urlname = models.TextField(blank=True)
    def __str__(self):
        return  self.title


class Category (models.Model):
    name=models.CharField(max_length=255, db_index=True)
    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('category_ref', kwargs={'cat_id': self.pk})


class Application  (models.Model):
    name = models.CharField(max_length=255, blank=False,verbose_name='ФИО клиената' )
    email = models.EmailField(max_length=255,blank=False,verbose_name='Email клиента', unique=True)
    phone = models.CharField(max_length=255, blank=False,verbose_name='Телефон клиента')
    area = models.CharField(max_length=255, blank=False,verbose_name='Тип курса')
    conf=models.IntegerField(default=True, verbose_name='Согласие на обработку данных')

    def __str__(self):
        return  self.name


