from django.shortcuts import render, redirect
from .forms import task_Model_Form
from .models import taskModel

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = task_Model_Form(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
        
    else:
        task_form = task_Model_Form()
    print(task_form)
    return render(request, 'add_task.html', {'data':task_form})
    
def edit_task(request, id):
    task = taskModel.objects.get(pk=id)
    task_form = task_Model_Form(instance=task)
    if request.method == 'POST':
        task_form = task_Model_Form(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    return render(request, 'add_task.html', {'data':task_form})

def delete_task(request, id):
    task = taskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')