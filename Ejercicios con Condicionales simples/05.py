'''Ejercicio 2.5.
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos superiores a $1000 mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.'''

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Cual es su ingreso mensual: "))

if edad > 15 and ingresos > 1000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")    
