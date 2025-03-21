# composición

"""una cordenada en dos dimensiones esta compuesta por dos valores el valor en el eje de las x y el valor en el eje de las y, esto podría ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que són los cuatro vértices, esto podria ser una clase que esta compuesta por cuatro clases del objeto ordenado."""

# clase coordenada


class Coordenadas:

    # metodo constructor
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    # metodos de lectura y escritura de cada atributo
    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y
    
    def setX(self, x):
        self.__X = x

    def sety(self, y):
        self.__Y = y

    # metodo para mostrar coordenada
    def mostrarCoordenada(self):     
        print("(", self.__X, "," , self.__Y, ")")


# clase cuadrado
class Cuadrado:

    # metodo constructor
    def __init__(self,v1, v2, v3, v4):
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    # metodos privados para mostrar los vertices
    def _mostrarCoordenadaV1(self):
        print("(", self.__V1.getX(), ",", self.V1.getY(), ")")

    def _mostrarCoordenadaV2(self):
        print("(", self.__V2.getX(), ",", self.V2.getY(), ")")

    def _mostrarCoordenadaV1(self):
        print("(", self.__V3.getX(), ",", self.V3.getY(), ")")

    def _mostrarCoordenadaV1(self):
        print("(", self.__V4.getX(), ",", self.V4.getY(), ")")




    # metodo para mostrar vertices
    def mostrarVertices(self):
        print("El cuadrado está compuesto por los siguientes vertices: ")
        self.__V1.mostrarCoordenada()
        self.__V2.mostrarCoordenada()
        self.__V3.mostrarCoordenada()
        self.__V4.mostrarCoordenada()

# metodo principal del modulo
def main():
    # input
    x1 = int(input("digite el valor de x: "))
    x2 = int(input("digite el valor de y: "))

    # processing
    c1 = Coordenadas(x1,x2)
    c1.mostrarCoordenada()

    v1 = Coordenadas(7,8)
    v2 = Coordenadas(10,8)
    v3 = Coordenadas(7,5)
    v4 = Coordenadas(10,5)

    Cuadrado1 = Cuadrado(v1, v2, v3, v4)
    Cuadrado1.mostrarVertices()

    # que ocurre si el metodo getX() lo hacemos privado: __getX()7
    
 
if __name__ == "__main__":
    main()

