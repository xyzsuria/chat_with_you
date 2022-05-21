from django.shortcuts import render
from chat.models import Room
from django.http import HttpResponse, StreamingHttpResponse
import json
# Create your views here.


def index(request):
    return render(request, 'chat/index.html',{
        'rooms': Room.objects.all()
    })


def room(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'chat/room.html',{
        'room_name': room_name
    })


def chat(request):
    print('----------------')
    print(request)
    if request.method == "POST":
        response = {}
        response['data'] = 'hello'
        response['ret'] = 0
        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        return HttpResponse("I don't know")