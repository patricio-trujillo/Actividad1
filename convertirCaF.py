"""
1.	Confecciona un programa que solicite al usuario ingresar la temperatura en grados Celsius 
y la convierta a grados Fahrenheit. Luego, se debe imprimir el resultado en pantalla.
"""

print("Ingrese los grados Celsius que desea Convertir")
gdsCelsius = float(input())
gdsFahrenheit = float((gdsCelsius * 9/5)+32)
print ("la conversion de ",gdsCelsius, "° Celsius es ",  gdsFahrenheit, "° Fahrenheit")