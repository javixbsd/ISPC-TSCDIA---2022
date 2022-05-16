'''Ejercicio 2.1.
Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. 
La fórmula a utilizar es:

Cn = C * (1 + x/100) ^ n

Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.'''

c = float(input("Ingrese la cantidad de pesos: "))
x = float(input("Ingrese la tasa de interes: "))
n = float(input("Ingrese la cantidad de años: "))

cf = c * pow((1+ (x/100)),n)

print("El capital final es :", cf)