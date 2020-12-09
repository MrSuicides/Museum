from django.urls import path, include
from .import views

urlpatterns = [
    path('F', views.indeex, name='indeex'),
]

