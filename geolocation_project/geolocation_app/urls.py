from django.urls import path
#from grpc import views as grpc_views
from . import views

urlpatterns = [
    path("", views.index),
    path("grpc/geolocation/", views.GetGeolocation),
]