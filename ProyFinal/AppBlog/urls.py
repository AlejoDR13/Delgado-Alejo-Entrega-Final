from django.urls import path, re_path
from AppBlog.views import *

AppBlog_patterns =([
    path('', inicio, name="Inicio"),
    path('sobremi/', sobremi, name="Sobremi"),
    path('showing/', searchpost, name='BuscarPost'),    
    path('commentform/<pk>', leavecomment, name='NewComment'),
    #CRUDS
    path('pelicula_detail/<pk>', PeliculaDetailView.as_view(), name="DetallePelicula"),   
    path('pelicula_edit/<pk>', PeliculaUpdateView.as_view(), name='UpdatePelicula'),    
    path('pelicula_confirm_delete/<pk>', PeliculaDeleteView.as_view(), name='DeletePelicula'),
    path('add_pelicula/', PeliculaCreateView.as_view(), name="AgregarPelicula"),
    path('view_pelicula/', PeliculasListView.as_view(), name="ListaPelicula"),  
],'AppBlog')