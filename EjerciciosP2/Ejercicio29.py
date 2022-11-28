def ejercicio29():
    #Definir variable
    puntaje:int
    genero:str
    ciudad:str
    #Datos de entrada
    puntaje=int(input("Ingrese su puntaje:"))
    genero=input("Ingrese su genero M/F:")
    #Proceso
    if puntaje>=18 and puntaje<=35:
        if genero=="M":
            ciudad="Arequipa"
        else:
            ciudad="Cuzco"
    elif puntaje>=36 and puntaje<=75:
        if genero=="M":
            ciudad="Cuzco"
        else:
            ciudad="Iquitos" 
    else:
        if genero=="M":
            ciudad="Iquitos"
        else:
            ciudad="Arequipa"               
    #Datos de salida
    print(ciudad) 

ejercicio29()
