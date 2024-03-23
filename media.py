print('''
BEM VINDO AO SISTEMA DE NOTAS DE CÁLCULO!!!
''')

n1 = float(input("DIGITE A PRIMEIRA NOTA: "))
n2 = float(input("DIGITE A SEGUNDA NOTA: "))
t = float(input("DIGITE A NOTA DO TRABALHO: "))
med = ((n1+n2+t)/3)

print("Sua media é :",med)

if (med>=6):
    print("Parabens! Você passou na matéria. ")
else:
    print("Que pena! infelizmente sua média foi menor que 6, então você está reprovado. ")
