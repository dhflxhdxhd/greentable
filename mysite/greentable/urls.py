from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('form/', views.form),
    path('result/', views.result),
    path('map/',views.map),
    path('info/',views.information),
]