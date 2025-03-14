# composición

"""una cordenada en dos dimensiones esta compuesta por dos valores el valor en el eje de las x y el valor en el eje de las y, esto podría ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que són los cuatro vértices, esto podria ser una clase que esta compuesta por cuatro clases del objeto ordenado."""

# clase coordenada

from typing import Self


class Coordenadas:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # metodo para mostrar coordenada
    def mostrarCoordenada(self):     
        print("(", self.X, "," , self.Y, ")")


# clase cuadrado
class Cuadrado:

    # metodo constructor
    def __init__(self,v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # metodo para mostrar vertices
    def mostrarVertices(self):
        print("El cuadrado está compuesto por los siguientes vertices: ")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()


# metodo principal
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



if __name__ == "__main__":
    main()












