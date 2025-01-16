'''x = 0

while x<10:
    print(x)
    x = x+1
    '''

''' Operación de multiplicación de a x b utilizando sumas
    a=3
    b=4
    salida: 3+3+3+3=12
'''

a = int(input("Ingresa la cantidad a sumar: "))
b = int(input("Ingresa la cantidad de veces que se va a sumar: "))
cont = 0
resultado = 0
salida = ""

while b>cont:
    resultado = resultado + a
    salida += str(a) + "+"
    cont = cont + 1

texto = salida + " = " + str(resultado)
print(texto)
