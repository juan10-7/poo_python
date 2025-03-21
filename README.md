# poo en python

- El paredigma de POO esta basado en una abstraccion del mundo real que nos va a permiti desarrollar programas de forma mas cercana a como vemos el mundo pensando en objetos que tenemos delante y acciones que podemos hacer con ellos

## clase

- una clase es un tipo de datos cuyas variables se llaman objetos o instancias - la clase es la definicion del mundo real y los objetos o instancias son el propio objeto de mundo real

- las clases estan compuestas por dos elementos:atributos y métodos

### atributos
- información que almacena la clase

### métodos
- operaciones que pueden realiza las clases

## definion de una clase en python
```python
class NombreClase:
    def_init_(self, variable1, variable2):
       self.Atributo1 = valor1
       self.Atributo2 = valor2

    def nombreMetodo(self):
    bloqueCodigo
```
### Componentes

```class```: palabra  reservada en python para definir una clase.
```NombreClase```: nobre de la clase que quieres crear
```def```: palabra reservada en python que se utiliza para definir tanto el constuctor de la clase (método que se ejecuta la primera vez que usas una clase) como los diferente métodos que tiene.
```_init_```:palabra reservada en python para defir el método constructor de la clase. es lo primero que se ejecuta cuando creas un objeto de una clase.
```(self,variablex)```: parametro del constructor de la clase el para mettro self es obligatorio y despues puedes tener tantos parametros como quieras. La forma de añadir parametros es la misma que las funciones.

```self.Atributox```:forma de utilizacion y acceso a los atributos de la clase.

```nombreMetodo```:nombre del metodo de la clase

```(self)```:parametro del metodo. El parametro self es obligatorio y despues puedes ener todos los parametros que quieras. la forma de añadir parametros es la misma que en funciones.

```bloqueCodigo```: instrucciones que ejecutara el metodo.

-cuando defines una clase debes tener en cuenta los siguientes puntos:
  - puedes definir tantoa atributos como necesites.
  - puedes definir tantos metodos como necesites.
  - pudes definir tantos parametros en el contructor y en los meetodos como necesites.


## composición
- consiste en la creación de nuevas clases a partir de otras clases ya existentes que ayudan como elementos compositores de la nueva.
- las clases existentes seran atributos de la nueva clase.
- en poo la compisicion significa que entre las dos clases existe una relación e tipo "tiene un".
- Ejemplo:
    - una coorenada en dos dimensiones esta compuesta por dos valores el valor en el eje de lasx y el valor en el eje de las y, esto podría ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que són los cuatro vértices, esto podria ser una clase que esta compuesta por cuatro clases del objeto ordenado.


## Encapsulación
- Se trata de la protección de los datos de usos o accesos no controlados.
- Los datos (atributos) que componen una clase pueden ser de dos tipos:
    - Públicos:  los datos son accesibles sin control, es decir, los datos pueden ser usados sin ningún tipo de mecanismo que proteja ante usos no autorizados o indebidos.
    - Privados: los datos no pueden ser accedidos sin control y para acceder a ellos se deberá implementar un método que acceda a ellos.  De esta forma, los datos serán accedidos única y directamente por la propia clase.
- La encapsulación no solo puede realizarse sobre los atributos de la clase, también es posible realizarla sobre los métodos, es decir, aquellos métodos que indiquemos que son privados no podrán ser utilizados por elementos externos al propio objeto.
- La definición de atributos privados se realiza incluyendo los caracteres "__" (dos guiones de piso) entre la palabra "self" y el nombre del atributo.

## Herencia
- Permite la reutilización de código.
- Consiste en la definición de una clase utilizando como base una clase ya existente.
- La nueva clase derivada tendrá todas las caracteristicas de la clase base y ampliará el concepto de esta, es decir, tendrá todos los atributos y métodos de la clase base.
- Significa que entre dos clases existe una relación del tipo "es un".
- La herencia en Python se especifica de la siguiente manera: ```class NombreClase(ClaseBase):```
- Ejemplo:
    - Pensemos en una persona como una clase, la persona tendría una serie de atributos como pueden ser el nombre, los apellidos, la edad, etc.  Esas características de una persona serían compartidas por todas aquellas clases hijas como pueden ser alumno y profesor.  Es decir, alumno y profesor heredarían las propiedades de la clase persona y tendrían sus propias propiedades, diferentes entre ellas, como por ejemplo el curso en el que está el alumno y el horario de tutorias del profesor.

    - Clase base: Persona
        - Atributos:
            - Nombre
            - Apellidos
            - Edad

    - Clase derivada: Alumno
        - Atributos:
            - Curso
            - Asignaturas
    
    - Clase derivada: Profesor
        - Atributos:
            - Antigüedad
            - Tutorias
            - Teléfono

## Actividad:
- Consulte un ejemplo práctico del uso de herencia múltiple en Python

### Bibliografía
Moreno, A. y Córcoles, S.  (2020).  Python práctica.  Herramientas, conceptos y técnicas.  Ediciones de la U.



