# Generated by Django 4.2 on 2024-01-10 19:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_export'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavki',
            name='categ',
            field=models.CharField(choices=[('ofis', 'ОФИСЫ '), ('torg', 'ТОРГОВАЯ ПЛОЩАДЬ'), ('tc', 'ТОРГОВЫЕ ЦЕНТРЫ'), ('bc', 'БИЗНЕС ЦЕНТРЫ'), ('proizv', 'ПРОИЗВОДСТВО'), ('sklad', 'СКЛАДЫ'), ('psn', 'ПСН'), ('retail', 'РИТЕЙЛ'), ('land', 'ЗЕМЛЯ'), ('flat', 'КВАРТИРЫ')], max_length=100, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='zayavki',
            name='okrug',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1000', 'Все равно'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=30, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='zayavki',
            name='rentsale',
            field=models.CharField(choices=[('rent', 'Арендовать'), ('sale', 'Купить')], max_length=100, null=True, verbose_name='Арендовать/купить'),
        ),
    ]