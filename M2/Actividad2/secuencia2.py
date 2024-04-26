def solicitar_numero():
    while True:
        try:
            num = int(input("Ingrese un número entero del 1 al 9: "))
            if num < 1 or num > 9:
                raise ValueError
            return num
        except ValueError:
            print("Error: Debe ingresar un número entero del 1 al 9.")


def jugar_juego():
    num = solicitar_numero()
    print("Comienza el juego. Ingresa números secuenciales partiendo desde 1, pero saltándote los múltiplos de", num)
    siguiente_numero = 1
    while True:
        try:
            guess = int(input(f"Ingrese el número {siguiente_numero}: "))
            if guess != siguiente_numero:
                raise ValueError
            if num == 1:
                siguiente_numero += 1
            else:
                if siguiente_numero % num != 0:
                    siguiente_numero += 1
                else:
                    print(f"¡Saltaste el múltiplo de {num}! Siguiente número: {siguiente_numero + 1}")
                    siguiente_numero += 2
        except ValueError:
            print(f"Error: Debes ingresar el número {siguiente_numero}.")


jugar_juego()
