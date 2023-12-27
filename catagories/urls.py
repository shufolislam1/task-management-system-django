from django.urls import path
from .views import add_catagory

urlpatterns = [
    path('add/', add_catagory, name='addCatagory')
]
