from django.shortcuts import render
from django.http import HttpResponse

def bakery_view(request):
    messaage = "Welcome to our bakery"
    return HttpResponse(messaage)

# Create your views here.
