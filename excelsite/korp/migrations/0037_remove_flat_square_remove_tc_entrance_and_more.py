# Generated by Django 4.2 on 2024-02-06 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korp', '0036_alter_land_entrance_alter_ofis_entrance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='square',
        ),
        migrations.RemoveField(
            model_name='tc',
            name='entrance',
        ),
        migrations.RemoveField(
            model_name='tc',
            name='height',
        ),
        migrations.RemoveField(
            model_name='tc',
            name='layout',
        ),
        migrations.AddField(
            model_name='land',
            name='land_type',
            field=models.CharField(blank=True, choices=[('Поселений (ИЖС)', 'Поселений (ИЖС)'), ('Сельхозназначения (СНТ, ДНП)', 'Сельхозназначения (СНТ, ДНП)'), ('Промназначения', 'Промназначения'), ('Личное подсобное хозяйство (ЛПХ)', 'Личное подсобное хозяйство (ЛПХ)')], max_length=50, null=True, verbose_name='Тип участка'),
        ),
        migrations.AddField(
            model_name='land',
            name='landarea',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Площадь участка, в сотках'),
        ),
        migrations.AddField(
            model_name='land',
            name='lease',
            field=models.CharField(choices=[('Поселений (ИЖС)', 'Поселений (ИЖС)'), ('Сельхозназначения (СНТ, ДНП)', 'Сельхозназначения (СНТ, ДНП)'), ('Промназначения', 'Промназначения'), ('Личное подсобное хозяйство (ЛПХ)', 'Личное подсобное хозяйство (ЛПХ)')], max_length=50, null=True, verbose_name='Залог'),
        ),
        migrations.AddField(
            model_name='torg',
            name='retail',
            field=models.BooleanField(default=False, verbose_name='Ретейл'),
        ),
        migrations.AlterField(
            model_name='land',
            name='sale_right',
            field=models.CharField(choices=[('Собственник', 'Собственник'), ('Посредник', 'Посредник')], help_text='(только при продаже)', max_length=100, null=True, verbose_name='Право собственности '),
        ),
        migrations.DeleteModel(
            name='Retail',
        ),
    ]
