from django.shortcuts import render
from .forms import catagory_model_form

# Create your views here.
def add_catagory(request):
    addCatagory = catagory_model_form()
    return render(request, 'add_catagory.html', {'data': addCatagory})

