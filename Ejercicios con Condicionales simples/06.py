'''Ejercicio 2.6.
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.'''


name = input("Ingrese su nombre: ")
sex = input("Ingrese su sexo: ")

if sex == "femenino":
    if name[0] < "M":
        print("Usted esta en el grupo A") 
    else:
        print("Usted esta en el grupo B")

elif name[0]  > "N":
    print("Usted esta en el grupo A")
else:
    print("Usted esta en el grupo B")    
