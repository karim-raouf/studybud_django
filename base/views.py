from django.shortcuts import render , redirect
from.models import Room , Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
#rooms = [
    #{'id' : 1 , 'name' : 'lets learn python'},
    #{'id' : 2 , 'name' : 'design with me'},
   # {'id' : 3 , 'name' : 'frontend developers'},
#]


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)
    except:
        messages.error(request , 'User doesn\'t exist')
        
        
    context = {}
    return render(request , 'base/login_register.html' , context)







def home(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )
    
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms' : rooms ,'topics' : topics , 'room_count' : room_count}
    return render(request , 'base/home.html' , context)



def room(request , id):
    room = Room.objects.get(id=id)
    context = {'room' : room}        
    return render(request , 'base/room.html' , context)


def createroom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    
    else:
        form = RoomForm
    
    
    
    context = {'form' : form}
    return render(request , 'base/room_form.html' , context)


def updateroom(request ,id):
    room = Room.objects.get(id = id)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST , instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    context = {'form' : form}
    return render(request , 'base/room_form.html' , context)

def deleteroom(request , id):
    room = Room.objects.get(id = id)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj' : room}
    return render(request , 'base/delete.html' , context)