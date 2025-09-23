from django.shortcuts import render
from django.http import HttpResponse  # ✅ صحيح# Create your views here.
def login(request):
    return HttpResponse("<h1>Welcom to Login Page</h1>")

def logout(request):
    return HttpResponse("<h1>Welcom to Logout Page</h1>")

def register(request):
    return HttpResponse("<h1>Welcom to Register Page</h1>")