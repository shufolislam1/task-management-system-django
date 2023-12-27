from django import forms
from .models import catagoryModel

class catagory_model_form(forms.ModelForm):
    class Meta:
        model = catagoryModel
        fields = '__all__'