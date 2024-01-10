from django.urls import path
#from grpc import views as grpc_views
from . import views

from . import views

urlpatterns = [
    path("grpc/geolocation/", views.GetGeolocation),
]