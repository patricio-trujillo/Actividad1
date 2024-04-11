#Variable global para el calculo de nota de presentacion
arrayProm=[]
arregloRut=[]

def  menu():
    print("seleccione la opcion de la actividad que desea ejecutar")
    print("1 - Convertir de °C a °F")
    print("2 - Calcular Promedio")
    print("3 - Nota de Presentacion")
    print("4 - Calcula Digito Verificador del Rut")    
    op = input()
    return op


def switch_case(x):
    match x:
        case "1":
            #llamada a funcion que convierte grados celsius a fahrenheit
            cel,frh=convertirCelciusAFahrenheit()
            print(f"la conversion de {cel} grados Celsius es {frh} grados Fahrenheit")
            main()
        case "2":
            #Funcion que recibe 3 notas y calcula el promedio
           prom,sum=calcularPromedio(ingresaNotas(1),1)
           #print(f"la suma es :",sum)
           print(f"El Promedio es :",prom)
           main()
        case "3":
            global arrayProm
            promLab,suma1=calcularPromedio(ingresaNotas(1),1)
            promLab = promLab*0.15
            calculoNotaPresentacion(promLab,arrayProm)
            promTarea,suma2=calcularPromedio(ingresaNotas(2),2)
            calculoNotaPresentacion(promTarea,arrayProm)
            promSolemne,suma3=calcularPromedio(ingresaNotas(3),3)
            calculoNotaPresentacion("exit",arrayProm)
            main()
        case "4":
            print("Ingrese el RUT que desea calcular el digito Verificador")
            rut=input()
            calculoDigitoVerificador(rut)
            main()
        case _:
            return main()
        

def calculoDigitoVerificador(rut):
    datosRut=[]
    datosRut=rut
    digRut=[]
    
    for x in range(0,len(datosRut)-2):        
       digRut.append(datosRut[x])  
  
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
                
        print("el Digito Verificador es :",digitoVerificador)
        #print("arregloRut",arregloRut)
      
          
def calculoNotaPresentacion(prom, arrayProm):
    if prom == "exit":
        print("la nota de presentacion es : ", sum(arrayProm))
    else:    
       arrayProm.append(prom)     
       
            
# formula celsius fh(12 °C × 9/5) + 32 = 53.6 °F
def convertirCelciusAFahrenheit():
        print("Ingrese los grados Celsius que desea Convertir")
        gdsCelsius = float(input())
        gdsFahrenheit = float((gdsCelsius * 9/5)+32)
        #print ("la conversion de ",gdsCelsius, "° Celsius es ",  gdsFahrenheit, "° Fahrenheit")
        return gdsCelsius,gdsFahrenheit

        
def ingresaNotas(s):
    i=1
    notas=[]
    if s==1:
        while i<4:
            nota=float(input(f"Ingrese la nota {i} para calcular su promedio "))
            if nota == 0:
                break
            else:
                notas.append(nota)
                i+=1
    elif s==2:
        while i<4:
            nota=float(input(f"Ingrese la nota {i} de tareas en clases "))
            if nota == 0:
                break
            else:
                notas.append(nota)
                i+=1
    elif s==3:
        while i<3:
            nota=float(input(f"Ingrese la nota {i} Solemnes "))
            if nota == 0:
                break
            else:
                notas.append(nota)
                i+=1                    
    return notas
 
 
def calcularPromedio(notas,s):
    if s==1:
        suma = 0
        promedio=0
        for x in notas:
            suma+=x
            promedio= suma/len(notas)
 
        return promedio,suma
    elif s==2:
        suma =0
        pmdLab=0
        pmdTareas=0
        notaPresentacion=0
        for x in notas:
                suma+=x
                pmdLab= ((suma/len(notas))*0.15)
        return pmdLab,suma
                
    elif s==3:
        suma=0
        pmdTareas=0
        global arrayProm
        for x in notas:
                calculoNotaPresentacion((x*0.35),arrayProm)
        
        return pmdTareas,suma
        
def main():
    print("***************************")
    print("Actividad Modulo 1 ")
    print("***************************")
    op = menu()
    switch_case(op)
    return

#llamada inicial
main()

    



