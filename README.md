# PeliBlog - Entrega Final (Coderhouse)
## Descripción 
PeliBlog consiste en un Blog de Peliculas donde los usuarios pueden postear opiniones, comentarios, reseñas sobre lo que deseen dando la información correspondiente de la pelicula de la cual habla su posteo. Dicha web tiene administradores, perfiles de usuarios donde se puede visualizar la informacion personal junto con su correspondiente avatar, para poder reaccionar o interactuar se debe estar logueado por lo tanto cuenta con registros para quien quiera aportar o interactuar, de no ser así, cualquier persona podrá simplemente visualizar el Blog como lo desee. 

Todos los usuarios tienen la posibilidad de likear, o dislikear los posts, de crear un post, de comentarlo y de alterar su información de perfil como la desee. A diferencia de un administrador, que el mismo tiene la posibilidad de editar cualquier post independientemente sea o no de su pertenencia, de eliminarlos, y contar con una opción del panel de administrador que posee django.  

En resumen, el proyecto consiste en la implementación de Django/Python para crear un Blog con funcionalidades que deben cumplir los requisitos que se plantean en las consignas asignadas para el proyecto final segun CorderHouse. 

![Logo](https://avatars.githubusercontent.com/u/116843946?s=400&u=91949b295a9524968148fba6ea4d66edfec1a40a&v=4)

## 👨 Autor: Delgado Alejo

### 📱 Redes

[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alejo-alfredo-angel-delgado-129b291b5/)

[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AlejoDR13)

[![email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](alejodelgado199999@gmail.com)

[![instragram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/alejo.d13/)

## 🎞 Demo
Enlace del video demostrativo, donde se puede observar en menos de 10min todas las funcionalidades con las que cuenta el Blog:
[Demo](https://youtu.be/9diSZ3uwdcQ)

## Techs

🛠️ Python (Version 3.7.0)

🛠️ Django (Version 3.2.16)

🛠️ HTML

🛠️ CSS

## Instalacion git clone

Para acceder al proyecto clonándolo, deberás ejecutar en consola: 
```sh
git clone https://github.com/AlejoDR13/Delgado-Alejo-Entrega-Final.git
```

## Instalación y ejecución del proyecto

En primer lugar nos posicionamos en el directorio donde hemos almacenado el proyecto, e instalamos nuestro entorno virtual
```sh
C:\Users\...\> cd \Proyecto

C:\Users\...\Proyecto> pip install virtualenv
```
Le asignamos un nombre a nuestro entorno

```sh
C:\Users\...\Proyecto> virtualenv env
```

Y luego lo activamos a nuestro entorno local

```sh
C:\Users\...\Proyecto>env\Scripts\activate

(env) C:\Users\...\Proyecto>
```
Posteriormente, nos posicionamos en el directorio correspondiente en el que se encuentra el proyecto

```sh
(env) C:\Users\...\Proyecto> cd ProyFinal

(env) C:\Users\...\Proyecto\ProyFinal>
```

Llegado a este punto y considerando que se ha instalado django, para poder visualizar el Blog basta con utilizar el siguiente comando

```sh
(env) C:\Users\...\Proyecto\ProyFinal> py manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 12, 2022 - 14:14:27
Django version 3.2.16, using settings 'ProyFinal.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Ingresando en http://127.0.0.1:8000/ nos redireccionara al inicio de PeliBlog 🚀

## Backend 

El proyecto consta de dos aplicaciones, una dedicada a la estructura general del Blog, es decir; el inicio, mostrar los posts en una galeria, crear posts, sistema de likes, comentarios, etc. Y la otra aplicación consiste en administrar el registro, inicio de sesión, información de los usuarios en general. 

### Aplicación del Blog (AppBlog)

### 📊 Modelos

#### 🔑 Peliculas

|    Campo      |   Tipo        |
| ------------- | ------------- |
|    usuario_post     |   ForeignField   |
|   autor   |   CharField   |
|     email   |   EmailField   |
|   fecha   |  DateField  |
|   titulo    |   CharField   |
|   genero    |   CharField   |
|   direccion    |   CharField   |
|   estreno    |   DateTimeField   |
|   duracion_en_min    |   IntegerField   |
|   Primer_cuerpo    |   TextField   |
|   Segundo_cuerpo    |   TextField   |
|   Primer_imagen    |   ImageField   |
|   Segunda_imagen    |   ImageField   |
|   likes    |   ManyToManyField   | 
|   dislikes    |   ManyToManyField   |  

#### 🔑 Comment

|    Campo      |   Tipo        |
| ------------- | ------------- |
|    usuario     |   ForeignField   |
|   comentario   |   TextField   |
|     fecha   |   DateTimeField   |
|   post   |  CharField  |


### 📊 Vistas

Se implemento el uso de Vistas Basadas en Clases y Vistas Basadas en Funciones según se vio conveniente. Las mismas se resumen junto con la función que realizan acontinuación:

```sh
> def inicio(request):... #### Renderizar el inicio junto con los datos de usuario y del avatar correspondiente.

>def sobremi(request):... #### Renderizar la pagina "Sobre mi" junto con los datos de usuario y del avatar correspondiente.

>def searchpost(request):... #### Renderiza la pagina de Busqueda, realiza un request con lo que se desea obtener, junto con los datos de usuario y del avatar correspondiente.

>class PeliculaCreateView(LoginRequiredMixin, CreateView):... #### Solicita un inicio de sesión en primer lugar, luego renderiza el .html donde se crea el post que el usuario desee, junto con los datos de usuario y del avatar correspondiente.

>class PeliculasListView(ListView):... #### No solicita un inicio de sesión ya que solo nos renderiza el .html donde observan los posts creados por otros usuariose, y si esta logueado se pasa por contexto tambien los datos de usuario y del avatar correspondiente.

@login_required(login_url='AppUsers:Login')
>def leavecomment(request, titulo):... #### Solicita un inicio de sesión en primer lugar, luego renderiza el .html donde se escribe el comentario que el usuario desee, junto con los datos de usuario y del avatar correspondiente

>class PeliculaDetailView(DetailView):... #### No solicita un inicio de sesión ya que solo nos renderiza el .html donde se observan los detalles del posteo, los likes, dislikes, comentarios y nos solicitara iniciar sesión si deseamos interactura, si esta la sesión iniciada tambien se pasara por contexto los datos de usuario y del avatar correspondiente.

>class PeliculaUpdateView(UpdateView):... #### Opción que solamente observa alguien con permisos de administrador, renderiza el .html que nos permite modificar los campos de los posteos, junto con los datos de usuario y del avatar correspondiente. 

>class PeliculaDeleteView(DeleteView):... #### Opción que solamente observa alguien con permisos de administrador, renderiza el .html que nos avisa que posteo se esta por eliminar, y nos da la posibilidad de volver o ejecutar la acción, junto con los datos de usuario y del avatar correspondiente.

>class AddLike(LoginRequiredMixin, View):... #### Solicita un inicio de sesión en primer lugar, una vez realizado nos permite ejecutar la acción de dar Like a un post en especifico modificando asi el contador de likes, junto con los datos de usuario y del avatar correspondiente.

>class AddDislike(LoginRequiredMixin, View):... #### Solicita un inicio de sesión en primer lugar, una vez realizado nos permite ejecutar la acción de dar Lislike a un post en especifico modificando asi el contador de dislikes, junto con los datos de usuario y del avatar correspondiente.

>def aviso(request):... #### Renderiza una pagina que da aviso de que hay alguna funcionalidad no disponible en el Blog, junto con los datos de usuario y del avatar correspondiente.
```

### Aplicación de Usuarios (AppUsers) 

### 📊 Modelos

#### 🔑 Avatar

|    Campo      |   Tipo        |
| ------------- | ------------- |
|    user    |   ForeignField   |
|   imagen   |   ImageField   |

#### 🔑 UserAbout

|    Campo      |   Tipo        |
| ------------- | ------------- |
|    user     |   ForeignField   |
|   bio   |   TextField   |
|     instagram   |   URLField   |
|     facebook   |   URLField   |
|     twitter   |   URLField   |

### 📊 Vistas

Se implemento el uso de Vistas Basadas en Clases y Vistas Basadas en Funciones según se vio oportuno, pero en el caso de la Aplicacion de Usuarios, se implemento solamente Vistas Basadas en Funciones. Las mismas se resumen junto con la función que realizan acontinuación:

```sh
> def login_request(request):... #### Encargado del inicio de sesion se hace uso del formulario que brinda Django 'AuthenticationForm', siendo los datos correctos redirecciona al inicio, sino muestra el correspondiente error

>def register_request(request):... #### Haciendo uso formulario creado en forms.py con sus respectivas modificaciones en las que consiste realizar una validación de usuarios ya existentes, no permitiendo crear una nueva cuenta si ya existe un usarname o email en uso en el blog. El formulario modificado en cuestión es 'UserCreationForm'.

@login_required
>def edituser_request(request):... #### En primer lugar exije un inicio de sesión ya que solo podran modificar la información de usuario solo quienes esten ya registrados, luego validando la información de avatar correspondiente y un metodo de solicitud de posteo, se llama y hace uso de los formularios UserEdit_form y AboutUser_form para modificar la información de usuario. 

@login_required
>def add_avatar(request,):... #### Similar a lo anterior, ya que requiere de una cuenta para poder ser ejecutado, pero en este caso se hace uso del formulario Avatar_form para agregar una imagen Avatar. 

@login_required
>def open_profile(request):... #### Permite al usuario poder visualizar su perfil personal, donde podra encontrar toda su información correspondiente y la posibilidad de modificarla tambien. 

>def open_user_profile(request, usuario):... #### Permite a alguien que no es usuario y a los usuarios tambien, poder visualizar el perfil de otra cuenta que este disponible en el Blog. Para estas dos ultimas funciones se hizo uso de un formulario llamado 'AboutUser_form' que nos permite solicitar la información sobre el usuario correspondiente.
```


Se mostrara a grandes rasgos como estan conectadas estas dos aplicaciones y toda la información que nos brinda django con respecto a las tablas de usuarios, administradores, persmisos, etc., mediante DBeaver.

### Diagrama ER

<img src="/DB.png">

Se pueden observar las entidades relacionadas entre si, esto nos brinda una visión mas dinamica de como los datos interactuan entre si, como estan correlacionados, etc. 

### Agradecimientos

En un principio agradecer a Daniel Ochoa, profesor que nos acompaño con paciencia brindandonos conocimientos, y ganas de enseñar de principio a fin en el transcurso del curso. Agradecimientos especialmente a mi tutor Pablo David Schvager por la disposición a ayudar siempre que se pudo. Y a CoderHouse por la posibilidad de aprender Python mediante un curso dinamico y en un plazo de tiempo relativamente corto. 
