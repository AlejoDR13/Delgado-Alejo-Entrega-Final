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
        exclude = ['usuario_post']
        
        widgets = {
                    
                    'estreno': DateTimeInput(attrs={'class': 'form-control'}),

                }

class LeaveComment_form(forms.Form):

    usuario = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea, label='Comentario')
    post = forms.CharField(max_length=40, label='Post comentado')