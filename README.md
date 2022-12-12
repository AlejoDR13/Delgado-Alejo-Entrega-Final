# PeliBlog - Entrega Final (Coderhouse)
## Descripción 
PeliBlog consiste en un Blog de Peliculas donde los usuarios pueden postear opiniones, comentarios, reseñas sobre lo que deseen dando la información correspondiente de la pelicula de la cual habla su posteo. Dicha web tiene administradores, perfiles de usuarios donde se puede visualizar la informacion personal junto con su correspondiente avatar, para poder reaccionar o interactuar se debe estar logueado por lo tanto cuenta con registros para quien quiera aportar o interactuar, de no ser así, cualquier persona podrá simplemente visualizar el Blog como lo desee. 

Todos los usuarios tienen la posibilidad de likear, o dislikear los posts, de crear un post, de comentarlo y de alterar su información de perfil como la desee. A diferencia de un administrador, que el mismo tiene la posibilidad de editar cualquier post independientemente sea o no de su pertenencia, de eliminarlos, y contar con una opción del panel de administrador que posee django.  

En resumen, el proyecto consiste en la implementación de Django/Python para crear un Blog con funcionalidades que deben cumplir los requisitos que se plantean en las consignas asignadas para el proyecto final segun CorderHouse. 

![Logo](https://avatars.githubusercontent.com/u/116843946?s=400&u=91949b295a9524968148fba6ea4d66edfec1a40a&v=4)

## 👨 Autor
###- Delgado Alejo
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
C:\Users\...\>cd \Proyecto

pip install virtualenv
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

Se mostrara a grandes rasgos como estan conectadas estas dos aplicaciones y su correspondiente información mediante DBeaver.
### Diagrama ER

<img src="/DB.png">

### Aplicación del Blog (AppBlog)

#### 📊 Modelos

####🔑 Peliculas

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

####🔑 Comment

|    Campo      |   Tipo        |
| ------------- | ------------- |
|    usuario     |   ForeignField   |
|   comentario   |   TextField   |
|     fecha   |   DateTimeField   |
|   post   |  CharField  |

### Aplicación de Usuarios (AppUsers) 

#### 📊 Modelos

####🔑 Avatar

|    Campo      |   Tipo        |
| ------------- | ------------- |
|    user    |   ForeignField   |
|   imagen   |   ImageField   |

####🔑 UserAbout

|    Campo      |   Tipo        |
| ------------- | ------------- |
|    user     |   ForeignField   |
|   bio   |   TextField   |
|     instagram   |   URLField   |
|     facebook   |   URLField   |
|     twitter   |   URLField   |
