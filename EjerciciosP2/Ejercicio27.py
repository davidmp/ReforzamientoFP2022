def ejercicio27():
    #Definir variable
    codigo:int
    estadoCivil:str
    #Datos de entrada
    codigo=int(input("Introducu Código:"))
    #Proceso
    if(codigo==0):
        estadoCivil="Soltero"
    elif codigo==1:
        estadoCivil="Casado"
    elif codigo==2:
        estadoCivil="Divorciado"      
    elif codigo==3:
        estadoCivil="Viudo"
    else:
        estadoCivil="Codigo novalido"     
    #Datos de salida
    print(estadoCivil) 

ejercicio27()