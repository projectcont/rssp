# Generated by Django 4.2 on 2024-01-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0031_alter_flat_floor_alter_land_floor_alter_ofis_floor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AddField(
            model_name='land',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AddField(
            model_name='ofis',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AddField(
            model_name='proizv',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AddField(
            model_name='psn',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AddField(
            model_name='retail',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AddField(
            model_name='tc',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AddField(
            model_name='torg',
            name='scan',
            field=models.TextField(blank=True, null=True, verbose_name='Скан заявок'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='land',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='ofis',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='proizv',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='psn',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='retail',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='tc',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='torg',
            name='adres',
            field=models.CharField(help_text='(с городом)', max_length=255, verbose_name='Адрес'),
        ),
    ]