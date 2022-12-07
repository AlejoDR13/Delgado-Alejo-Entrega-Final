from django.db import models
from django.contrib.auth.models import User

#MODELOS DE USUARIOS
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f'{self.user} | Avatar'

class UserAbout(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    bio = models.TextField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return f'{self.user} | About'
