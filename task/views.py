from django.shortcuts import render, redirect
from .forms import task_Model_Form

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
    