"""3. Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar
el resultado dos veces."""




def suma(n1, n2):
    return n1 + n2
    
def resultado(res):
    print( "\nLa suma es:" ,res)    

n1 = float(input("Ingrese un num: "))
n2 = float(input("ingrese otro num: "))
res = suma(n1,n2)
print(res)
i=0
while i<2:
    resultado(res)
    i +=1
