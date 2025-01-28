class DistanciaEntrePuntos:
    #Declaración de propieedades
    x1=0
    x2=0
    y1=0
    y2=0
    res=0
    #Declaración del constructor this
    def __init__(self):
        self.x1=0
        self.x2=0
        self.y1=0
        self.y2=0
    #Declaración de metodos de clase
    def distancia(self):
        self.res=((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)**(1/2)
        print("La distancia entre los puntos es: {}".format(self.res))

    def pedirDatos(self):
        self.x1 = int(input("Introduce la coordenada x1: "))
        self.x2 = int(input("Introduce la coordenada x2: "))
        self.y1 = int(input("Introduce la coordenada y1: "))
        self.y2 = int(input("Introduce la coordenada y2: "))

def main():
    obj = DistanciaEntrePuntos()
    obj.pedirDatos()
    obj.distancia()

if __name__ == "__main__":
    main()