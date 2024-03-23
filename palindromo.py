def palin(a):
    a= a.replace(" ", "").lower()

    return a == a[::-1]

palavra = input("Digite a palavra: ")

if palin(palavra):
    print("ESSA PALAVRA É UM PALINDROMO. ")
else:
    print("ESSA PALAVRA NÃO É UM PALINDROMO. ")

