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


#class LeaveComment_form(forms.ModelForm):
#    comment = forms.CharField(
#        widget=forms.Textarea(attrs={
#            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex m',
#            'rows': '1',
#            'placeholder':'Deja un comentario...'
#            }),
#        required=True
#        )
#    
#    class Meta:
#        model=Comment
#        fields=['comment']