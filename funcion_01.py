# Evaluar la funcion f(x) = 2*x + 1, en [1,10[ con un incremento de 1

def f(x):
    return 2*x + 1

def mostrar(i, nro):
    print('f(',i,') -> ', nro)

if __name__ == '__main__':
    i = 1
    while i < 10:
        nro = f(i)
        mostrar(i,nro)
        i = i + 1
    print('Fin')


