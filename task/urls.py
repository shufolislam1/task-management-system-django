from django.urls import path
from .views import add_task

urlpatterns = [
    path('add/', add_task, name='addTask')
]
