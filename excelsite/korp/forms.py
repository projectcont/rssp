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
    conf = forms.BooleanField(required=True, label='Подтверждаю согласие на обработку персональных данных',)
    #area = forms.CharField(max_length=255, label='область',choices=CHOICES ),
    area = forms.ChoiceField(choices=CHOICES,label='Область сертификации',)

class addPageForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model=Pages
        fields=['title','content','cat']
        #fields='__all__'
