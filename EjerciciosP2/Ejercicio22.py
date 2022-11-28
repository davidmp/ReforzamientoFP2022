def ejercicio22():
    #Definir Variables
    montoComp=float(0)
    montoDesc=float(0)
    montoRecarg=float(0)
    totalPagar=float(0)
    tipoCliente:str()
    tipoPago: str()
    #Leer Datos de entrada
    montoComp=float(input("Ingrese Monto de Compra:"))
    tipoCliente=input("Ingrese Tipo Cliente G/A:")
    tipoPago=input("Ingrese tipo de pago C/P:")    
    #Proceso
    if tipoCliente=="G":
        if tipoPago=="C":
            montoDesc=montoComp*0.15
        else:
            montoRecarg=montoComp*0.10
    else:
        if tipoPago=="C":
            montoDesc=montoComp*0.20
        else:
            montoRecarg=montoComp*0.05      
    totalPagar=(montoComp-montoDesc)+montoRecarg
    #Datos de Salida
    print("Monto de Compra:", montoComp)
    print("-----------------------------")
    print("Total descuento:", montoDesc)
    print("Total Recargo:", montoRecarg)
    print("Total a Pagar:", totalPagar)

ejercicio22()
    