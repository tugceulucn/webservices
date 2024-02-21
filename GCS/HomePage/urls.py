from django.urls import path
from . import views

urlpatterns =[
    path("", views.index),
    path("index", views.index),
    path("param_details",views.param_details)
]