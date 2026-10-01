Primero que nada asegurate de que tengas lista tu configuración personal de **git**, esto es, tu username y correo (de preferencia que sean los mismos que los de tu cuenta de GitHub).
En caso de que no lo tengas configurado, usa los siguientes comandos:
```bash
git config --global user.email "email"
git config --global user.name "name"
```

Ahora, tendrás que aceptar la invitación que se te hizo al repositorio. Para esto **entra** a la notificación que te llegó y ahí aceptala, de esta forma ya podrás entrar al repositorio para ver los archivos que se subieron a ese momento. 

Ya que eres colaborador, lo siguiente sería clonar los archivos del repositorio directo a tu computadora. Crea una carpeta que solo esté destinada a este proyecto y abre la terminal de git bash dentro de la carpeta. Teclea ```git init``` y luego ```git clone url```. La url la encontrarás en el botón verde que verás en la página principal del repositorio, bajo el apartado de HTTPS. Ahora deberías ver que los archivos que se encuentran en el repositorio también están en la carpeta que creaste para el proyecto.

A partir de aquí todo el trabajo se hará dentro de la carpeta  ```security-tool```.

Ahora, para que puedas añadir tu código y actualizar tu repositorio local según vayamos avanzando al proyecto tienes que conectar el repositorio a tu directorio destinado para el proyecto (el que se te creó cuando hiciste el clone). Para esto ejecuta el siguiente comando: ```git remote add origin <url>``` donde la url es la misma que ya debiste haber usado anteriormente.

Para probar que todo funcione, crea un archivo de texto y haz el git workflow convencional para cualquier archivo creado, esto es: add, commit (agrega un comentario al commit que especifique que ese archivo solo es de prueba o algo así) y por último, para que este se suba al repositorio ```git push origin master```. Si ningún error emerge, actualiza en tu navegador el repositorio de GitHub e inmediatamente deberías ver tu archivo ahí.

Finalmente, para ir descargando las actualizaciones que los demás hagan en el repositorio, usa el comando ```git pull origin master```.

A partir de aquí solamente usarás git pull y push a secas, ya no es necesario agregar ```origin master```.

#### Comandos
_______
git add \<archivo\>: se usa inmediatamente después de modificar un archivo.
git commit -m "comentario": commit al archivo
git push: sube tu archivo (después del commit) al repositorio
git pull: te descarga los archivos que han sido modificados por los demás (que se encuentran en el repositorio de GitHub) a tu carpeta local.
