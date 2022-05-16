'''Ejercicio 2.7.
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.'''


n1 = int(input("Ingrese primer num: "))
n2 = int(input("Ingrese el segundo num: "))


while n1 != n2+1 :
    if n1%2 ==0:
        print("\n",n1)
    n1 +=1        

   
''' 
for numero in range(n1, n+1):
    if(numero % 2 == 0):
        print(numero)

'''
