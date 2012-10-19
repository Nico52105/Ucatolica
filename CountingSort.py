import random
import time

def CountingSort(lista, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m               
    for a in lista:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):
            lista[i] = a
            i += 1
    return lista

def mayor(numMayor):
    if numMayor ==[]:
        return("error")
    elif len(numMayor) == 1:
        return(numMayor)
    lista_nueva = 0
    while numMayor != []:
        primero = numMayor[0]
        if lista_nueva > primero:
            lista_nueva = lista_nueva
        else:
            lista_nueva =primero
        numMayor = numMayor[1:]
    return(lista_nueva)

def reset():
    TamLista = input("INGRESE TAMAÑO DE NUMEROS A ORDENAR EJ:10-100-1000\n")
    lista = []
    
    for i in range(TamLista):
        lista.append(random.randint(0,(TamLista*10)))
    print lista
    numMayor = lista     
    numM = mayor(numMayor)

    print ("LISTA ORDENADA")
    Tiempo_inicia1 = time.clock()
    CountingSort(lista,numM)
    Tiempo_Termina1 = time.clock()
    print"Tiempo De Ordenamiento: %f"%(Tiempo_Termina1 - Tiempo_inicia1)
    print lista
    print"Tiempo De Ordenamiento: %f"%(Tiempo_Termina1 - Tiempo_inicia1)
    
    reset()

reset()

#Misael Armando Gutierrez Gutierrez
#Codigo: 625120
#Analisis y Diseño De Algoritmos
#Universidad Catolica De Colombia

