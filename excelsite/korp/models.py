
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
import utils.get_okrug_title
from datetime import datetime

# -------------------------------------------------------------------------------------


# Create your models here.
class Pages (models.Model):
    title=models.CharField(max_length=255, verbose_name='Название')
    content=models.TextField(blank=True, verbose_name='контент')
    photo=models.ImageField(upload_to="photos/%Y/%m/%d", null=True, blank=True, verbose_name='Фото')
    time_create=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_update=models.DateTimeField(auto_now=True, verbose_name='Модифицировано')
    is_published=models.BooleanField(default=True, verbose_name='Публикация')
    metatitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='meta title')
    metadescription = models.TextField(null=True, blank=True, verbose_name='meta description')

    def get_absolute_url (self): return reverse('page_ref',kwargs={'post_id':self.pk})

    def __str__(self):return  self.title

    class Meta:
        verbose_name='_Страница'
        verbose_name_plural= '_Страницы'
        ordering=['time_create','title']

#-------------------------------------------------------------------------------------

class Category (models.Model):

    title = models.CharField(max_length=100, blank=False,null=False,
                              help_text='Название категории', verbose_name='Название категории')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    metatitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='meta title')
    metadescription = models.TextField(null=True, blank=True, verbose_name='meta description')
    alias = models.CharField(max_length=255, null=True, blank=True, verbose_name='alias')

    def __str__(self): return  self.title

    def get_absolute_url(self): return reverse('category_ref', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name='Категория'
        verbose_name_plural= 'Категории'
        ordering=['title']

#-------------------------------------------------------------------------------------




#------Owner-----------------------------------------------

class Owner  (models.Model):
    name = models.CharField(max_length=255, blank=False,verbose_name='ФИО владельца' )
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='Email владельца', unique=True)
    phone = models.CharField(max_length=255, blank=False, verbose_name='Телефон владельца')
    phone1 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп1. телефон владельца')
    phone2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп2. телефон владельца')
    phone3 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп3. телефон владельца')
    phone4 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп4. телефон владельца')
    phone5 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Доп5. телефон владельца')

    whatsapp = models.CharField(max_length=255, null=True, blank=True, verbose_name='Whatsapp клиента')
    telegram = models.CharField(max_length=255, null=True, blank=True, verbose_name='Telegram клиента')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        result = f" {self.id}  {self.name} "
        return result

    def get_absolute_url(self): return reverse('owner_ref', kwargs={'owner_id': self.pk})

    class Meta:
        verbose_name='_Владелец'
        verbose_name_plural= '_Владельцы'
        ordering=['id']
#------Owner-----------------------------------------------


# ---------Realty----------------------------------------------------------------------------


