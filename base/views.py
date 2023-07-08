from django.shortcuts import render


# Create your views here.
rooms = [
    {'id' : 1 , 'name' : 'lets learn python'},
    {'id' : 2 , 'name' : 'design with me'},
    {'id' : 3 , 'name' : 'frontend developers'},
]



def home(request):
    context = {'rooms' : rooms}
    return render(request , 'base/home.html' , context)



def room(request , id):
    room = None
    for i in rooms:
        if i['id'] == id:
            room = i
    context = {'room' : room}        

    return render(request , 'base/room.html' , context)

