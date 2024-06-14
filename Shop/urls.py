from django.contrib import admin
from django.urls import path, include
from .views import showshops

app_name = "Shop"
urlpatterns = [
    path("", showshops, name='showshops')
]