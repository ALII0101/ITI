
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_trainees(request):
    return HttpResponse("<h1>Welcome to All Trainees Page</h1>")

def get_trainee(request):
    return HttpResponse(f"<h1>Welcome to Trainee Page </h1>")

def insert_trainee(request):
    return HttpResponse("<h1>Welcome to Insert Trainee Page</h1>")

def update_trainee(request, id):
    return HttpResponse(f"<h1>Welcome to Update Trainee Page {id}</h1>")

def delete_trainee(request, id):
    return HttpResponse(f"<h1>Welcome to Delete Trainee Page {id}</h1>")