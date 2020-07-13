from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add_widget/', views.add_widget),
  path('widget/<int:id>/delete', views.delete)
]
