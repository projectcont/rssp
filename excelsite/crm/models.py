from django.db import models
from korp.models import Category
from django.urls import reverse
from django.apps import apps
from multiselectfield import MultiSelectField
import utils.get_okrug_titles

#apps.get_model('korp', 'Category')

class Client  (models.Model):
    name = models.CharField(max_length=255, blank=False,verbose_name='ФИО клиента' )
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='Email клиента', unique=True)
    phone = models.CharField(max_length=255, blank=False, verbose_name='Телефон клиента')
    phone1 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп1. телефон клиента')
    phone2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп2. телефон клиента')
    phone3 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп3. телефон клиента')
    phone4 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп4. телефон клиента')
    phone5 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп5. телефон клиента')

    whatsapp = models.CharField(max_length=255, null=True, blank=True, verbose_name='Whatsapp клиента')
    telegram = models.CharField(max_length=255, null=True, blank=True, verbose_name='Telegram клиента')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    login = models.CharField(max_length=255, null=True, blank=True, verbose_name='логин клиента')
    dop1 = models.CharField(max_length=255, null=True, blank=True, verbose_name='доп1 клиента')
    dop2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='доп2 клиента')
    dop3 = models.CharField(max_length=255, null=True, blank=True, verbose_name='доп3 клиента')

    STATUS_RANGE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    status = models.CharField(max_length=2, choices=STATUS_RANGE, blank=True, default='m', help_text='Book availability')

    def __str__(self):
        result = f" {self.id}  {self.name} "
        return result


    def get_absolute_url(self): return reverse('client_ref', kwargs={'client_id': self.pk})

    class Meta:
        verbose_name='Клиент'
        verbose_name_plural= 'Клиенты'
        ordering=['id']


#------ Zayavki---------------------

class Zayavki  (models.Model):
    categ_select = (  ('ofis', 'ОФИСЫ '),    ('torg', 'ТОРГОВАЯ ПЛОЩАДЬ'),    ('tc', 'ЗДАНИЯ'),        ('proizv', 'ПРОИЗВОДСТВО'),    ('sklad', 'СКЛАДЫ'),    ('psn', 'ПСН'),    ('retail', 'РИТЕЙЛ'),    ('land', 'ЗЕМЛЯ'),    ('flat', 'КВАРТИРЫ'),   )
    categ  = models.CharField(max_length=100, choices= categ_select, blank=False, null=True, verbose_name='Категория', )

    client = models.ForeignKey('Client', on_delete=models.PROTECT, blank=False, verbose_name='Клиент')

    rentsale_type = (('rent', 'Арендовать'), ('sale', 'Купить'))
    rentsale = models.CharField(max_length=100, choices=rentsale_type, blank=False, null=True, verbose_name='Арендовать/купить', )

    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')

    OKRUG_SELECT = (('1000', 'Все равно'),('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'),
                    ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'),
                    ('7', 'Юго-Западный'), ('8', 'Западный'),
                    ('9', 'Северо-Западный'),
                    ('10', 'Зеленоградский'), ('11', 'Троицкий'),
                    ('12', 'Новомосковский'),)


    okrug = MultiSelectField(choices=OKRUG_SELECT, max_choices=12, max_length=30, null=True, verbose_name='Округ')

    square = models.DecimalField(max_digits=20, decimal_places=2, blank=False, verbose_name='мин. площадь кв.м.')
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, default=0,  verbose_name='макс. цена, руб ')

    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        result=f"Заявка: id{self.id}  {self.categ}  {self.client}"
        return result

    def get_okruga(self):
        result=utils.get_okrug_titles.go(self)
        return result

    def get_categ_title (self):
        if self.categ == "ofis": result="Офисы"
        if self.categ == "torg": result = ""
        if self.categ == "ofis": result = ""
        if self.categ == "ofis": result = ""
        if self.categ == "ofis": result = ""
        if self.categ == "ofis": result = ""
        if self.categ == "ofis": result = ""
        if self.categ == "ofis": result = ""
        if self.categ == "ofis": result = ""
        return result

    def get_absolute_url(self): return reverse('requests_ref', kwargs={'zayav_id': self.pk})

    class Meta:
        verbose_name='Заявка'
        verbose_name_plural= 'Заявки'
        ordering=['id']



#----------------------------------------------------------------------------



class Export (models.Model):
    title=models.CharField(max_length=255, verbose_name='Название')
    is_using=models.BooleanField(default=True, verbose_name='Применяется')
    def get_absolute_url (self): return reverse('export_ref',kwargs={'export_id':self.pk})
    def __str__(self):return  self.title
    class Meta:
        verbose_name='Выгрузка'
        verbose_name_plural= 'Выгрузки'
        ordering=['title', 'is_using']