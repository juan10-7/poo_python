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









