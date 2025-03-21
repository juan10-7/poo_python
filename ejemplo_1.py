# Clase persona
class persona:
    # método constructor
    def __init__(self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad

    #método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("nombre: "+ self.Nombre)
        print("apellidos: " + self.Apellidos)
        print("edad: " + str(self.Edad))

# metodo principal
def main():
    p1 = persona("juan", "cala", 15)
    p1.MostrarPersona()
    p2 = persona("jorge", "luis", 49)
    p2.MostrarPersona()
    p1.Edad = 15
    p1.MostrarPersona()
    p1 = p2
    p1.MostrarPersona()
    p2.MostrarPersona()

if __name__ == "__main__":
    main()















