

arregloRut=[]


def calculoDigitoVerificador(rut):
    datosRut=[]
    datosRut=rut
    digRut=[]
    
    #RECORRO EL LARGO DEL RUT REGISTRO A REGISTRO Y ELIMINO LOS ULTIMOS REGISTROS
    #for x in range(0,len(datosRut)-2):        
    for x in range(0,len(datosRut)):        
        #ASIGNO A LA VARIABLE DIGRUT COMO ARREGLO CON EL VALOR DE CADA REGISTRO 
       digRut.append(datosRut[x])  
    #RECORRO EL ARREGLO DIGRUT Y LO INVERTO
    list.reverse(digRut) 
    largo=len(digRut)
    
    for x in digRut:
        calcularVerificador(int(x),largo)

def calcularVerificador(x,largo):
    global arregloRut
    datoMulti=x
    i = 1
    d = 0
    arregloRut.append(datoMulti)
    if len(arregloRut) == largo:
        for x in arregloRut:
            if i == 7:
                i = 2
                d += (x * i) 
            else:
                i += 1 
                d += (x * i)   
                
        resto=d%11
        digitoVerificador=11-resto  
        
        if digitoVerificador == 10:
            digitoVerificador = "K"
        elif digitoVerificador == 11:
            digitoVerificador = 0
        else: 
            digitoVerificador = digitoVerificador
                
        print("su Rut es : ", str(rut) +"-"+ str(digitoVerificador))
        #print("arregloRut",arregloRut)
        
        
#INICIO DE LA EJECUCION DEL VALIDADOR DE RUT
print(" Validador de Rut ")
print("Ingrese el RUT sin dígito verificador ")
rut=input()
calculoDigitoVerificador(rut)        