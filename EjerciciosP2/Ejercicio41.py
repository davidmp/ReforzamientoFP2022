import math
def ejercicio42():
    #definir variables
    sumaCuadrado=float(0)
    sumaCubica=float(0)
    Nnum:int
    #Leer Datos
    Nnum=int(input("Ingrese N primeros numeros:"))
    #Proceso
    for i in range(1, Nnum+1):
        sumaCuadrado=sumaCuadrado+math.pow(i,2)
        sumaCubica=sumaCubica+math.pow(i,3)
    #Datos de Salida
    print("Suma Cuadrados es:", sumaCuadrado)
    print("Suma Cubicas es:", sumaCubica)

ejercicio42()