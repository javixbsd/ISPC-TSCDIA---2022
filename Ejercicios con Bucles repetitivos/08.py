'''Ejercicio 2.8.
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta desde atrás de ese número hasta cero separados por comas.'''

from pickle import APPEND


n = int(input("Ingrese un entero positivo: "))

salida = []
for numero in range(n,0,-1):
    salida.append(numero)
  
print(salida)  
