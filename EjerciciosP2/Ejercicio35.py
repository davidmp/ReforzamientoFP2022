def ejercicio35():
    #Definir Variables
    mes:int
    anho:int
    cantDias:int
    mesletras:str
    #Datos de Entrada
    mes=int(input("Ingrese el mes en numeros:"))
    anho=int(input("Ingrese el año correspondiente:"))
    #Proceso
    if(mes==1):
        cantDias=31
        mesletras="Enero"
    elif mes==2:
        if (anho%4==0 and (anho%100!=0 or anho%400==0)):
            cantDias=29
        else: 
            cantDias=28        
        mesletras="Febrero"
    elif mes==3:
        cantDias=31
        mesletras="Marzo"
    elif mes==4:
        cantDias=30
        mesletras="Abril"     
    elif mes==5:
        cantDias=31
        mesletras="Mayo"
    elif mes==6:
        cantDias=30
        mesletras="Junio"  
    elif mes==7:
        cantDias=31
        mesletras="Julio"
    elif mes==8:
        cantDias=31
        mesletras="Agosto"
    elif mes==9:
        cantDias=30
        mesletras="Setiembre"   
    elif mes==10:
        cantDias=31
        mesletras="Octubre"   
    elif mes==11:
        cantDias=30
        mesletras="Noviembre"   
    elif mes==12:
        cantDias=31
        mesletras="Diciembre"     
    else:
        cantDias=0
        mesletras="Mes no valido"                                         
    #Datos de Salida
    print(mesletras)
    print("Tiene ", cantDias," dias")
    
ejercicio35()    