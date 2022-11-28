def ejercicio33():
    #definir Variables
    sumaResult=int(0)
    productoResult=int(1)
    nPriNum:int    
    #Datos de ingreso
    nPriNum=int(input("Ingrese N Numero:"))    
    #Proceso
    for i in range(1, nPriNum+1):
        if i%3==0:
            sumaResult=sumaResult+i
            productoResult=productoResult*i
    #Datos de salida
    print("Suma de numeros multiplos de 3:", sumaResult)
    print("Producto de numeros multiplos de 3:", productoResult)

ejercicio33()