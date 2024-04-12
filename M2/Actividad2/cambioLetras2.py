def reemplazar_letras(frase, palabra1, palabra2):
    # Crear un diccionario de reemplazo
    reemplazo = {letra1: letra2 for letra1, letra2 in zip(palabra1, palabra2)}

    # Aplicar el reemplazo a la frase
    nueva_frase = ''.join(reemplazo.get(letra, letra) for letra in frase)

    return nueva_frase

def main():
    # Paso 1: Permitir al usuario elegir dos palabras
    palabra1 = input("Ingrese la primera palabra: ").lower()
    palabra2 = input("Ingrese la segunda palabra: ").lower()

    # Verificar que las palabras tengan la misma longitud
    if len(palabra1) != len(palabra2):
        print("Error: Las palabras deben tener la misma longitud.")
        return

    # Paso 2: Solicitar al usuario que ingrese una frase
    frase = input("Ingrese una frase: ")

    # Paso 3: Reemplazar las letras según la regla establecida a partir de las palabras elegidas
    nueva_frase = reemplazar_letras(frase, palabra1, palabra2)

    # Paso 4: Imprimir la nueva frase con las letras reemplazadas
    print("La frase con las letras reemplazadas es:")
    print(nueva_frase)

if __name__ == "__main__":
    main()
