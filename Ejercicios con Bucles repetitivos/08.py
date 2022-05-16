'''Ejercicio 2.8.
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta desde atrás de ese número hasta cero separados por comas.'''


from os import sep



n = int(input("Ingrese un entero positivo: "))


for numero in range(n,0,-1):
    print(numero,end=",") 
    
  
print()


c=int(input("Ingrese un numero:"))
print(*range(c,0,-1), sep=',')