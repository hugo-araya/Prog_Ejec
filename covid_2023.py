import matplotlib.pyplot as plt

def calcula_promedio(fecha, datos):
    suma = 0
    cont = 0
    for dato in datos:
        if fecha in dato[0]:
            suma = suma + float(dato[1])
            cont += 1
    if cont != 0:
        promedio = suma / cont 
    else:
        promedio = 0
    return promedio   

def lectura(nombre):
    ar = open(nombre)
    datos = []
    for linea in ar:
        linea = linea.rstrip('\n')
        lista = linea.split(' ')
        datos.append(lista)
    ar.close()
    return datos

def proceso(datos):
    resultados = []
    ultimo = datos[-1]
    septiembre = 0
    for dato in datos:
        if '2020-09' in dato[0]:
            septiembre = septiembre + float(dato[1])
    resultados.append(ultimo)
    resultados.append(septiembre)
    year = 2020
    while year < 2023:
        mes = 1
        while mes < 13:
            m = str(mes)
            if len(m) == 1:
                m = '0'+m
            fecha = str(year)+'-'+m
            promedio = calcula_promedio(fecha, datos)
            resultados.append(promedio)
            mes = mes + 1
        year = year + 1
    return resultados
    
def muestra(resultados):
    print('Ultimo dia informado:', resultados[0][1])
    print('Casos mes de septiembre 2020:', resultados[1])
    promedio_mensual = []
    i = 2
    largo = len(resultados)
    mes = 1
    year = 2020
    while i < largo:
        valor = resultados[i]
        if valor != 0:
            m = str(mes)
            if len(m) == 1:
                m = '0'+m
            print('Promedio',year,'/',m,':', valor)
            promedio_mensual.append(valor)
        mes = mes + 1
        if mes > 12:
            year = year + 1
            mes = 1
        i = i + 1

    plt.plot(promedio_mensual)
    plt.show()

if __name__ == '__main__':
    datos = lectura('TotalesNacionales.txt')
    resultados = proceso(datos)
    muestra(resultados)
