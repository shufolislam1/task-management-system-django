from django.shortcuts import render
from task.models import taskModel
from catagories.models import catagoryModel

def showTasks(request):
    data = taskModel.objects.all()
    cataData = catagoryModel.objects.all()
    # print(cataData)
    return render(request, 'show_tasks.html', {'data':data, 'cataData':cataData})