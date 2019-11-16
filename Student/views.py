from django.shortcuts import render
from Student.models import *


def Show_student(request):
    name = 'Anna'
    obj01 = Student.objects.all()
    # return render(request, 'RoomsList/index_old.html', context={'num_room': obj01.num_room,
    #                                                         'num_build': obj01.num_build,
    #                                                         'count_places': obj01.count_places,
    #                                                         'count_resident': obj01.count_resident})
    # return render(request, 'RoomsList/index.html', context={'rooms': obj01})
    return render(request, 'Student/index.html', context={'student': obj01})


def Show_st(request, slug):
    obj01 = Student.objects.get(slug=slug)
    return render(request, 'Student/rooms.html', context={'student': obj01})


def Rooms(request):
    obj02 = Rooms.objects.get(slug='1')
    return render(request, 'Student/rooms.html', context={'rooms': obj02})
# Create your views here.
