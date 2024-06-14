from django.contrib import admin
from django.urls import path, include
from .views import showfoods, showbeverages, showsnacks, Addfoodtocart

app_name = "Item"
urlpatterns = [
    path("foods/", showfoods, name='showfoods'),
    path("foods/<int:item_id>/<int:quantity>/", Addfoodtocart, name='Addfoodtocart'),
    path("beverages/", showbeverages, name='showbeverages'),
    path("snacks/", showsnacks, name='showsnacks')
]