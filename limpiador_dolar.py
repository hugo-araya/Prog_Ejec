ar = open('datos_total.txt')
sal = open('datos_salida.txt','w')
for linea in ar:
    linea = linea.rstrip('\n')
    lista = linea.split('\t')
    if lista[1] != '':
        lista[1]=lista[1].replace(',','.')
        sal.write(lista[0]+' '+lista[1]+'\n')
ar.close()
sal.close()
