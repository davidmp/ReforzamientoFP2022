def ejercicio39():
    #Definir Varibales
    num1:int
    num2:int
    mcd:int
    #Datos de lectura
    num1=int(input("Ingrese valor num1:"))
    num2=int(input("Ingrese valor num1:"))
    #Proceso
    for x in range(1,num1):
        if(num1%x==0 and num2%x==0):
            mcd=x
    
    #Datos de Salida
    print("MCD es:", mcd)

ejercicio39()