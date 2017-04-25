
# Relationships between elements of sets

Project for Discrete Structures

Automatically deployed to:
```sh
 https://relations-project-stage.herokuapp.com/ 
 ```

 # Documentacion

## Uso
 En el campo de "Conjunto" debera incluirse una lista de elementos (Numeros, letras o cadenas) separadas por coma. Los elementos son sensibles a mayusculas por lo que es diferente el elemento "Hola" de "hola".

En los campos de elementos deberan ingresarse los elementos antes definidos separados por coma, en caso de no pertencer alguno o ambos de los elementos se mostrara un mensaje de error para que sea corregido.

Para agregar mas parejas debera presionar el boton de "Agregar" el cual agregara mas casillas para poder ingresar mas relaciones. El numero de relaciones no tiene limite.

Para ver las propiedades de las relaciones debera presionar el boton "Enviar" el cual enviara los datos por medio de una peticion a nuestro servidor y retornando los valores correspondientes que seran inmediatamente mostrados debajo.

Podra repetir estre proceso para N numero de relaciones y/o conjuntos.

Para limpiar los datos y regresar al estado inicial es tan facil como presionar el boton "Limpiar".


## Descripción del proyecto

La carpeta ENV es un entorno virtual para poder correr el proyecto de manera local utilizando Heroku con el comando "heroku local" esto es necesario
porque nuestro repositorio automaticamente es sincronizado desde el Dashboard de Heroku por lo cual los cambios se refljean en cuestion de minutos en la aplicacion web en linea.

Para correr el proyecto en local en cualquier computadora es necesario:

tener python 2 o 3 instalado
tener pip instalado 

y correr los comandos:
```sh
pip install requirements.txt
 ```
 lo cual instalara lo necesario de "Flask" y posterioromente

 ```sh
 python app.py 
 ```

 Lo cual inicializa la aplicacion y la corre en "localhost" ahora solo debemos entrar a la direccion en consola y estamos listos para usar la aplicacion en local.

  Recordar que ya se encuentra en linea para su comoidad:

  ```sh
 https://relations-project-stage.herokuapp.com/ 
 ```


 

