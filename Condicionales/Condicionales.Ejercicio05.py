'''Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''

horas = float(input("ingrese la cantidad de horas trabajadas: "))
costeHora = float(input("Ingrese el coste por hora: "))
paga = horas * costeHora
print("La paga es de", paga , "pesos.")
