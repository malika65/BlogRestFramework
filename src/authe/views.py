from django.shortcuts import render
from authe.models import Author
from .forms import AuthorRegisterForm, LoginForm, PasswordResetForm, NewPasswordForm
from .utils import  send_reset_link
from .models import ConfirmCode
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from authe.tasks import send_verified_link
from django.shortcuts import redirect


# Create your views here.
def registration(request):
    form = AuthorRegisterForm
    if request.method == 'POST':
        save_form = AuthorRegisterForm(request.POST)
        if Author.objects.filter(email=request.POST['email'], verified = False):
            author = Author.objects.get(email=request.POST['email'])
            author.codes.all().delete()
            code = ConfirmCode.objects.create(author=author)
            send_verified_link,delay(f'Чтобы подтвердить почту перейите по ссылке:127.0.0.1:8000/auth/confirm/{code.code}/',code.author.email)
            return render(request,'reply.html',{'message':'Проверьте почту','success':True})

        if save_form.is_valid():
            author = Author.objects.create(
                password = request.POST['password'],
                username = request.POST['username'],
                email = request.POST['email']
            )           
            author.set_password(request.POST['password'])
            author.save()
            code = ConfirmCode.objects.create(author=author)

            send_verified_link.delay(f'Чтобы подтвердить почту перейите по ссылке:http://127.0.0.1:8000/auth/confirm/{code.code}/',code.author.email)
            
            return render(request,'reply.html',{'message':'Проверьте почту','success':True})
        return render(request, 'registration.html', {'form':form,'errors':save_form.errors})
    return render(request, 'registration.html', {'form':form})

def confirm(request,code):
    if ConfirmCode.objects.filter(code=code):
        code = ConfirmCode.objects.get(code=code)
        if not code.confirm:
            code.confirm = True
            code.author.verified = True
            code.author.save()
            code.save()
            return render(request,'reply.html', {'message':'Ваша почта подтверждена','success':True})

        return render(request,'reply.html', {'message':'Ваша почта уже подтверждена','success':True})

    return render(request,'reply.html', {'message':'Ваша код устарел либо неправавильный'})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user:
            auth_login(request,user)
            return render(request,'reply.html',{'message':'Вы вошли','success':True})
        return render(request,'reply.html',{'message':'Такой пользователь не найден','success':False})

    return render(request,'login.html',{'form':form})


def reset_password(request):
    form = PasswordResetForm()
    if request.method == 'POST':
        author = Author.objects.filter(email=request.POST['email'])
        if author:
            code = ConfirmCode.objects.create(author=author.last(),reset=True)
            send_verified_link.delay(f'Чтобы сбросить пароль перейите по ссылке:http://127.0.0.1:8000/auth/confirm/new_password/{code.code}',code.author.email)
            return render(request,'reply.html',{'message':'Проверьте почту','success':True})
    
        else:
            return render(request,'reply.html',{'message':'Введите почту , с которой вы регистрировались','success':False})

    return render(request,'reset_password.html',{'form':form})

def new_password(request,code):
    if ConfirmCode.objects.filter(code=code):
        code = ConfirmCode.objects.get(code=code,reset = True)
        if not code.confirm:
            code.confirm = True
            code.save()
            new_password = get_random_string(length=8)
            code.author.set_password(new_password)
            code.author.save()
            send_verified_link.delay(f'Ваш пароль: {new_password}',code.author.email)
            return render(request,'reply.html',{'message':'Новый пароль отправлен на почту','success':True})
        return render(request,'reply.html',{'message':'Ваш пароль был уже сброшен. Проверьте почту','success':False})
    return render(request,'reply.html',{'message':'Неверный код','success':False})


def edit_password(request):
    form = NewPasswordForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.check_password(request.POST['old_password']):
                
                request.user.set_password(request.POST['new_password'])
                request.user.save()
                return redirect('authe:login')
                # return render(request,'reply.html',{'message':'Поменяли','success':True})
            print()
            return render(request,'reply.html',{'message':'Неверный старый пароль','success':False})


        # return render(request,'new_passowrd.html',{'form':form})


    return render(request,'new_password.html',{'form':form})

   