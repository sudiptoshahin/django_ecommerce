from __future__ import unicode_literals
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home-page'),
    
]