'''Ejercicio 2.2.
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:

F =  f - 32 * 5/9.'''

f = float(input("Ingrese los grados en Fahrenheit: "))
celsius = (f - 32) * 5/9

print(f,"grados fahrenheit son igual a :", celsius,"grados celsius")