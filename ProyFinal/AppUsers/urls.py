from django.urls import path
from AppUsers.views import *

from django.contrib.auth.views import LogoutView

AppUsers_patterns =([
    #Inicio, registro y salida de usuario
    path('accounts/login/', login_request, name='Login'),   
    path('accounts/singup/', register_request, name='Register'),     
    path('accounts/logout/', LogoutView.as_view(template_name='AppUsers/templates/AppUsers/logout.html'), name='Logout'),

    #Edicion de usuario
    path('accounts/edituser/', edituser_request, name="EditarPerfil"),
    path('accounts/addavatar/', add_avatar, name='addAvatar'),

    #Abrir Perfil de usuario
    path('accounts/profile/', open_profile, name='Profile'),
    path('accounts/userprofile/<usuario>', open_user_profile, name='OpenProfile'),

],'AppUsers')



