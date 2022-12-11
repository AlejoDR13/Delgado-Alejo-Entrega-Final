from django.contrib import admin
from AppBlog.models import Peliculas, Generos, Comment

admin.site.register(Generos)
admin.site.register(Peliculas)
admin.site.register(Comment)