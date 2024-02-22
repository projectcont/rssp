from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

# https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield

class FormAdmin(forms.ModelForm):
    description=forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = RealtyCommon
        fields = '__all__'



class ContactForm(forms.Form):
	client = forms.CharField(max_length = 100)

	phone = forms.CharField()

