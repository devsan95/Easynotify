from django.shortcuts import render
from django.http import HttpResponse

def showwelcomepage(request):
    return render(request, 'index.html')