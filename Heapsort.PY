#-----------------------------------#
#Nicolas Fiquitiva Segura
#625120
#Analisis y Diseño De Algoritmos
#Universidad Catolica De Colombia
#-----------------------------------#
import random
import time
##Este metodo es el encarhado de realizar el ordenamienyo por el metodo heapsort o de monticulos
def Ondenar(a):
    def sift(start, count):  
        root = start  
  
        while root * 2 + 1 < count:  
            child = root * 2 + 1  
            if child < count - 1 and a[child] < a[child + 1]:  
                child += 1  
            if a[root] < a[child]:  
                a[root], a[child] = a[child], a[root]  
                root = child  
            else:  
                return  
  
    count = len(a)  
    start = count / 2 - 1  
    end = count - 1  
  
    while start >= 0:  
        sift(start, count)  
        start -= 1  
  
    while end > 0:  
        a[end], a[0] = a[0], a[end]  
        sift(0, end)  
        end -= 1
    return a

  
def Heapsort():
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
        Heapsort();
Heapsort();



  
