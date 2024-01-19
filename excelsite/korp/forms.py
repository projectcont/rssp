from django import forms
from .models import *

# https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield

class addPageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
        widgets={
            "title": forms.TextInput(attrs={"class":"form-input"}  ),
            "content": forms.Textarea(attrs={"cols": 60,"rows": 100, })
        }

    class Meta:
        model = Pages
        fields = ['title', 'content',]
        # fields='__all__'
