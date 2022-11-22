from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'asfdwfe'},
    {'id': 3, 'name': 'afwfewf'},
    {'id': 4, 'name': 'asefdfsadafsd'},
]


def home(request):
    context = {'rooms' : rooms}
    i = type(context)
    return type(context)
    #return render(request, 'base/index.html', context)

def room(request, pk):

    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'base/room.html', context)