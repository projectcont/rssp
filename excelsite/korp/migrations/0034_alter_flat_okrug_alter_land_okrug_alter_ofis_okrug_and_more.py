# Generated by Django 4.2 on 2024-01-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0033_alter_flat_okrug_alter_land_okrug_alter_ofis_okrug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='land',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='ofis',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='proizv',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='psn',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='retail',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='tc',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='torg',
            name='okrug',
            field=models.CharField(choices=[('13', 'не применимо (вне Москвы)'), ('1', 'Центральный'), ('2', 'Северный'), ('3', 'Северо-Восточный'), ('4', 'Восточный'), ('5', 'Юго-Восточный'), ('6', 'Южный'), ('7', 'Юго-Западный'), ('8', 'Западный'), ('9', 'Северо-Западный'), ('10', 'Зеленоградский'), ('11', 'Троицкий'), ('12', 'Новомосковский')], max_length=100, null=True, verbose_name='Округ'),
        ),
    ]
