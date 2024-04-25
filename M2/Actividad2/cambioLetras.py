'''
Elige dos palabras del mismo largo en las que dos letras iguales no coincidan en la misma posición. Por 
ejemplo, si se eligen las palabras "morena" y "pelito", cualquier "m" que aparezca en una frase será 
reemplazada por una "p", las letras "o" se reemplazan por "e", "r" por "l", "e" por "i", "n" por "t" y "a" por "o".

Crea un programa que:
    1. Permita al usuario elegir dos palabras que cumplan con las condiciones mencionadas anteriormente.
    2. Solicite al usuario que ingrese una frase.
    3. Reemplace las letras según la regla establecida a partir de las palabras elegidas.
    4. Imprima la nueva frase con las letras reemplazadas.
'''
def reemplazar_letras(palabra1, palabra2, frase):
    # Crear un diccionario de reemplazo con las letras de palabra1 como clave y las letras de palabra2 como valor
    reemplazo = dict(zip(palabra1, palabra2))
    
    # Reemplazar las letras en la frase según el diccionario de reemplazo
    nueva_frase = ""
    for letra in frase:
        if letra.lower() in reemplazo:
            # Mantener el caso original de la letra
            if letra.isupper():
                nueva_frase += reemplazo[letra.lower()].upper()
            else:
                nueva_frase += reemplazo[letra.lower()]
        else:
            nueva_frase += letra
    
    return nueva_frase

def main():
    # Paso 1: Permitir al usuario elegir dos palabras
    palabra1 = input("Ingrese la primera palabra: ").strip().lower()
    palabra2 = input("Ingrese la segunda palabra: ").strip().lower()
    
    # Verificar si las palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        print("Las palabras deben tener la misma longitud.")
        return
    
    # Paso 2: Solicitar al usuario que ingrese una frase
    frase = input("Ingrese una frase: ")
    
    # Paso 3: Reemplazar las letras según la regla establecida
    nueva_frase = reemplazar_letras(palabra1, palabra2, frase)
    
    # Paso 4: Imprimir la nueva frase con las letras reemplazadas
    print("La nueva frase con las letras reemplazadas es:")
    print(nueva_frase)

if __name__ == "__main__":
    main()
