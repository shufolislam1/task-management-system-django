from django.shortcuts import render, redirect
from .forms import catagory_model_form

# Create your views here.
def add_catagory(request):
    if request.method =='POST':
        addCatagory = catagory_model_form(request.POST)
        if addCatagory.is_valid():
            addCatagory.save()
            return redirect('addCatagory')
        
    else:
        addCatagory = catagory_model_form()
    return render(request, 'add_catagory.html', {'data': addCatagory})