class Realty (models.Model):
    title=models.CharField(max_length=255, verbose_name='Название',blank=False,)
    adres = models.CharField(max_length=255, verbose_name='Адрес (с городом)',blank=False,)
    map = models.TextField(blank=False, verbose_name='Код с яндекс карты')
    square=models.DecimalField(max_digits=10, decimal_places=2, blank=False,verbose_name='Площадь кв.м.')
    photo=models.ImageField(upload_to="photos/osn", null=False, blank=True, verbose_name='Фото (основное)')
    time_create=models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    #categ = models.ManyToManyField("Category", related_name="Категория",blank=False, verbose_name='Категория')
    #worker = models.ForeignKey('auth.user', on_delete=models.PROTECT, blank=False, verbose_name='Сотрудник')

    worker =  models.ForeignKey(User, on_delete=models.PROTECT, blank=False, verbose_name='Сотрудник')
    owner  =  models.ForeignKey(Owner, on_delete=models.PROTECT, default=1, blank=False, verbose_name='Владелец')



    # --- sale ---
    sale = models.BooleanField(default=False, verbose_name='Продажа')
    price_sale = models.DecimalField(max_digits=10, decimal_places=0, default=0, blank=True, null=True, verbose_name='Цена продажи')
    sale_type_select = (('1', 'Продажа'), ('2', 'Переуступка прав аренды'),)
    sale_type = models.CharField(max_length=100, choices=sale_type_select, blank=True, null=True, verbose_name='Тип продажи', )

    sale_right_select = ( ('Собственник', 'Собственник'), ('Посредник', 'Посредник'), ('Застройщик', 'Застройщик (для квартир)'),)
    sale_right = models.CharField(max_length=100, choices=sale_right_select, blank=True, null=True, verbose_name='Право собственности ', help_text = "(только при продаже)" )

    # --- rent ---
    rent = models.BooleanField(default=False, verbose_name='Аренда')
    price_rent = models.DecimalField(max_digits=10, decimal_places=0, default=0, blank=True, null=True, verbose_name='Цена аренды')
    rent_type_select = ( ('1', 'Прямая'), ('2', 'Субаренда'),)
    rent_type = models.CharField(max_length=100, choices=rent_type_select, blank=True, null=True, verbose_name='Тип аренды', )

    OKRUG_SELECT = ( ('13', 'не применимо'),  ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'),  ('10', 'Зеленоградский'), ('11', 'Троицкий'),  ('12', 'Новомосковский'),)
    okrug = models.CharField(max_length=100, choices=OKRUG_SELECT, blank=False, null=True, verbose_name='Округ', )

    #--- not nessesary-----

    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    photo1 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото1')
    photo2 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото2')
    photo3 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото3')
    photo4 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото4')
    photo5 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото5')
    photo6 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото6')
    photo7 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото7')
    photo8 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото8')
    photo9 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото9')
    photo10 = models.ImageField(upload_to="photos/dop", null=True, blank=True, verbose_name='доп.фото10')

    maplink = models.CharField(max_length=255,  null=True, blank=True, verbose_name='Ссылка на яндекс карту')

    categ = models.CharField(max_length=255, null=True, blank=True, default='undef', verbose_name='Категория')

    '''
    def get_idl (self):
        result = 'realty' + self.categ + self.pk     
        return result
    '''

    idl = models.CharField(max_length=255, null=True, blank=True, default='2222', verbose_name='уникальный ID')

    description = models.TextField(blank=False, null=True, verbose_name='Описание')

    export_avito=models.BooleanField(default=False, verbose_name='Avito экспорт')
    export_yandex = models.BooleanField(default=False,verbose_name='Яндекс экспорт')
    export_afi = models.BooleanField(default=False,verbose_name='Afi экспорт')
    export_domclik = models.BooleanField(default=False,verbose_name='Domclik экспорт')
    export_5 = models.BooleanField(default=False,verbose_name='экспорт5')
    export_6 = models.BooleanField(default=False,verbose_name='экспорт6')

    floor_select_ = [('Не применимо', 'Не применимо'), ('Подвальный', 'Подвальный'), ('Цокольный', 'Цокольный'), ]
    floor_select2 = [(i, i) for i in range(1, 99)]
    floor_select_.extend(floor_select2)
    floor_select = tuple(floor_select_)
    floor = models.CharField(max_length=100, choices=floor_select, blank=False, null=True, verbose_name='Этаж', )
    floors = models.IntegerField(null=True, blank=False, verbose_name='Этажность')


    metatitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='meta title')
    metadescription = models.TextField(null=True, blank=True, verbose_name='meta description')

    def get_fields(self):
        result= [  [field.name, field.verbose_name, field.value_from_object(self)] for field in self.__class__._meta.fields]
        print("result=",result)
        return result

    def get_rentsale(self):
        if ((self.price_sale==0) or (self.price_sale==None)) and (self.price_rent!=0): result="rent"
        if (self.price_sale!=0) and ((self.price_rent==0) or (self.price_rent==None) ): result = "sale"
        if (self.price_sale != 0) and (self.price_rent != 0) and (self.price_sale != None) and (self.price_rent != None): result = "salerent"
        if ((self.price_sale == 0) and (self.price_rent == 0)) or ((self.price_sale == None) and (self.price_rent == None)): result = "noprice"
        return result

    def get_map(self):
        v=self.map
        v2 = v.replace('560', '100%')
        v2 = v2.replace('400', '500')
        v2 = v2.replace('frameborder="1"', 'frameborder="0"')
        return v2

    def get_okrug_title(self):
        result = utils.get_okrug_title.go(self)
        return  result

    def __str__(self):
        result = f" Объект: id={self.id},  {self.title},   Адрес {self.adres}"
        return result

    class Meta:
        abstract = True



