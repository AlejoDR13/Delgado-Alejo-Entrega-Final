from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister_form(UserCreationForm):

    username=forms.CharField(label="Username")
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(u"Username existente, prueba con otro")
        return username

    email = forms.EmailField(required=True)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u"Email existente, prueba con otro")
        return email
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")
        help_text = {k: "" for k in fields}


class UserEdit_form(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u"Email existente, prueba con otro")
        return email
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirme su contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k: "" for k in fields}


class AboutUser_form(forms.Form):

    bio = forms.CharField(widget=forms.Textarea, label='Biografía', required=False)
    instagram = forms.URLField(required=False, label='Instagram')
    facebook = forms.URLField(required=False, label='Facebook')
    twitter = forms.URLField(required=False, label='Twitter')

class Avatar_form(forms.Form):

    img = forms.ImageField()