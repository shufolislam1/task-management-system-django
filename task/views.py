from django.shortcuts import render
from .forms import task_Model_Form

# Create your views here.
def add_task(request):
    task_form = task_Model_Form()
    return render(request, 'add_task.html', {'data':task_form})
    