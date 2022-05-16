"""5. Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos
variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos
argumentos para este ejercicio sería dos."""

def symayresta(n1,n2):
    suma = n1 + n2
    resta = n1 - n2
    print("\nLa suma es ", suma)
    print("\nLa resta es ", resta)

n1 = float(input("Ingrese un num: "))
n2 = float(input("Ingrese otro num: "))

symayresta(n1,n2)