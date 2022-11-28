def ejercicio55p():
    #Definir Variables
    vector=[None]*6
    contador=int(0)
    temp=int(0)
    #Leer Datos
    for i in range(len(vector)):
        vector[i]=int(input(f"Ingrese el valor de la posicion {(i+1)}:"))        
    #Proceso
    vector.sort()
    print(vector)
    for x in range(1,len(vector)):                
        if(vector[x-1]==vector[x]):
            if temp!=vector[x]:
                contador=contador+1
            temp=vector[x]                        
    #Datos de Salida
    print("De los 6 numeros se repiten ", contador)

ejercicio55p()