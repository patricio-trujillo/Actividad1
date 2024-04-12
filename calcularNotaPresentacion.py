arrayProm=[]
"""
3.	Elabora un programa que, ingresando todas las notas, entregue la nota de presentación.

Puntos a calcular:
    3 tareas en Laboratorio, estas valen un 15% del curso,
    3 tareas en clase, que valen un 15% del curso, 
    2 notas solemnes cada una un 35%
"""
#Variable global para el calculo de nota de presentacion


#DECLARACION DE FUNCIONES
def calculoNotaPresentacion(prom, arrayProm):
    if prom == "exit":
        print("la nota de presentacion es : ", round(sum(arrayProm),2))
    else:
        #Se agrega al arreglo en donde estan los promedios de las notas    
       arrayProm.append(prom)   

def ingresaNotas(s):
    i=1
    notas=[]
    if s==1:
        while i<4:
            nota=float(input(f"Ingrese la nota del Laboratorio {i} para calcular su promedio "))
            if nota == 0:
                break
            else:
                 #se agregan las notas ingresadas por el usuario
                notas.append(nota)
                i+=1
    elif s==2:
        while i<4:
            nota=float(input(f"Ingrese la nota {i} de tareas en clases "))
            if nota == 0:
                break
            else:
                 #se agregan las notas ingresadas por el usuario
                notas.append(nota)
                i+=1
    elif s==3:
        while i<3:
            nota=float(input(f"Ingrese la nota {i} Solemnes "))
            if nota == 0:
                break
            else:
                #se agregan las notas ingresadas por el usuario
                notas.append(nota)
                i+=1                    
    return notas
       
def calcularPromedio(notas,s):
    if s==1:
        suma = 0
        promedio=0
        for x in notas:
            suma+=x
            #variable que obtiene el promedio de las notas cde laboratorio contenidas en el arreglo
            promedio= suma/len(notas)
 
        return promedio,suma
    elif s==2:
        suma =0
        pmdLab=0
        pmdTareas=0
        notaPresentacion=0
        for x in notas:
                #Variable que suma las notas contenidas en el arreglo
                suma+=x
                #variable que obtiene el promedio de las notas tareas en clases contenidas en el arreglo 
                pmdLab= ((suma/len(notas))*0.15)
        return pmdLab,suma
                
    elif s==3:
        suma=0
        pmdTareas=0
        global arrayProm
        for x in notas:
                calculoNotaPresentacion((x*0.35),arrayProm)
        
        return pmdTareas,suma


print("Calcular Nota de Presentación a examen")
promLab,suma1=calcularPromedio(ingresaNotas(1),1)
promLab = promLab*0.15
calculoNotaPresentacion(promLab,arrayProm)
promTarea,suma2=calcularPromedio(ingresaNotas(2),2)
calculoNotaPresentacion(promTarea,arrayProm)
promSolemne,suma3=calcularPromedio(ingresaNotas(3),3)
calculoNotaPresentacion("exit",arrayProm)
