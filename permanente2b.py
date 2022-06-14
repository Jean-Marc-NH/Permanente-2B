from time import time

n = [1]

#Crea una lista de un tamaño X
for i in range(10000000):
     n.append(i)

def ordenamiento_por_insercion(A):
    """
    _summary_

    Args:
        A (list): Una lista de numeros
    Returns:
        list: Te devuelve una lista ordenada
    """
    inicio = time()
    for j in range(len(A)):
        key = A[j]
        i = j-1
        while  i>=0 and key <A[i]:
            i = i -1
        A[i+1]= key
    fin = time()
    x = "{0:.10f}".format(fin-inicio)
    return A, x
    

print(ordenamiento_por_insercion(n))


def ordenamiento_por_burbuja(a):
    """
    _summary_

    Args:
        a (list): Una lista con numeros

    Returns:
        list: Ordena los numeros de menor a mayor
    """
    inicio = time()
    n = len(a)
    for i in range(0,n-1):
        for j in range(n-1, i + 1):
            if a[j] < a[j-1]:
                f = a[j]
                a[j] = a[j-1]
                a[j-1] = f
    fin = time()
    x = "{0:.10f}".format(fin-inicio)
    return x

print(ordenamiento_por_burbuja(n))