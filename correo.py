'''
Solicitar al usuario que ingrese su dirección email. 
Imprimir un mensaje indicando si la dirección es válida o no, 
valiéndose de una función para decidirlo.
Una dirección se considerará válida si contiene el símbolo "@".
'''
def lee_correo():
    correo = []
    ar = open('correos.txt')
    for linea in ar:
        correo.append(linea)    
    return correo

def valida_correo(correo):
    estado_correo = []
    for mail in correo:
        if '@' in mail:
            estado_correo.append('Valido')
        else:
            estado_correo.append('No Valido')
    return estado_correo

def muestra_estado(estado_correo):
    for estado in estado_correo:
        print('Estado: ', estado)

if __name__ == '__main__':
    correo = lee_correo()
    estado_correo = valida_correo(correo)
    muestra_estado(estado_correo)
