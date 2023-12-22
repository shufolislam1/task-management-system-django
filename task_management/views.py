from django.shortcuts import render

def showTasks(request):
    return render(request, 'show_tasks.html')