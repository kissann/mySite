"""MySite01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Student.views import *
from AuthAndReg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('Student.urls')),
    path('rooms/', Rooms),
    path('register/', RegView),
    path('register/create',RegCreate,name='register'),
    path('login/',LogView),
    path('login/enter',LogEnter,name='login'),
    path('home/',HomeView,name='home'),
    path('logout/',LogoutView,name='logout')

]
