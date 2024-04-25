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
            if num < 1 or num > 9:
                raise ValueError
            break
        except ValueError:
            print("Error: Debe ingresar un número entero del 1 al 9.")

    # Paso 2: Solicitar al usuario que ingrese números secuenciales saltándose el número ingresado y sus múltiplos
    #print(f"Ingrese números secuenciales comenzando desde 1, pero saltándose el número {num} y sus múltiplos:")
    i = 1
    while True:
        try:
            if i % num == 0:
                #print(f"Se ha saltado el número {i} y sus múltiplos.")
                i += 1
                continue
            user_input = int(input(f"Ingrese el número {i}: "))
            if user_input != i:
                # se envia un mensaje informando al usuario el numero que debe ingresar
                raise ValueError(f"Error: Debe ingresar el número {i}.") 
            i += 1
        except ValueError as e:
            print(e)
        else:
            if i == 10:  # Cuando se han ingresado 9 números correctamente, termina el ciclo
                break

    print("¡Felicidades! Ha ingresado correctamente los números secuenciales.")

if __name__ == "__main__":
    main()
