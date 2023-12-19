from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenges, name="challenges"),
]