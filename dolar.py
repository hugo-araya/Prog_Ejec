import matplotlib.pyplot as plt

def calcula_promedio(year, datos):
    suma = 0
    contador = 0
    for elem in datos:
        fecha = elem[0]
        valor = float(elem[1])
        if fecha[7:] == year:
            suma = suma + valor
            contador = contador + 1
    promedio = suma / contador
    return promedio  

def lee_datos(nombre):
    datos = []
    ar = open(nombre)
    for linea in ar:
        linea = linea.rstrip('\n')
        lista = linea.split(' ')
        datos.append(lista)
    ar.close()
    return datos
    
def procesar(datos):
    promedios = []
    i = 2013
    while i <= 2019:
        promedio = calcula_promedio(str(i), datos)
        promedios.append(promedio)
        i = i + 1
    return promedios

def mostrar(promedios):
    i = 2013
    years = []
    while i <= 2019:
        print('Promedio :', i, int(promedios[i-2013]))
        years.append(i)
        i = i + 1
    plt.title('Dolares')
    plt.plot(years, promedios)
    plt.show()

if __name__ == '__main__':
    datos = lee_datos('datos.txt')
    promedios = procesar(datos)
    mostrar(promedios)
