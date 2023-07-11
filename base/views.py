from django.shortcuts import render , redirect
from.models import Room , Topic , Message
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
#rooms = [
    #{'id' : 1 , 'name' : 'lets learn python'},
    #{'id' : 2 , 'name' : 'design with me'},
   # {'id' : 3 , 'name' : 'frontend developers'},
#]


def loginpage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , 'User doesn\'t exist')
        user = authenticate(request , username=username , password=password)
        if user != None:
            login(request , user)
            return redirect('home')
        
    context = {'page': 'login'}
  
    return render(request , 'base/login_register.html', context)


def logoutuser(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username =  user.username.lower()
            user.save()
            login(request , user)
            return redirect('home')
        else:
            messages.error(request , 'An error occurred during registration')
    
    context = {'form': form}
    return render(request , 'base/login_register.html'  ,context)


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
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', id = room.id)
    
    
    context = {'room' : room , 'room_messages' : room_messages , 'participants' : participants}        
    return render(request , 'base/room.html' , context)

@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def deleteroom(request , id):
    room = Room.objects.get(id = id)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj' : room}
    return render(request , 'base/delete.html' , context)


@login_required(login_url='/login')
def deletemessage(request , id):
    
    message = Message.objects.get(id = id)
   
    if request.method == 'POST':
        message.delete()
        referring_url = request.POST.get('referring_url')
        return redirect(referring_url)
    
    context = {'message' : message}
    return render(request , 'base/delete_m.html' , context)