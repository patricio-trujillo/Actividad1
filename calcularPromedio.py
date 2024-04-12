"""
2.	Realiza un programa que reciba tres números por teclado y calcule su promedio, 
se debe mostrar el resultado en pantalla.

"""


def ingresaNotas(s):
    i=1
    notas=[]
    
    while i<4:
        nota=float(input(f"Ingrese la nota {i} para calcular su promedio "))
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
  
print("Calcular promedio")  
prom,sum=calcularPromedio(ingresaNotas(1),1)
print(f"El Promedio es :",prom)  