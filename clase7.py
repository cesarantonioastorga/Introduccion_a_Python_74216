'''
1.- Pedir al usuario una cantidad determinada de numeros a ingresar
2.- En base esa cantidad, solicitar dicha cantidad de numeros
3.- Agregar los numeros ingresados a una lista, separandolos por pares e impares
4.- Mostrar la cantidad de numeros pares e impares ingresados, y los numeros como tal
'''

""" numeros_pares = []
numeros_impares = []

cantidad = int(input("¿Cuántos números quieres ingresar? >>"))

for i in range(cantidad):
    print(i)
    numero = int(input("Ingrese el numero " + str(i + 1) + ">>>"))
    
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
        
print("Cantidad de numeros pares: " + str(len(numeros_pares))+ ". Numeros pares: " + str(numeros_pares))
print("Cantidad de numeros impares: " + str(len(numeros_impares))+ ". Numeros pares: " + str(numeros_impares))  """

##########PROYECTO INTEGRADOR ETAPA 2##########

""" def verificar_str(dato):
    while dato == "":
        print("Error, dato vacío")
        dato = input("Ingrese el dato nuevamente: ")
    return dato

def verificar_int(dato):
    while dato.isdecimal() == False:
        print("Error, ingrese solo numeros")
        dato = print("Ingrese el dato nuevamente")
    return dato

alumnos = {}

while True:
    print('''
        1.- Añadir alumno a la lista
        2.- Ver lista de alumnos
        3.- Ver cursos del alumno
        4.- Salir
        ''')
    
    opcion = input("Ingrese la opcion deseada >>> ")
    if opcion == "1":
        nombre_alumno = input("Ingrese el nombre del alumno >>> ")
        nombre_alumno = verificar_str(nombre_alumno)
        cursos = input("Ingrese la cantidad de curso >>> ")
        cursos = int(verificar_int(cursos))
        alumnos[nombre_alumno] = cursos
        print("El alumno se ha ingresado correctamente")
    elif opcion == "2":
        print("Lista de alumnos: ")
        for nombre in alumnos:
            cursos = alumnos[nombre]
            print("Nombre: " + nombre + " - " + str(cursos) + " cursos" )
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno a consultar >>>")
        if nombre in alumnos:
            print(nombre + " tiene " + str(cursos) + "cursos")
        else:
            print("El alumno no esta en la lista")
    elif opcion == "4":
        print("Gracias por usar el programa!")
        break
    else:
        print("La opcion ingresada no es válida, intente nuevamente") """
        
""" def min_y_max(lista):
    menor = min(lista)
    mayor = max(lista)
    
    return [menor, mayor]

numeros = [10, 20, 50, 5]
print(min_y_max(numeros)) """

""" import time

time.sleep(5)
print(time.asctime()) """

""" import time
import random


while True:
    numero = random.randint(1,20)
    if numero == 5:
        print(numero)
        break
    print(numero)
    time.sleep(1) """
    
""" import random

sorteo = []
carton = []
acertados = []


def hacer_sorteo():
    while len(sorteo) < 6:
        numero = random.randint(1, 40)
        if numero not in sorteo:
            sorteo.append(numero)
    sorteo.sort()
    print("Numeros sorteados: "+ str(sorteo) + "\n")

def comprar_numeros():
    numeros = 1
    while numeros <= 6:
        numero = int(input("Ingrese el " + str(numeros) + " numero deseado: "))
        if numero > 40 or numero <= 0:
            print("\nEl numero debe ser entre 1 y 40")
        else:
            if numero in carton:
                print("\nEl numero ya fue agregado, intente con otro")
            else:
                carton.append(numero)
                numeros += 1
                print("\nNumero agregado con éxito")
    carton.sort()
    print("\nLos numeros comprados son: " + str(carton))

def verificar_resultados():
    for numero in sorteo:
        if numero in carton:
            acertados.append(numero)
            print("\nAcertaste el "+ str(numero))
        else:
            print("\nNo acertaste el " + str(numero))
            
    if len(acertados) == 6:
        print("\nFELICITACIONES!!! GANASTE EL PREMIO MAYOR!!!")
    elif len(acertados) == 5:
        print("\nFelicitaciones! Ganaste el premio menor.")
    else:
        print("\nLo sentimos, no ganaste nada JAJAJAA xD")

comprar_numeros()
hacer_sorteo()
verificar_resultados() """


import random

while True:
    print("""
        ##################JUEGO DE DADOS##################
        1.- Tirar dados
        2.- Salir
        """)
    
    opcion = input("Ingrese la opcion deseada >>> ")
    if opcion == "1":
        usuario = random.randint(1,6)
        maquina = random.randint(1,6)
        print("\nDado usuario: " + str(usuario))
        print("Dado maquina: " + str(maquina))
        
        if usuario > maquina:
            print("\nFelicitaciones! Ganaste!\n")
        elif usuario < maquina:
            print("\nPerdiste, lo sentimos.\n")
        else:
            print("\nEmpate! Perdiste igual XD\n")
            
    elif opcion == "2":
        print("\nGracias por jugar con los dados! Vuelve pronto!")
        break
    else:
        print("\nLa opcion no es válida")