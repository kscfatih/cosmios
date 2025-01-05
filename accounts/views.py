from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from blogapp.models import Author

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

class Register(View):
    
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        isim = request.POST.get('isim')
        soyisim = request.POST.get('soyisim')
        email = request.POST.get('email')
        if password == repassword:
            user = User.objects.create_user(username=username, first_name = isim, last_name = soyisim, email=email, password=password)
            print(user)
            if user is not None:
                Author.objects.create(user=user)
                messages.success(request, 'User başarıyla oluşturuldu!')
                return redirect('login')
            else:
                messages.error(request, 'User oluşturulamadı')
                return render(request, 'accounts/register.html')
        else:
            messages.error(request, 'Lütfen parolaları aynı girin')
        return render(request, 'accounts/register.html')

def register(request):
    
    return render(request, 'accounts/register.html')