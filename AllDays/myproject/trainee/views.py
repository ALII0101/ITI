
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainee
# Create your views here.
# def all_trainees(request):
#     return HttpResponse("<h1>Welcome to All Trainees Page</h1>")

# def get_trainee(request):
#     return HttpResponse(f"<h1>Welcome to Trainee Page </h1>")

# def insert_trainee(request):
#     return HttpResponse("<h1>Welcome to Insert Trainee Page</h1>")

# def update_trainee(request, id):
#     return HttpResponse(f"<h1>Welcome to Update Trainee Page {id}</h1>")

# def delete_trainee(request, id):
#     return HttpResponse(f"<h1>Welcome to Delete Trainee Page {id}</h1>")


def all_trainee(request):
    # trainee=[[1,'Ali','ali224101539@ksiu.edu.eg','photo'],[2,'Ashraf','ashraf223101539@ksiu.edu.eg','photo']]
    trainee=Trainee.objects.all()  
    return render(request, 'alltrainee.html', context={'trainee':trainee})

def get_trainee(request):
    return HttpResponse(f"<h1>Welcom to Trainee  Page</h1>")

def insert_trainee(request):
    # return HttpResponse("<h1>Welcom to Insert Trainee Page</h1>")
    # print(request.POST)
    if request.method=='POST':
        name=request.POST['trname']
        email=request.POST['tremail']
        image=request.FILES['trphoto']
        Trainee.objects.create(name=name,email=email,image=image)
        
        print(name,email,image)
        #save data in database
        # return HttpResponse(f"<h1>Welcom to Insert Trainee Page {name} {email} </h1>")
    return render(request, 'insert.html')

def update_trainee(request,id):
    return HttpResponse(f"<h1>Welcom to Update Trainee Page {id}</h1>")

def delete_trainee(request,id):
    return HttpResponse(f"<h1>Welcom to Delete Trainee Page {id}</h1>")

