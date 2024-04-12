'''
Debes crear un programa que dibuje una matriz, según las siguientes consideraciones:
    1. Solicitar la cantidad de filas.
    2. Solicitar la cantidad de columnas.
    3. Dibujar las filas y columnas solicitadas
'''
# Definición de la función para imprimir el formato de la matriz
def generaMatrix(filas, columnas):
    # Imprimir la primera línea superior de la matriz
    print("+", end="")              # Imprimir el borde izquierdo de la primera celda
    for _ in range(columnas):       # Repetir según el número de columnas
        print("---+", end="")       # Imprimir la línea horizontal entre celdas
    print()                         # Salto de línea para comenzar la nueva fila
    
    # Imprimir cada fila de la matriz
    for _ in range(filas):          # Repetir según el número de filas
        # Imprimir línea vertical izquierda de la celda y celdas vacías
        print("|", end="")
        for _ in range(columnas):   # Repetir según el número de columnas
            print("   |", end="")   # Imprimir celdas vacías
        print()                     # Salto de línea para comenzar la nueva fila
        # Imprimir línea horizontal inferior de la celda
        print("+", end="")
        for _ in range(columnas):   # Repetir según el número de columnas
            print("---+", end="")   # Imprimir la línea horizontal entre celdas
        print()                     # Salto de línea para comenzar la nueva fila
        
# Función principal
# # Solicitar al usuario el número de filas y columnas
def main():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    # Mostrar el formato de la matriz
    print("\nEl formato de la matriz es:")
    # Llamar a la función para imprimir el formato de la matriz
    generaMatrix(filas, columnas)

#if __name__ == "__main__":
main()
