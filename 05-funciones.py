import os

def funcion1():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res = num1 + num2
    print(f'Resultado: {res}')

def funcion2():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res = num1 - num2
    print(f'Resultado: {res}')

def run():
    while True:
        print('1. Suma')
        print('2. Resta')
        print('3. Salir')
        op = int(input('Opcion: '))
        if op == 1:
            funcion1()
            print('')
        if op == 2:
            funcion2()
            print('')
        if op == 3:
            break
    os.system('cls')
    
if __name__== "__main__":
    run()