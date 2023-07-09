from django.shortcuts import render , redirect
from.models import Room
from .forms import RoomForm

# Create your views here.
#rooms = [
    #{'id' : 1 , 'name' : 'lets learn python'},
    #{'id' : 2 , 'name' : 'design with me'},
   # {'id' : 3 , 'name' : 'frontend developers'},
#]



def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
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