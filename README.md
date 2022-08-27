# INFORMATORIO CHACO
## Proyecto Final 
### Aplicación web desarrollada con tecnología DJANGO


## Integrantes Grupo 6

- Di Blasio Sergio
- Silva Alan Federico
- Ramirez Heber Nahuel intento 4mil
- Benitez Damian Nicolas
- Laleff Alexis Martin
- Echaide Maximiliano
- Romano Cristian Julian


Proyecto Final Blog - Instituto Barranqueras UEGP N° 161.
Introducción

El siguiente repositorio público donde realizamos el desarrollo de la aplicación tipo Blog contiene una instalación de Django, es por esto que para que todo funcione correctamente y no se generen conflictos de versiones es necesario que se instale el archivo requierements.txt. Los pasos a seguir para esto los explicaremos más adelante.


>> Clonando el repositorio

En el directorio de trabajo, se debe crear una carpeta nueva. Podemos darle cualquier nombre a la carpeta pero es preferible que el nombre sea algo representativo al proyecto que estamos realizando.

Una vez creada, se debe ingresar a la misma y ejecutar los siguientes comandos en un terminal GIT:

git init
git clone https://github.com/federico42o/Proyecto-Final-Blog.git
git fetch origin
git checkout -b NombreDeRamaNueva

El último comando creará una rama nueva con el nombre que le demos, esto hace que tengamos una rama propia actualizada desde main.

El último comando se debe saltar si ya se creó una rama directamente desde GitHub. Si esto ya se tiene una rama, el comando a ustilizar es git checkout NombreDeRamaCreada (esto nos permite movernos a la rama que ya teniamos creada).

>> Solucionar los errores de clonado

Cuando clonas un repositorio, es posible que puedas encontrar algunos errores.

Si no puedes clonar un repositorio, revisa que:

    Puedas conectarte utilizando HTTPS. Para obtener más información, consulta la sección "Errores de clonado de HTTPS".
    Tienes permiso para acceder al repositorio que quieres clonar. Para obtener más información, consulta la sección "Error: Repositorio no encontrado".
    La rama predeterminada que quieres clonar aún existe. Para obtener más información, consulta "Error: El HEAD remoto se refiere a una ref inexistente, imposible registrar",

>> Instalando Dependencias

Una vez clonado el código, se deben instalar las dependencias descriptas en el archivo requeriments.txt, para ello debemos ejecutar el siguiente comando "pip install -r requirements.txt" en la consola posicionandonos en el directorio donde se encuentre este archivo.
Haciendo esto, se instalaran en el sistema o en el virtualenv que tengamos activado, los paquetes anotados en el archivo requirements.txt



>> Creación de la base de datos, migración y creación de superuser

Djando trae por defecto una base de datos llamadadb.sqlite la que nos daba la posibilidad de trabajar directamente ahí.
Pero nosostros utilizamos una base de datos Mysql para este proyecto.
Para instalar la base de datos en la aplicacion Instituto creamos una carpeta llamada "settings" la cual contiene las configuraciones de nuestro proyecto en dos archivos "base.py" y "local.py" este ultimo archivos es en donde esta la configuración de la base de dato de cada colaborardor en particular es por esto y para no generar conflictos con las migraciones que tenemos ingorado el archivo "local.py"
Para conectar Mysql con Django debemos seguir los siguientes pasos (copiarlos en el archivo local.py)

from .base import *
import os

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static")
),


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre de la base de datos',
        'USER': 'root',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Por último, se deben realizar las migraciones necesarias utilizando python manage.py makemigrations y python manage.py migrate para completar la configuración.

Para crear un nuevo superuser procederemos de la siguiente manera:

Con el entorno virtual activado, desde el terminal de Visual Studio Code ejecutamos :

"python manage.py createsuperuser"

El comando nos proporcionara un programa interactivo que nos pedirá ingresar un usuario, un correo electrónico y una contraseña.

Si presionamos enter sin haber ingresado nada cuando nos pide un usuario, toma por defecto el nombre de usuario del sistema. Sino podemos ingresar el nombre de usuario deseado.

Luego, nos pide un correo, el cual puede estar en blanco, ya que no se usa para acceder al panel administrativo.

La contraseña puede ser arbitraria, aunque si Django detecta que es una contraseña muy sencilla(números consecuitivos, todas letras min{usculas, etc) nos mostrará un mensaje diciendonos que la contraseña es debil y si qeuremos continuar con la misma, si queremos seguir con esa contraseña presionamos "y" y si por el contrario queremos cambiarla por una más segura presionamos "n". 

>> Probando el Servidor

Por último nos queda comprobar que todo funcione correctamente al levanatar el servidor, para ello debemos porsicionarnos a la altura del archivos "manage.py" y ejecutar el siguiente comando:

python manage.py runserver

Este comando abre el servidor en la dirección 127.0.0.1:8000/.

Si nos vamos a esa dirección en nuestro navegador, deberíamos ver la página por defecto de Django, con la leyenda:
The install worked successfully! Congratulations!

Si esto te aparece en el navegador significa que todo fue bien!!