lista = [1,2,3,4,5,6,7,8,9]
print(lista)
print(lista[2:5])
print(lista[-1])
lista.append(10)
print(lista)
lista = lista[:5] + [0] + lista[5:]
print(lista)


