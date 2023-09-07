from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'user does not exist!'})
    
        
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('repeat-password'):
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'password does not match!'})        
    return render(request, 'signup.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

