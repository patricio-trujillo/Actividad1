'''
Crea un programa en Python que solicite al usuario:
1. Ingresar un número entero del 1 al 9.
2. Que ingrese números secuenciales partiendo por 1, pero saltándose aquellos que sean múltiplos del 
valor ingresado al comienzo.
3. En caso de ingresar un valor erróneo, enviar un mensaje indicando el error y el número que 
correspondía ingresar
'''

def main():
    # Paso 1: Solicitar al usuario que ingrese un número entero del 1 al 9
    while True:
        try:
            num = int(input("Ingrese un número entero del 1 al 9: "))
            if  num == 1:
                #Se envia un warning alerta cuando el valor ingresado es 1 por bucle infinito
                raise ValueError(f"Warning: Los valores del rango 1 al 9 son multiplos de 1.")
            if num < 1 or num > 9:
                #Se envia un mensaje de error cuando el valor ingresado no es un numero entero del 1 al 9
                raise ValueError("Error: Debe ingresar un número entero del 1 al 9.")
            break
        except ValueError as e:
            print(e)

    # Paso 2: Solicitar al usuario que ingrese números secuenciales saltándose el número ingresado y sus múltiplos
    #print(f"Ingrese números secuenciales comenzando desde 1, pero saltándose el número {num} y sus múltiplos:")
    i = 1
    intentos = 0
    while True:
        #se controla el maximo se ingreso de datos permitidas por ejecucion
        if intentos == 10:
            print("Se ha alcanzado el número máximo de intentos.")
            break
        try:
            
            if i % num == 0:
                i += 1
                continue
            user_input = int(input(f"Ingrese el número {i}: "))
            intentos += 1
            if user_input != i:
                # se envia un mensaje informando al usuario el numero que debe ingresar
                raise ValueError(f"Error: Debe ingresar el número {i}.") 
            i += 1

        except ValueError as e:
            print(e)
            intentos += 1
            
    print("¡Felicidades! Ha ingresado correctamente los números secuenciales.")

if __name__ == "__main__":
    main()