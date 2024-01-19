# Generated by Django 4.2 on 2023-12-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0015_alter_realty_okrug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/osn', verbose_name='Фото (осн.)'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото1'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo10',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото10'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото2'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото3'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото4'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото5'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото6'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo7',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото7'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo8',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото8'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='photo9',
            field=models.ImageField(blank=True, null=True, upload_to='photos/dop', verbose_name='доп.фото9'),
        ),
    ]
