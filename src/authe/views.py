from django.shortcuts import render
from authe.models import Author
from .forms import AuthorRegisterForm, LoginForm, PasswordResetForm, NewPasswordForm
from .utils import send_verified_link, send_reset_link
from .models import ConfirmCode

# Create your views here.
def registration(request):
    form = AuthorRegisterForm
    if request.method == 'POST':
        save_form = AuthorRegisterForm(request.POST)
        if Author.objects.filter(email=request.POST['email'], verified = False):
            author = Author.objects.get(email=request.POST['email'])
            author.codes.all().delete()
            code = ConfirmCode.objects.create(author=author)
            send_verified_link(f'Чтобы подтвердить почту перейите по ссылке:127.0.0.1:8000/auth/confirm/{code.code}/',code.author.email)
            return render(request,'reply.html',{'message':'Проверьте почту','success':True})

        if save_form.is_valid():
            author = Author.objects.create(
                password = request.POST['password'],
                username = request.POST['username'],
                email = request.POST['email']
            )           
            code = ConfirmCode.objects.create(author=author)

            send_verified_link(f'Чтобы подтвердить почту перейите по ссылке:http://127.0.0.1:8000/auth/confirm/{code.code}/',code.author.email)
            
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
    return render(request,'login.html',{'form':form})


def reset_password(request):
    form = PasswordResetForm()
    if request.method == 'POST':
        if Author.objects.filter(email=request.POST['email']):
            a = Author.objects.get(email=request.POST['email'])
            code = ConfirmCode.objects.create(author=a)
            send_verified_link(f'Чтобы сбросить пароль перейите по ссылке:http://127.0.0.1:8000/auth/confirm/new_password/{code.code}',a.email)
            return render(request,'reply.html',{'message':'Проверьте почту','success':True})
    
        else:
            return render(request,'reply.html',{'message':'Введите почту , с которой вы регистрировались','success':False})

    return render(request,'reset_password.html',{'form':form})

def new_password(request,code):
    form = NewPasswordForm()
    if request.method == 'POST':
        save_form = NewPasswordForm(request.POST)
        if ConfirmCode.objects.filter(code=code):
            c = ConfirmCode.objects.get(code=code)
            b = c.author
            b.password = save_form['password'].value()
            b.save()
            form_l = LoginForm()
            return render(request,'login.html',{'form':form_l})

    return render(request,'new_password.html',{'form':form})