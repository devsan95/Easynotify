from django.contrib import admin
from django.urls import path, include
from .views import showemployee

app_name = "Employee"
urlpatterns = [
    path("employee/<int:employee_id>", showemployee, name='showemployee')
]