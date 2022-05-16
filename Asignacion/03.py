'''Ejercicio 2.3.
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla 
el nombre en mayúsculas y el número de caracteres que contiene en líneas distintas.'''

name = input("Ingrgrese su nombre: ")

nameUp = name.upper()
numCaract = len(name)
print(nameUp)
print("\nEl num de caracteres es: ", numCaract)
