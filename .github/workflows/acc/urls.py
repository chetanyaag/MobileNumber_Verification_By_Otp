from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.log, name='log'),
    path('ver', views.ver, name='ver'),
    path('otp',views.otp,name='otp')
]