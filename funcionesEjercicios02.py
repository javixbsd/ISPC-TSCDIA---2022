"""2. A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con al
menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos
ejercicios trabajamos argumentos."""

def name(nombre):
    print(" Hola " + nombre + ", ¿Qué tal?")

i = 0
while i < 3 :
    nombre = input("Cual es su nombre?")
    name(nombre)
    i +=1
