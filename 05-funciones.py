import os

def suma():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res = num1 + num2
    print(f'Resultado: {res}')

def resta():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res = num1 - num2
    print(f'Resultado: {res}')

def multiplicacion():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res = num1 * num2
    print(f'Resultado: {res}')

def division():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res = num1 / num2
    print(f'Resultado: {res}')

def run():
    while True:
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5. Salir')
        op = int(input('Opcion: '))
        if op == 1:
            suma()
            print('')
        if op == 2:
            resta()
            print('')
        if op == 3:
            multiplicacion()
            print('')
        if op == 4:
            division()
            print('')
        if op == 5:
            break
    os.system('cls')
    
if __name__== "__main__":
    run()