class RealtyCommon (Realty):
    BUILD_CLASS = (('А', 'А'), ('А+', 'А+'), ('B', 'B'), ('B+', 'B+'), ('C', 'C'), ('C+', 'C+'), ('D', 'D'), ('D+', 'D+'),)
    buildclass = models.CharField(max_length=10, choices=BUILD_CLASS, blank=True, null=True, verbose_name='Класс здания', )
    bc = models.CharField(max_length=255, blank=True, null=True, verbose_name='Наименование БЦ')

    OTDELKA_SELECT = (('без отделки', 'без отделки'), ('чистовая', 'чистовая'), ('офисная', 'офисная'),)
    otdelka = models.CharField(max_length=50, choices=OTDELKA_SELECT, blank=True, null=True, verbose_name='Отделка', help_text = " обязательно для - Офис, ПСН, Торговое помещение, Питание,Гостиница, Здание" )

    BUILD_TYPE = (('Бизнес-центр ', 'Бизнес-центр '), ('Торговый центр', 'Торговый центр'), ('Административное здание', 'Административное здание'), ('Жилой дом', 'Жилой дом'), ('другой', 'другой'),)
    buildtype = models.CharField(max_length=100, choices=BUILD_TYPE, blank=True, null=True, verbose_name='Тип здания', help_text = "обязательно для: Офис, ПСН, Торговое, Склад, Производственное, Питания , Гостиница, Автосервис , Здание" )

    height = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True, verbose_name='Высота потолка (м)')

    entrance_type = (  ('С улицы',  'С улицы'), ('Со двора', 'Со двора'), )
    entrance = models.CharField(max_length=10, choices=entrance_type, blank=False, null=True, verbose_name='Вход', help_text = "обязательно для: ПСН, Питание" )

    parking_type = (  ('Нет', 'Нет'), ('На улице', 'На улице'), ('В здании', 'В здании'),   )
    parking = models.CharField(max_length=100, choices = parking_type, blank=True, null=True, verbose_name='Тип парковки', help_text = "обязательно для: Офис, ПСН, Торговое, Питание, Гостиница, Здание" )

    layout_type = (  ('Кабинетная', 'Кабинетная'), ('Открытая', 'Открытая'),  )
    layout = models.CharField(max_length=100, choices = layout_type, blank=True, null=True, verbose_name='Раскладка ', help_text = "для офисов обязательна " )


    class Meta:
        abstract = True
        ordering = ['time_create', 'title']

#---------------- 3  офисы ---------------
class Ofis (RealtyCommon):
    categ = models.CharField(max_length=255, null=True, blank=True, default='ofis', verbose_name='Категория')
    class Meta:
        abstract = False
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'
    def get_absolute_url(self):
        return reverse('itemref_ofis', kwargs={'pk': self.pk})

#---------------- 4  Торговая площадь ---------------
class Torg (RealtyCommon):
    categ = models.CharField(max_length=255, null=True, blank=True, default='torg', verbose_name='Категория')
    class Meta:
        abstract = False
        verbose_name = 'Торговая площадь'
        verbose_name_plural = 'Торговые площади'
    def get_absolute_url(self):
        return reverse('itemref_torg', kwargs={'pk': self.pk, })

