from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import  HttpResponseRedirect, HttpResponse
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def RegView(request):
    form = UserCreationForm(request.POST)
    return render(request, 'AuthAndReg/reg.html', context={'form': form})

def RegCreate(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('Validation =', form.is_valid())
        if form.is_valid():
            form.save()
            #user = form.save()
            #login(request,user)
            return redirect('http://127.0.0.1:8000/student/')
        else:
            return HttpResponseRedirect('/register/')
    else:
        return HttpResponseRedirect('/register/')
def LogView(request):
    form = AuthenticationForm()
    return render(request, 'AuthAndReg/log.html', context={'form':form})
def LogEnter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/home')
        else:
            return HttpResponseRedirect('/login')
    else:
         return HttpResponseRedirect('/login/')
def HomeView(request):

    return render(request, 'AuthAndReg/home.html',context={})
def LogoutView(request):
    if request.method=='POST':
        logout(request)
        return redirect('http://127.0.0.1:8000/login')
    else:
        return redirect('http://127.0.0.1:8000/home')