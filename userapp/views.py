from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user) # 인증된 사용자를 로그인 처리
            return redirect('index') 
        else:
            return render(request, 'signup.html', {'form': form})       
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form' : form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    
def logout(request):
    auth.logout(request)
    return redirect('index')