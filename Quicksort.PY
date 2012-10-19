#-----------------------------------#
#Nicolas Fiquitiva Segura
#625120
#Analisis y Diseño De Algoritmos
#Universidad Catolica De Colombia
#-----------------------------------#
import random
import time

def Ondenar(arr, l, r):  
    def swap(arr, s, d):  
        if s != d:  
            tmp = arr[s]  
            arr[s] = arr[d]  
            arr[d] = tmp  
    if l >= r:  
        return      
    m = l  
    for i in range(l, r):  
        if arr[i] <= arr[r]:  
            swap(arr, i, m)  
            m += 1  
    swap(arr, m, r)  
    Ondenar(arr, l, m-1)  
    Ondenar(arr, m+1, r)  
    return arr

  
def Quicksort():
    Tamano=input("Ingrese la cantidad de numeros a ordenar \n")
    Elementos = []
    for i in range(Tamano):
        Elementos.append(random.randint(0, (Tamano*10)))
    print "Elementos a ordenar"
    print Elementos
    print "Elementos ordenados"    
    To=time.clock()
    print Ondenar(Elementos,0,Tamano-1)
    print "Tiempo de ejecucion"
    print time.clock()-To
    rta=input("\n\nPresione [1] para continuar \n")
    if(rta==1):
        Quicksort();
Quicksort();



  
