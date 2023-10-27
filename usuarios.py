def lee_datos(nombre):
    datos = []
    ar = open(nombre)
    for linea in ar:
        linea = linea.rstrip('\n')
        datos.append(linea)
    ar.close()
    return datos

def genera_usuarios(datos):
    usuarios = []
    for dato in datos:
        lista = dato.split(' ')
        user = lista[0][0].lower() + lista[1].lower()
        if user in usuarios:
            user = user + lista[2].upper()
        usuarios.append(user)
    return usuarios

def crea_archivo_usuario(usuarios):
    sal = open('usuarios.txt', 'w')
    for user in usuarios:
        sal.write(user + '\n')
    sal.close()

if __name__ == '__main__':
    datos = lee_datos('nombres.txt')
    usuarios = genera_usuarios(datos)
    crea_archivo_usuario(usuarios)