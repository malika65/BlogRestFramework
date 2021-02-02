from django import forms
from .models import Author

class AuthorRegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    username=forms.CharField()
    email=forms.EmailField()
    class Meta:
        model = Author
        fields = ('email','username','password',)

    username.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Your login'
    })
    email.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Your email'
    })
    password.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Your password'
    })


class LoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField()

    username.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Your login'
    })

    password.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Your password'
    })


class PasswordResetForm(forms.Form):
    email = forms.CharField()

    email.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Напишите email, с которым вы регистрировались'
    })



class NewPasswordForm(forms.Form):
    old_password = forms.CharField()
    new_password = forms.CharField()

    old_password.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Старый пароль'
    })

    new_password.widget.attrs.update({
        'class':'form-control',
        'placeholder':'Новый пароль'
    })

    