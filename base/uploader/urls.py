from django.contrib import admin
from django.urls import path
from uploader import views

urlpatterns = [
    path('', views.uploader, name="uploader"),
    path('update/<id>/', views.update, name="update"),
    path('delete/<id>/', views.delete, name="delete")
]