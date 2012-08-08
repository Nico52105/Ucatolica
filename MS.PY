#-----------------------------------#
#Nicolas Fiquitiva Segura
#625120
#Analisis y Diseño De Algoritmos
#Universidad Catolica De Colombia
#-----------------------------------#
import random
import time

def Ondenar(Lista):
    if len(Lista) == 1:
        return Lista
    
    mitad = len(Lista) / 2
    cabeza = Ondenar(Lista[:mitad])
    cola = Ondenar(Lista[mitad:])

    if not len(cabeza) or not len(cola):
        return cabeza or cola
        
    result = []
    i = j = 0
    while (len(result) < len(cola)+len(cabeza)):        
        if cabeza[i] < cola[j]:
            result.append(cabeza[i])
            i += 1
        else:
            result.append(cola[j])
            j += 1            
        if i == len(cabeza) or j == len(cola):            
            result.extend(cabeza[i:] or cola[j:])
            break
        
    return result

def mergesort():
    Tamano=input("Ingrese la cantidad de numeros a ordenar \n")
    Elementos = []
    for i in range(Tamano):
        Elementos.append(random.randint(0, (Tamano*10)))
    print "Elementos a ordenar"
    print Elementos
    print "Elementos ordenados"    
    To=time.clock()
    print Ondenar(Elementos)
    print "Tiempo de ejecucion"
    print time.clock()-To
    rta=input("\n\nPresione [1] para continuar \n")
    if(rta==1):
        mergesort();
mergesort();
