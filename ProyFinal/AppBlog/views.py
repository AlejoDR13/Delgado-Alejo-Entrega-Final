from django.shortcuts import render, redirect
#Django login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

#CRUDS 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View
#AppBlog FORMULARIOS
from AppBlog.forms import CrearPelicula_form
#AppBlog MODELOS
from AppBlog.models import Peliculas
#AppUser MODELOS
from AppUsers.models import Avatar

from django.urls import reverse_lazy

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import get_user

#------------------------------------------------------------------------------------------------------
def inicio(request):
    return render(request, 'AppBlog/templates/AppBlog/inicio.html')

def sobremi(request):
    return render(request, 'AppBlog/templates/AppBlog/sobremi.html')

def searchpost(request):
    
    data = request.GET.get('titulo', "ERROR")
    print(data)
    error = "ERROR"
    img = None


    if data:
        try:

            peliculas = Peliculas.objects.get(titulo=data)

            return render(request, 'AppBlog/showing.html', {"data": peliculas, "titulo": data, 'img': img})

        except Exception as exc:

            error = "¡Lo lamentamos! No se ha encontrado la pelicula que buscabas."

    return render(request, 'AppBlog/showing.html', {"error": error, 'img': img})

def ver_post(request, titulo):

        readPost = Peliculas.objects.get(titulo=titulo)

        try:
            commentsPost = Comment.objects.filter(post=titulo)

            if request.user.username:

                avatar = Avatar.objects.filter(user=request.user)

                if len(avatar) > 0:

                    img = avatar[0].imagen.url
                
                else:

                    img= None
        
            else:

                img = None

        except:

            commentsPost = None

            if request.user.username:

                avatar = Avatar.objects.filter(user=request.user)

                if len(avatar) > 0:

                    img = avatar[0].imagen.url

                else:
                    img=None
            else:
                img=None

        return render(request, 'AppBlog/templates/AppBlog/post.html', {'post': readPost, 'img': img, 'comentarios': commentsPost})

class PeliculaCreateView(LoginRequiredMixin, CreateView):
     model = Peliculas
     template_name = "AppBlog/templates/AppBlog/crearpelicula.html"
     form_class = CrearPelicula_form
     success_url = reverse_lazy('AppBlog:ListaPelicula')
     login_url = reverse_lazy('AppUsers:Login')
     
     def get_initial(self):
        return {'usuario_post':self.request.user, 'email':self.request.user.email}
class PeliculasListView(ListView):

    template_name = "AppBlog/templates/AppBlog/peliculaslistar.html"

    model = Peliculas
    queryset = Peliculas.objects.all()
    paginate_by = 9  # if pagination is desiredcd
    fields= "__all__"


class PeliculaDetailView(DetailView):

    model = Peliculas
    template_name = "AppBlog/post.html"   
    fields= "__all__"     

class PeliculaUpdateView(UpdateView):
    model = Peliculas

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash

    success_url = reverse_lazy('AppBlog:ListaPelicula')
    fields = ['usuario_post',
    'autor',
    'email',
    'titulo', 
    'direccion', 
    'estreno', 
    'duracion_en_min',
    'Primer_cuerpo',
    'Segundo_cuerpo',
    'Primer_imagen',
    'Segunda_imagen',]


class PeliculaDeleteView(DeleteView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('cursos_list/', views.CursoList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Peliculas
    success_url = reverse_lazy('AppBlog:ListaPelicula')

@login_required
def leavecomment(request, titulo):


    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:

        img = avatar[0].imagen.url

    else:

        img = None

    if request.method =='POST':

        miComment = LeaveComment_form(request.POST)

        if miComment.is_valid():

            content = miComment.cleaned_data

            pelicula = Peliculas.objects.filter(titulo=titulo)

            pelicula = pelicula[0].titulo

            comment = Comment(usuario=content['usuario'], body=content['body'], pelicula = pelicula)

            comment.save()

            postslist = Peliculas.objects.all().order_by('-fecha')

            return render(request, 'AppBlog/templates/AppBlog/peliculaslistar.html', {'postlist': postslist, 'img': img})
    
    else:

        pelicula = Peliculas.objects.filter(titulo=titulo)

        pelicula = pelicula[0].titulo

        miComment = LeaveComment_form(initial={'usuario':request.user, 'pelicula':pelicula})

    return render(request, 'AppBlog/leavecomment.html', {'miComment': miComment, 'img': img})

#--------------------------------------------------------------------------------------------------------------------------------

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Peliculas.objects.get(pk=pk)

        is_dislike=False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if is_dislike:
            post.dislikes.remove(request.user)

        is_like=False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    login_url = reverse_lazy('AppUsers:Login')
        
class AddDislike(LoginRequiredMixin,View):
    def post(self,request, pk, *args, **kwargs):
        post = Peliculas.objects.get(pk=pk)   

        is_like=False
        for like in post.dislikes.all():
            if like == request.user:
                is_like = True
                break
        
        if is_like:
            post.likes.remove(request.user)

        is_dislike=False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    login_url = reverse_lazy('AppUsers:Login')
