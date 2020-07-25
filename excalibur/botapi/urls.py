# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('whatsapp/', views.WhatsappBot.as_view(), name="whatsappbot"),
]