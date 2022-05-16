
''' 1. Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que
pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección. '''

def hola(aula):
    print("Hola Aula "+aula + " ¿Qué tal?" )
def nombre(name):
    print("Bienvenido al Curso de Inteligencia Arififial " + name)
def despedita(name):
     print("Que tengas un buen dia " + name)   
i = 1
while i < 6:
  aula = input("ingrese su numero de aula:")
  hola(aula)
  name = input("Cual es su nombre? ")
  nombre(name)
  despedita(name)
  i += 1