#---------------- 21 квартира ---------------
class Flat (Realty):
    categ = models.CharField(max_length=255, null=True, blank=True, default='flat', verbose_name='Категория')
    marketType_select = ( ('Новостройка', 'Новостройка'), ('Вторичка', 'Вторичка'), )
    marketType = models.CharField(max_length=100, choices=marketType_select, blank=False, null=True, verbose_name='Новостройка или Вторичка ', )
    houseType_select = (('Кирпичный', 'Кирпичный'), ('Панельный', 'Панельный'),  ('Блочный', 'Блочный'),  ('Монолитный', 'Монолитный'),  ('Монолитно-кирпичный', 'Монолитно-кирпичный'),     )
    houseType = models.CharField(max_length=100, choices=houseType_select, blank=False, null=True, verbose_name='Тип дома', )
    rooms_select = (   ('Студия', 'Студия'), ('Своб. планировка', 'Своб. планировка'), ('1', '1'),   ('2', '2'),   ('3', '3'),   ('4', '4'),   ('5', '5'),   ('6', '6'),   ('7', '7'),   ('8', '8'),   ('9', '9'),   ('10 и более', '10 и более'),    )
    rooms = models.CharField(max_length=100, choices=rooms_select, blank=False, null=True,   verbose_name='Количество комнат', )
    status_select = (  ('Квартира', 'Квартира'), ('Апартаменты', 'Апартаменты'), )
    status = models.CharField(max_length=100, choices=status_select, blank=False, null=True,  verbose_name='Статус', )
    NewDevelopmentId= models.CharField(max_length=300, blank=False, null=True,
                                        verbose_name='NewDevelopmentId ', help_text = " Обязательно. ID корпуса (элементы Housing); если корпусов нет, то ID жилого комплекса (элементы Object)" )
    class Meta:
        abstract = False
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
    def get_absolute_url(self):
        return reverse('itemref_flat', kwargs={'pk': self.pk, })

#----------------5 Торговые центры ---------------
class Tc (RealtyCommon):
    categ = models.CharField(max_length=255, null=True, blank=True, default='tc', verbose_name='Категория')
    class Meta:
        abstract = False
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'
    def get_absolute_url(self):
        return reverse('itemref_tс', kwargs={'pk': self.pk, })

#----------------6 ------


#----------------7  Производство---------------
class Proizv(RealtyCommon):
    categ = models.CharField(max_length=255, null=True, blank=True, default='proizv', verbose_name='Категория')
    class Meta:
        abstract = False
        verbose_name = 'Производство'
        verbose_name_plural = 'Производство'
    def get_absolute_url(self):
        return reverse('itemref_proizv', kwargs={'pk': self.pk, })

#----------------8  Склады---------------
class Sklad(RealtyCommon):
    categ = models.CharField(max_length=255, null=True, blank=True, default='sklad', verbose_name='Категория')
    class Meta:
        abstract = False
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
    def get_absolute_url(self):
        return reverse('itemref_sklad', kwargs={'pk': self.pk, })

#---------------- 9 ПСН---------------
class Psn(RealtyCommon):
    categ = models.CharField(max_length=255, null=True, blank=True, default='psn', verbose_name='Категория')
    class Meta:
        abstract = False
        verbose_name = 'ПСН'
        verbose_name_plural = 'ПСН'
    def get_absolute_url(self):
        return reverse('itemref_psn', kwargs={'pk': self.pk, })

#---------------- 10 Ритейл---------------
class Retail(RealtyCommon):
    categ = models.CharField(max_length=255, null=True, blank=True, default='retail', verbose_name='Категория')
    class Meta:
        abstract = False
        verbose_name = 'Ритейл'
        verbose_name_plural = 'Ритейл'
    def get_absolute_url(self):
        return reverse('itemref_retail', kwargs={'pk': self.pk, })

#----------------11 Земля ---------------
class Land(RealtyCommon):
    categ = models.CharField(max_length=255, null=True, blank=True, default='land', verbose_name='Категория')
    class Meta:
        abstract = False
        verbose_name = 'Земля'
        verbose_name_plural = 'Земля'
    def get_absolute_url(self):
        return reverse('itemref_land', kwargs={'pk': self.pk, })














