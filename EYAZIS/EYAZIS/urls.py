from django.urls import path
from EYAZIS_3 import views

urlpatterns = [
    path('', views.index),
    path("load", views.load_fun, name="load"),
    path("request", views.request_fun),
    path("delete", views.delete_fun, name="delete"),
]
