def ejercicio34():
    #definir variables
    importePagar=int(0)
    colegioProcedencia:str()
    nivelSocioEcon:str()
    #Datos de Entrada
    colegioProcedencia=input("Ingrese el Colegio de Procedencia- Nacional(N), Particular(P):")
    nivelSocioEcon=input("Ingrese el nivel socioeconomico A/B/C:")
    #Proceso
    if nivelSocioEcon=="A":
        if colegioProcedencia=="N":
            importePagar=300
        else:
            importePagar=400
    elif nivelSocioEcon=="B":
        if colegioProcedencia=="N":
            importePagar=200
        else:
            importePagar=300
    else:
        if colegioProcedencia=="N":
            importePagar=100
        else:
            importePagar=200
    #Datos salida
    print("El importe a pagar por el examen de admision universitaria es:", importePagar)
    
ejercicio34()