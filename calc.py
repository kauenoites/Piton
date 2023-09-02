import sys
import math

def bv():
    print('''
Bem-Vindo a Calculadora
''')
    
    bv()
    calcular()

def calcular():
    op = input('''
Digite a operação matematica que deseja: 
+ para somar
- para subtrair
* para multiplicar
/ para dividir
^ para potência
v para raiz quadrada
''')

    if op == "+" :
        n1 = int(input("DIGITE O PRIMEIRO NUMERO: "))
        n2 = int(input("DIGITE O SEGUNDO NUMERO: "))
        print("{} + {} = ".format(n1, n2))
        print(n1 + n2)

    elif op == "-":
        n1 = int(input("DIGITE O PRIMEIRO NUMERO: "))
        n2 = int(input("DIGITE O SEGUNDO NUMERO: "))
        print("{} - {} = ".format(n1, n2))
        print(n1-n2)

    elif op == "*":
        n1 = int(input("DIGITE O PRIMEIRO NUMERO: "))
        n2 = int(input("DIGITE O SEGUNDO NUMERO: "))
        print("{} * {} = ".format(n1,n2))
        print(n1*n2)

    elif op == "/":
        n1 = int(input("DIGITE O PRIMEIRO NUMERO: "))
        n2 = int(input("DIGITE O SEGUNDO NUMERO: "))
        print("{} / {} = ".format(n1,n2))
        print(n1 / n2)

    elif op == "^":
        n1 = int(input("DIGITE O PRIMEIRO NUMERO: "))
        n2 = int(input("DIGITE O SEGUNDO NUMERO: "))
        print("{} ^ {} = ".format(n1,n2))
        print(n1**n2)

    elif op == "v":
        num = float(input("Entre com um número:\n"))
        raiz = math.sqrt(num)
        print(f'\nA raiz quadrada de {num} é {raiz}\n') 

    else:
        print("Você digitou uma operação invalida, tente novamente. ")

    repetir()

def repetir():
    calDnv = input('''
Deseja calcular novamente?
Digite S para sim ou N para não.
''')
    
    if calDnv.upper() == "S":
        calcular()
    elif calDnv.upper() == "N":
        print("Encerrando programa...")
        sys.exit()
    else:
        repetir()

calcular()