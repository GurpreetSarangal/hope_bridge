from django.urls import path
from . import views

urlpatterns = [
    path("api/ngos/add/", views.add_ngo),
    path("api/ngos/", views.list_ngos),
]