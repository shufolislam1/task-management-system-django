from django.shortcuts import render
from task.models import taskModel

def showTasks(request):
    data = taskModel.objects.all()
    return render(request, 'show_tasks.html', {'data':data})