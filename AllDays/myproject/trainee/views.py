
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainee   
from django.shortcuts import redirect
from track.models import Track
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
    # trainee=Trainee.objects.all()  
    trainee=Trainee.get_all_trainee()
    return render(request, 'alltrainee.html', context={'trainee':trainee})

def get_trainee(request):
    return HttpResponse(f"<h1>Welcom to Trainee  Page</h1>")

def insert_trainee(request):
    # return HttpResponse("<h1>Welcom to Insert Trainee Page</h1>")
    # print(request.POST)
    # if request.method=='POST':
    #     name=request.POST['trname']
    #     email=request.POST['tremail']
    #     image=request.FILES['trphoto']
    #     Trainee.objects.create(name=name,email=email,image=image)
        
    #     print(name,email,image)


    context = {}
    context['tracks'] = Track.objects.all()

    if request.method == 'POST':
        trackobj = Track.objects.get(id=request.POST['trtrack'])
        if 'trphoto' in request.FILES:
            img = request.FILES['trphoto']
            Trainee.objects.create(name=request.POST['trname'], email=request.POST['tremail'], image=img, track=trackobj)
        else:
            Trainee.objects.create(name=request.POST['trname'], email=request.POST['tremail'], track=trackobj)
        return redirect('all_trainee')  
        #save data in database
        # return HttpResponse(f"<h1>Welcom to Insert Trainee Page {name} {email} </h1>")
    return render(request, 'insert.html', context)

def update_trainee(request, id):
    # return HttpResponse(f"<h1>Welcom to Update Trainee Page {id}</h1>")
    # trainee = Trainee.objects.get(id=id)
    tracks=Track.objects.all()
    trainee = Trainee.get_trainee_by_id(id)
    if request.method == 'POST':
        trainee.name = request.POST['trname']
        trainee.email = request.POST['tremail']
        trainee.track = Track.objects.get(id=request.POST['trtrack'])
        if 'trphoto' in request.FILES:
            img = request.FILES['trphoto']
            trainee.image = img
        trainee.save()
        return redirect('all_trainee')
        # return HttpResponse(f"<h1>Welcom to Update Trainee Page {trainee.name} {trainee.email}</h1>")
    return render(request, 'update.html', context={'trainee': trainee, 'tracks': tracks})

def delete_trainee(request,id):
    # return HttpResponse(f"<h1>Welcom to Delete Trainee Page {id}</h1>")
    # trainee=Trainee.objects.get(id=id).delete()
    # Trainee.objects.filter(id=id).update(status=False)
    trainee=Trainee.get_trainee_by_id(id=id).update(status=False)
    return redirect('all_trainee')

