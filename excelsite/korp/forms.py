from django import forms
from .models import *

# https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield

class addApplForm (forms.Form):
    CHOICES = (
        ('ОБУЧЕНИЕ ЭКСПЕРТОВ И ПЕРСОНАЛА', 'ОБУЧЕНИЕ ЭКСПЕРТОВ И ПЕРСОНАЛА'),
        ('СЕРТИФИКАЦИЯ ЭКСПЕРТОВ И ПЕРСОНАЛА', 'СЕРТИФИКАЦИЯ ЭКСПЕРТОВ И ПЕРСОНАЛА'),
        ('СЕРТИФИКАЦИЯ ПРОДУКЦИИ, УСЛУГ, СИСТЕМ МЕНЕДЖМЕНТА', 'СЕРТИФИКАЦИЯ ПРОДУКЦИИ, УСЛУГ, СИСТЕМ МЕНЕДЖМЕНТА'),
    )

    name=forms.CharField(max_length=255, label='ФИО',)
    email = forms.EmailField(max_length=255, label='Email', )
    phone = forms.CharField(max_length=255, label='Телефон', )

    conf = forms.BooleanField(required=True, label='Подтв')
    #area = forms.CharField(max_length=255, label='область',choices=CHOICES ),
    area = forms.ChoiceField(choices=CHOICES,label='область',)
