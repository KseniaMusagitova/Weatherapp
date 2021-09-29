from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]

# обращаемся в файл views и берем index
