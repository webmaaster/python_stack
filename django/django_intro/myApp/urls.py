from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('another_page', views.another_page),
  path('apple', views.does_nothing),
  path('region')
]