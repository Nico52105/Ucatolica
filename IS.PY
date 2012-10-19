#-----------------------------------#
#Nicolas Fiquitiva Segura
#625120
#Analisis y Diseño De Algoritmos
#Universidad Catolica De Colombia
#-----------------------------------#

import random
import time

def Ondenar(Lista,Tam): 
    To=time.clock()
    for i in range(Tam):
      Compara = Lista[i]
      Posicion = i-1
      while (Posicion >= 0 and Lista[Posicion] > Compara):
         Lista[Posicion+1] = Lista[Posicion]
         Posicion = Posicion-1
      Lista[Posicion+1] = Compara
    print Lista
    print "Tiempo de ejecucion"
    print time.clock()-To

def insertsort():
    Tamano=input("Ingrese la cantidad de numeros a ordenar \n")
    Elementos = []
    for i in range(Tamano):
        Elementos.append(random.randint(0, (Tamano*10)))
    print "Elementos a ordenar"
    print Elementos
    print "Elementos ordenados"    
    Ondenar(Elementos,Tamano)
    rta=input("\n\nPresione [1] para continuar \n")
    if(rta==1):
        insertsort();
insertsort();
