from django.contrib import admin
from django.urls import path
from uploader import views

urlpatterns = [
    path('', views.uploader, name="uploader")
]