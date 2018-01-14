from django.urls import path

from . import views

app_name = "teaching"
urlpatterns = [
    path("", views.index, name="index"),
]