from urllib import request
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class CrearPelicula_form(forms.ModelForm):
    class Meta:
        model=Peliculas
        fields='__all__'
        
        widgets = {
                    'usuario_post': forms.HiddenInput,
                    'email': forms.HiddenInput,
                    'estreno': DateTimeInput(attrs={'class': 'form-control'}),
                    'dislikes': forms.HiddenInput,
                    'likes': forms.HiddenInput,

                }

class LeaveComment_form(forms.Form):

    usuario = forms.CharField(max_length=50)
    comentario = forms.CharField(widget=forms.Textarea)
    post = forms.CharField(max_length=40, label='Post comentado') #Estaria bueno ocultarlo a este
