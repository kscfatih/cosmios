from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('login işlemi başarılı')
            login(request, user)
            messages.success(request, 'Login işleminiz başarılı')
            return redirect('blog_liste')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
            return render(request, 'accounts/login.html')
    
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yapıldı!')
    return redirect('login')

def register(request):
    return render(request, 'accounts/register.html')