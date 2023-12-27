from django import forms
from .models import taskModel

class task_Model_Form(forms.ModelForm):
    class Meta:
        model = taskModel
        fields = '__all__'
        