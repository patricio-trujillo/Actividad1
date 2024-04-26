#1. Ingresar un número entero del 1 al 9.
numero_base = int(input("ingrese un numero del 1 al 9: "))

#2. Que ingrese números secuenciales partiendo por 1, pero saltándose aquellos que sean múltiplos del
#valor ingresado al comienzo.

#Verificar que ek numero base este dentro del rango

if numero_base < 1 or numero_base > 9:
    print("El numero ingresado no esta dentro del rango 1 y 9")
else:
    #Iniciar contadore de numeros secuenciales
    contador = 1
    while True:
        entrada = int(input("Ingrese el siguiente numero, sin poner el multiplo del numero base :".format(numero_base)))
         #calcular el siguiente numero esperado
         
        while contador % numero_base == 0:
            contador += 1
            
        if entrada == contador:
            print("Felicidades, ha ingresado correctamente los numeros secuenciales")
            contador +=1                
        else:
            print("Error, el numero correcto es : ".format(contador))
            contador +=1
           