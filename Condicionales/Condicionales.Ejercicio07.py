'''Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase "Tu índice de masa corporal es " donde es el índice de masa corporal 
calculado redondeado con dos decimales.
El índice de masa corporal (IMC) es el peso de una persona en kilogramos dividido por el cuadrado de la estatura en metros
'''

peso = float(input("Ingrese su peso en kg :"))
estatura =  float(input("Ingrese su estatura en metros : "))
imc = peso / pow(estatura,2)
print("Tu índice de masa corporal es ", round(imc,2))