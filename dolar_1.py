import matplotlib.pyplot as plt
ar = open('datos_salida.txt')
x = []
y = []
todos = []
datos = []
linea = ar.readline()
while linea != '':
    linea = linea.rstrip('\n')
    lista = linea.split(' ')
    datos.append(lista)
    linea = ar.readline()
ar.close()

year = 1982         
while year < 2024: 
    suma = 0
    contador = 0
    for lista in datos:
        if lista[0][7:] == str(year):
            suma = suma + float(lista[1])
            contador = contador + 1
            todos.append(float(lista[1]))
    promedio = suma / contador
    x.append(year)
    y.append(promedio)
    print('Promedio', year,':', promedio)
    year = year + 1

mayor = 0
for lista in datos:
    if float(lista[1]) > mayor:
        mayor = float(lista[1])
        fecha = lista[0]
print('El mayor valor corresponde al dia',fecha[0:2],'del mes',fecha[3:6],'de',fecha[7:], mayor)

menor = 10000
for lista in datos:
    if float(lista[1]) < menor:
        menor = float(lista[1])
        fecha = lista[0]
print('El menor valor corresponde al dia',fecha[0:2],'del mes',fecha[3:6],'de',fecha[7:], menor)

plt.plot(todos)
plt.title('Dolar observado')
plt.grid()
plt.show()
