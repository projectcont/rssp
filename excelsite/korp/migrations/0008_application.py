# Generated by Django 4.2 on 2023-07-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0007_alter_pages_options_alter_pages_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО клиената')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email клиента')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон клиента')),
                ('area', models.CharField(max_length=255, verbose_name='Тип курса')),
                ('conf', models.IntegerField(default=True, verbose_name='Согласие на обработку данных')),
            ],
        ),
    ]
