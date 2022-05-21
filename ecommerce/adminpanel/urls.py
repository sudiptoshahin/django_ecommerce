from __future__ import unicode_literals
from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.adminPanel, name='panel'),

    path('panel/product/add/', views.addProduct, name='add-product'),
]