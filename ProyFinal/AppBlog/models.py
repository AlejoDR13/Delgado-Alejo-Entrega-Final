from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

class Generos(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"Genero: {self.nombre}"

class Peliculas(models.Model):
    #Datos del autor del POST
    usuario_post = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    autor= models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(max_length=40, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, null=True, blank=True)
    #Datos de la PELICULA (POST)
    titulo = models.CharField(primary_key=True, max_length=40)
    #genero = models.ManyToManyField(Generos, null=True, blank=True) SOLUCIONAR ESTO
    direccion = models.CharField(max_length=40)
    estreno = models.DateTimeField()
    duracion_en_min = models.IntegerField()
    Primer_cuerpo = models.TextField(max_length=10**10, null=True, blank=True)
    Segundo_cuerpo = models.TextField(max_length=10**10, null=True, blank=True)
    Primer_imagen = models.ImageField(upload_to='posts', null=False, blank=True)
    Segunda_imagen = models.ImageField(upload_to='posts', null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    
    def __str__(self) -> str:
        return f'{self.titulo} | {self.usuario_post}'

class Comment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comment_author')
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.CharField(max_length=100)
 
    def __str__(self) -> str:
        return f'{self.usuario} | {self.post}'        