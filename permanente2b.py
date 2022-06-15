import time

a = []
for i in range(10000000):
    a.append(i)

def bublesort(lista):
    inicio = time.time()
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    fin = time.time()
    return  fin - inicio

# print(f"BubbleSort: {bublesort(a):.10f}")

def insertionSort(lista):
    inicio = time.time()
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j] < lista[j-1]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1
    fin = time.time()
    return fin - inicio

print(f"insertionSort: {insertionSort(a):.10f}")

print("----------------------------------------------------")