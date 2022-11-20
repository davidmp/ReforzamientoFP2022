import math

def ejercico01():
    print("hola")

    num=[None]*12 #definir vector

    #Asignando valores
    num[0]=39
    num[1]=-2
    num[4]=0
    num[6]=14
    num[8]=5
    num[9]=120
    numx=[39,-2,None,None, 0,None,14,None,5,120,None,None]
    #Imprimir vector
    print(num)
    print(numx)

def ejercio02():
    num1=int(input("Ingrese el Primer numero:"))
    num2=int(input("Ingrese el Segundo numero:"))
    c=num1/num2
    print("Cociente:", c)
    r=num1%num2
    print("Resto:", r)

def ejercicio31():
    #definir variables
    nota:float()
    categoria:str()
    #Leer datos
    nota=float(input("Ingrese Nota Promedio:"))
    #proceso
    if nota>=0 and nota<=5:
        categoria="Pesimo"
    elif nota>=6 and nota<=10:
        categoria="Malo"
    elif nota>=11 and nota<=14:
        categoria="Regular"
    elif nota>=15 and nota<=16:
        categoria="Bueno"
    elif nota>=17 and nota<=20:
        categoria="Excelente"
    else:
        categoria="Nota no valida"
    #Datos de salida
    print(categoria)

def ejercicio08():
    #Definir variables
    capital:float()
    ti:float()
    ic:float()
    tiempo:int()
    #Datos de entrada
    capital=float(input("Ingrese el Capital:"))
    ti=float(input("Ingrese tasa de interes:"))
    tiempo=int(input("Tiempo de inversion:"))
    #Proceso
    ic=((math.pow((1+ti),tiempo))*capital) - capital
    #Datos de salida
    print("Intere Compuesto:", ic)
#ejercio02()
#ejercicio31()

def propuesto50():
    #definir variables
    numFin:int()    
    #Datos de entrada
    numFin=int(input("Ingrese el rango Final:"))
    #proceso
    if(numFin>=10):
        for i in range(numFin):    
            valorI=str(i)[::-1];                        
            if i>=10 and i==int(valorI):
                print(i)

                
    #datos de salida
def propuesto43():
    numA=int(input("Ingrese el num A:"))
    numB=int(input("Ingrese el num B:"))
    numPar, numImpar, numMult3=0,0,0    
    sumPar, sumImpar, sumMult3=0,0,0
    for i in range(numA,numB+1):
        if i%2==0:
            numPar=numPar+1
            sumPar=sumPar+i
        else:
            numImpar=numImpar+1
            sumImpar=sumImpar+i
        if(i%3==0):
            numMult3=numMult3+1
            sumMult3=sumMult3+i
    print("Cant num Par:", numPar)
    print("Cant num Impar:", numImpar)
    print("Cant num Multiplo 3:", numMult3)
    print("Suma num Par:", sumPar)
    print("Suma num Impar:", sumImpar)
    print("Suma num Multiplo 3:", sumMult3)    

#ejercicio08()
#propuesto50()
propuesto43()




