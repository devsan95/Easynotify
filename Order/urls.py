from django.contrib import admin
from django.urls import path, include
from .views import showorders

app_name = "Order"
urlpatterns = [
    path("", showorders, name='showorders')
]