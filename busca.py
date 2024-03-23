def pesquisa(lista, elemento):
    esq = 0
    dir = len(lista) -1
    while esq <= dir:
        meio = (esq + dir) //2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esq = meio +1
        else:
            dir = meio -1
    return -1

##ENTRADA
lista=list()
i=1
while i<10:
    elem = int(input("Digite um elemento da lista:"))
    lista.append(elem)
    i+=1
print(lista)
lista_ordenada = sorted(lista)
print(lista_ordenada)
elemento = int(input("Digite o elemento para pesquisar:"))

#RESULTADOS
ind =pesquisa(lista, elemento)
if ind != -1:
    print("O elemento", elemento, "foi encontrado no indice", ind)
else:
    print("O elemento", elemento, "não foi encontrado.")