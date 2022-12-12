import difflib
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
from AppBlog.forms import CrearPelicula_form, LeaveComment_form
#AppBlog MODELOS
from AppBlog.models import Peliculas, Comment
#AppUser MODELOS
from AppUsers.models import Avatar

from django.urls import reverse_lazy

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import get_user
#------------------------------------------------------------------------------------------------------
def inicio(request):

    if request.user.username:

        avatar = Avatar.objects.filter(user=request.user)

        usuario = request.user

        if len(avatar) > 0:

            img = avatar[0].imagen.url

        else:

            img = None

    else:

        img = None

        usuario = None

    return render(request, 'AppBlog/inicio.html', {'user': usuario, 'img':img})

def sobremi(request):
    
    if request.user.username:

        avatar = Avatar.objects.filter(user=request.user)

        usuario = request.user

        if len(avatar) > 0:

            img = avatar[0].imagen.url

        else:

            img = None

    else:

        img = None

        usuario = None

    return render(request, 'AppBlog/templates/AppBlog/sobremi.html', {'user': usuario, 'img':img})

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

class PeliculaCreateView(LoginRequiredMixin, CreateView):
    model = Peliculas
    template_name = "AppBlog/templates/AppBlog/crearpelicula.html"
    form_class = CrearPelicula_form
    success_url = reverse_lazy('AppBlog:ListaPelicula')
    login_url = reverse_lazy('AppUsers:Login')
    
    def get_initial(self):
       return {'usuario_post':self.request.user,'email':self.request.user.email}

    def get_context_data(self, *args, **kwargs ):

        avatar = Avatar.objects.filter(user=self.request.user)

        if len(avatar) > 0:
            img = avatar[0].imagen.url

        else:
            img = None

        context = super(PeliculaCreateView, self).get_context_data(**kwargs)
        context['img']=img
        return context   
        
class PeliculasListView(ListView):

    template_name = "AppBlog/templates/AppBlog/peliculaslistar.html"

    model = Peliculas, Avatar
    queryset = Peliculas.objects.all()
    paginate_by = 9 
    fields= "__all__"

    def get_context_data(self, *args, **kwargs ):

        if self.request.user.username:
        
                avatar = Avatar.objects.filter(user=self.request.user)

                usuario = self.request.user

                if len(avatar) > 0:
                
                    img = avatar[0].imagen.url

                else:
                
                    img = None

        else:
        
            img = None
            usuario = None

        context = super(PeliculasListView, self).get_context_data(**kwargs)
        context['img']=img
        context['usuario']=usuario
        return context
    
@login_required(login_url='AppUsers:Login')
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

            comment = Comment(usuario=request.user, comentario=content['comentario'], post = pelicula)

            comment.save()

            postslist = Peliculas.objects.all().order_by('-fecha')

            return render(request, 'AppBlog/templates/AppBlog/inicio.html', {'postlist': postslist, 'img': img})
    
    else:

        pelicula = Peliculas.objects.filter(titulo=titulo)

        pelicula = pelicula[0].titulo

        miComment = LeaveComment_form(initial={'usuario':request.user, 'post':pelicula})

    return render(request, 'AppBlog/commentform.html', {'miComment': miComment, 'img': img})

class PeliculaDetailView(DetailView):

    model = Peliculas
    template_name = "AppBlog/post.html"   
    fields= "__all__"     

    def get_context_data(self, *args, **kwargs ):
        pk = self.kwargs.get('pk')

        avatar = Avatar.objects.filter(user=self.request.user)

        if len(avatar) > 0:
            img = avatar[0].imagen.url

        else:
            img = None

        context = super(PeliculaDetailView, self).get_context_data(**kwargs)
        context = super(PeliculaDetailView, self).get_context_data(**kwargs)
        context['comentarios']=Comment.objects.filter(post=pk)
        context['img']=img

        return context   


class PeliculaUpdateView(UpdateView):
    model = Peliculas
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

    def get_context_data(self, *args, **kwargs ):

        avatar = Avatar.objects.filter(user=self.request.user)

        if len(avatar) > 0:
            img = avatar[0].imagen.url

        else:
            img = None

        context = super(PeliculaUpdateView, self).get_context_data(**kwargs)
        context['img']=img
        return context

class PeliculaDeleteView(DeleteView):
    model = Peliculas
    success_url = reverse_lazy('AppBlog:ListaPelicula')
    
    def get_context_data(self, *args, **kwargs ):

        avatar = Avatar.objects.filter(user=self.request.user)

        if len(avatar) > 0:
            img = avatar[0].imagen.url

        else:
            img = None

        context = super(PeliculaDeleteView, self).get_context_data(**kwargs)
        context['img']=img
        return context

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
        
class AddDislike(LoginRequiredMixin, View):
    def post(self,request, pk, *args, **kwargs):
        post = Peliculas.objects.get(pk=pk)   

        is_like=False
        for like in post.likes.all():
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
