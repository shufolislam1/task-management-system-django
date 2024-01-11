from django.urls import path
from .views import add_task, edit_task, delete_task

urlpatterns = [
    path('add/', add_task, name='addTask'),
    path('edit/<int:id>',edit_task ,name='editTask'),
    path('delete/<int:id>',delete_task ,name='deleteTask'),
]
