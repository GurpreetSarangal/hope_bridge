from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Add this line
    path("api/user/add/", views.add_user),
    path("api/users/", views.list_users),  # Fix this - was pointing to list_ngos
    path("api/ngos/debug-db/", views.debug_db),
    path("api/ngos/list/", views.list_ngos, name="list_ngos"),
]  # Add missing closing bracket
