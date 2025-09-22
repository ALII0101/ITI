from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def all_tracks(request):
    tracks=[[1,'python'],[2,'java'],[3,'C#']]
    return render(request, 'list.html', context={'tracks':tracks})

def get_track(request):
    return HttpResponse(f"<h1>Welcom to Track  Page</h1>")

def insert_track(request):
    return HttpResponse("<h1>Welcom to Insert Track Page</h1>")

def update_track(request,id):
    return HttpResponse(f"<h1>Welcom to Update Track Page {id}</h1>")

def delete_track(request,id):
    return HttpResponse(f"<h1>Welcom to Delete Track Page {id}</h1>")


