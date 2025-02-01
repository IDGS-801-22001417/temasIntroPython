from io import open
import os

class ventaEntradas:
    precioEntradas = 12.00
    descuento1 = 0.10  
    descuento2 = 0.15
    descuentoTarjeta = 0.10

    def __init__(self):
        self.total_general = 0
        self.ventas = []
        self.personas = 0
        self.limite_boletos = 0
        self.boletos = 0
        self.total = 0
        self.contenido = "" 

    def iniciar(self):
        os.system('cls')
        print("\n**CINEPOLIS - Adquisicion de Entradas**")
        while True:
            opcion = input("\n1. Realizar compra\n2. Salir\n\nSeleccione una opcion: ")

            if opcion == "1":
                self.hacer_ventas()
            elif opcion == "2":
                self.finalizar_ventas()
                break
            else:
                print("ERROR \nIngrese una opcion valida")

    def hacer_ventas(self):
        nombre = input("Indique su nombre: ")

        self.personas = int(input("¿Cuántas personas asistiran? (Maximo 7 boletos por persona): "))
        while self.personas <= 0:
            print("ERROR: \nDebe haber al menos un asistente.")
            self.personas = int(input("¿Cuántas personas asistirán? (Maximo 7 boletos por persona): "))

        self.limite_boletos = self.personas * 7

        self.boletos = int(input(f"¿Cuántas entradas desea adquirir? (Maximo {self.limite_boletos}): "))
        while self.boletos <= 0 or self.boletos > self.limite_boletos:
            os.system('cls')
            print(f"ERROR \nDebe elegir entre 1 y {self.limite_boletos} entradas.")
            
            desea_corregir = input("¿Desea modificar la cantidad de personas o boletos? \n1. Personas\n2. Boletos\n").strip().lower()
            if desea_corregir == "1":
                self.personas = int(input("¿Cuántas personas asistiran? (Máximo 7 boletos por persona): "))
                while self.personas <= 0:
                    print("ERROR \nDebe haber al menos un asistente.")
                    self.personas = int(input("¿Cuántas personas asistiran? (Máximo 7 boletos por persona): "))

                self.limite_boletos = self.personas * 7
                self.boletos = int(input(f"¿Cuantas entradas desea adquirir? (Maximo {self.limite_boletos}): "))
            elif desea_corregir == "2":
                self.boletos = int(input(f"¿Cuantas entradas desea adquirir? (Maximo {self.limite_boletos}): "))

        self.total = self.boletos * self.precioEntradas
        if 3 <= self.boletos <= 5:
            self.total *= (1 - self.descuento1)
        elif self.boletos > 5:
            self.total *= (1 - self.descuento2)

        pago_tarjeta = input("¿Desea pagar con tarjeta CINECO? (SI/NO): ").strip().lower()
        while pago_tarjeta not in ["si", "no"]:
            print("ERROR: \nIngrese 'SI' o 'NO'.")
            pago_tarjeta = input("¿Desea pagar con tarjeta CINECO? (SI/NO): ").strip().lower()

        if pago_tarjeta == "si":
            self.total *= (1 - self.descuentoTarjeta)

        self.total_general += self.total
        venta = f"{nombre} - {self.boletos} boletos - Total: ${self.total:.2f}"
        self.ventas.append(venta)
        
        os.system('cls')
        print(f"Total a pagar para {nombre} ({self.boletos} boletos): ${self.total:.2f}")
        self.actualizar_archivo(venta)

    def actualizar_archivo(self, nueva_venta):
        modo = "w" if len(self.ventas) == 1 else "a"
        with open("ventas.txt", modo) as ticket:
            ticket.write(nueva_venta + "\n")

    def finalizar_ventas(self):
        if not self.ventas:
            print("\nNo hay ventas registradas.")
            return

        self.contenido = "Listado de ventas:\n"
        for venta in self.ventas:
            self.contenido += venta + "\n"
        self.contenido += "\nTotal de ingresos: ${:.2f}\n".format(self.total_general)
        os.system('cls')
        print(self.contenido)

        print("\n¡Gracias por su compra!")

if __name__ == "__main__":
    app = ventaEntradas()
    app.iniciar()
