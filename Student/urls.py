from django.urls import path
from .views import *
urlpatterns = [
    path('', Show_student, name='index'),
    path('<str:slug>',Show_st,name='Show_st'),
    path('rooms/', Rooms, name='rooms')
]