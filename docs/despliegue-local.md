## Configurar el Proyecto en un ambiente local

Los siguientes pasos lograran la configuracion minima nesesaria en un entorno de desarrollo local. Suponemos que se tiene instalado lo siguiente :

* pip
* virtualenv

Con los requerimientos cumplidos, hay que crear y activar un entorno virtual

```bash
$ virtualenv miemma
$ source miemma/bin/activate
```

Una ves activado el entorno, hay que instalar los requerimientos de la aplicacion, una ves posicionados dentro de la carpeta principal del proyecto ejecutamos los siguientes comandos

```bash
$ pip install -r requirements/local.txt
```

Ya instalados los requerimientos habra que sincronizar la base de datos, en desarrollo se esta usando una base de datos pequeña con sqlite3

```bash
$ python manage.py migrate
```

Para el correcto funcionamiento del proyecto deberan exportarse las siguientes variables de entorno, en caso de nesesitar llaves de apis externas o similares, solicitarlas a alguno de los administradores

* DJANGO_SETTINGS_MODULE=config.settings.local
* DJANGO_DEBUG=True

Finalmente queda lanzar el servidor de desarrollo y empezar a codear

```bash
$ python manage.py runserver
```
