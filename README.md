
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

> - tener python 2 o 3 instalado
> - tener pip instalado 

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

## Funcionamiento de los algritmos en relaciones.py

La forma en cómo se verifican las propiedades para cada relación ingresada, es en base a una matriz de adyacencia, la cual es generada por la función 'createBinaryMatrix’, que toma como parámetros un conjunto y las relaciones ingresadas, representando un 1 si están relacionados dos elementos y un 0 si no.
Una ves generada la matriz, tenemos que:

> - La reflexividad comprobada por la función ‘isReflexive’ verifica que en la diagonal principal todo elemento del conjunto se encuentre relacionado con sí mismo, o sea [i][i] = 1, para todo i.

> - La irreflexividad es el caso contario, la función ‘isIrreflexive’  verifica que ningún elemento del conjunto esté relacionado consigo mismo.

> - Para comprobar si es simétrica, la función ‘isSymmetric’ verifica que para toda relación [i][j]=1 en la matriz, exista también [j][i]=1.

> - Su caso contrario, para ver si la matriz es asimétrica, la función ‘isAsimetric’ verifica que para toda relación [i][j]=1, no exista [j][i]=1.

> - Para ver si es antisimétrica, la función ‘isAntisymmetric’, comprueba que si [i][j]=1 y [j][i]=1, entonces j=i.

> - Finalmente, la transitividad comprobada por la función ‘isTransitive’, verifica que si [i][j]=1 y [j][k]=1, entonces [i][k]=1, para todo i,j,k.

 

