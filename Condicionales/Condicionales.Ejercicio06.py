'''Ejercicio 6
Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la
 suma de todos los enteros desde 1 hasta n. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
'''
flag = 0
while flag == 0:
    n = int(input("Ingrese un num entero positivo: "))
    if n > 0 :
        suma = (n*(n+1) ) / 2
        print("La suma es: ", suma)
        flag = 1
    else:
        print("Debe ingresar un entero positivo") 