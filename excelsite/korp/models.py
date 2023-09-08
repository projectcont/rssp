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


#-------------------------------------------------------------------------------------
class Menu (models.Model):
    title=models.CharField(max_length=255, verbose_name='Название пункта меню')
    url=models.TextField(blank=True, verbose_name='url')
    urlname = models.TextField(blank=True, verbose_name='url-name' )
    def __str__(self):
        return  self.title

    class Meta:
        verbose_name='Меню'
        verbose_name_plural= 'Меню'
        ordering=['id']


#-------------------------------------------------------------------------------------
class Category (models.Model):
    name=models.CharField(max_length=255, db_index=True, verbose_name='Название категории')
    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('category_ref', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name='Категория'
        verbose_name_plural= 'Категории'
        ordering=['name']

#-------------------------------------------------------------------------------------
class Application  (models.Model):
    name = models.CharField(max_length=255, blank=False,verbose_name='ФИО клиената' )
    email = models.EmailField(max_length=255,blank=False,verbose_name='Email клиента', unique=True)
    phone = models.CharField(max_length=255, blank=False,verbose_name='Телефон клиента')
    area = models.CharField(max_length=255, blank=False,verbose_name='Тип курса')
    conf=models.IntegerField(default=True, verbose_name='Согласие на обработку данных')

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name='Заявка'
        verbose_name_plural= 'Заявки'
        ordering=['id']


#-------------------------------------------------------------------------------------
''' 
class Rating  (models.Model):
    valuta = models.CharField(max_length=255, blank=False,verbose_name='Валюты' )
    exchrate=models.FloatField(null=True, blank=True)(default=True, blank=False, verbose_name='Курс обмена')
    date = models.DateTimeField(verbose_name='Дата')

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name='Валюта'
        verbose_name_plural= 'Валюты'
        ordering=['id']
 '''
#-------------------------------------------------------------------------------------
class Kurs  (models.Model):
    title = models.CharField(max_length=255, blank=False,verbose_name='Курс' )
    pricerub=models.FloatField(default=True, blank=False, verbose_name='Цена в руб.')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name='Курс'
        verbose_name_plural= 'Курсы'
        ordering=['id']


