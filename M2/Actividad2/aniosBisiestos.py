'''
1. Pedir al usuario el año de nacimiento de una persona.
2. Pedir al usuario el año de muerte de la persona.
3. Si la persona sigue viva, el año de muerte será 0. En este caso, el programa debe reemplazar el 0 
por el año actual.
4. Calcular la cantidad de años bisiestos que la persona ha vivido.
5. Mostrar la cantidad de años bisiestos calculados en el paso anterior.
'''
import datetime

def es_bisiesto(anio):
    # Comprueba si el año es bisiesto salida booleana verdadero o falso
    '''
        Un año bisiesto es un año con 366 días en vez de 365. Cada 4 años, febrero tiene un día más. Esto se 
        hace porque un año oficialmente no tiene 365 días, sino 365,25 días. Añadiendo un día cada 4 años, se 
        soluciona este problema. Sin embargo, la regla no se aplica a los años de siglo a menos que sean 
        divisibles por 400. Por ejemplo, 1900 no fue un año bisiesto porque es divisible por 100 pero no por 400, 
        mientras que 2000 sí fue un año bisiesto porque es divisible por 400.
    '''
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def calcular_anios_bisiestos(nacimiento, muerte):
    # Si la persona sigue viva, el año de muerte será 0
    if muerte == 0:
        muerte = datetime.datetime.now().year
    
    # Calcular la cantidad de años bisiestos entre el año de nacimiento y el año de muerte
    anios_bisiestos = sum(1 for anio in range(nacimiento, muerte + 1) if es_bisiesto(anio))
    return anios_bisiestos

def main():
    # Paso 1: Pedir al usuario el año de nacimiento
    nacimiento = int(input("Ingrese el año de nacimiento de la persona: "))
    
    # Paso 2: Pedir al usuario el año de muerte o establecerlo como el año actual si sigue viva
    muerte = int(input("Ingrese el año de muerte de la persona (o 0 si está viva): "))
    if muerte == 0:
        muerte = datetime.datetime.now().year
    
    # Paso 3: Calcular la cantidad de años bisiestos que la persona ha vivido
    anios_bisiestos = calcular_anios_bisiestos(nacimiento, muerte)
    
    # Paso 4: Mostrar la cantidad de años bisiestos calculados
    print(f"La persona ha vivido {anios_bisiestos} años bisiestos.")

if __name__ == "__main__":
    main()
