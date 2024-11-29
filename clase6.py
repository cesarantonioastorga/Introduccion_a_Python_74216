""" numero = 0
while numero <=10:
    print(numero)
    numero += 1
    
numeros = [0,1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    print(numero) """

#range(inicio, fin -1)
""" for numero in range(0,101,3):
    print(numero) """
    
'''
Crear un programa que reciba del usuario dos numero, un inicio de rango y un fin de rango
pasar esos datos a range como argumento y en base a ese rango mostrar los numero multiplos de 3 y 5
Crear una lista vacia para ir agregando esos mutiplos
'''

""" inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el fin del rango: "))
rango = range(inicio, fin + 1)
multiplos = []

for numero in rango:
    if numero % 3 == 0 and numero % 5 == 0:
        multiplos.append(numero)
print("Los números múltiplos de 3 y 5 en el rango son:", multiplos) """

""" edad = input("Ingrese su edad: ")
if edad.isdecimal():
    if int(edad) >= 18:
        print("Sos mayor de edad")
else:
    print("El dato ingresado no es un numero") """
    
############FUNCIONES#############


""" def menu_principal():
    print("######MENU######")
    print("Opcion 1")
    print("Opcion 2")
    print("Opcion 3")
    print("Opcion 4")
    
menu_principal()
ingreso = input("Ingrese la opcion deseada: ")
if ingreso == "1":
    print("uno")
    
menu_principal()
ingreso = input("Ingrese la opcion deseada: ")
if ingreso == "1":
    print("otro uno")
    
menu_principal()
ingreso = input("Ingrese la opcion deseada: ")
if ingreso == "1":
    print("otro uno mas") """
    
""" def sumar(numero1, numero2):
    suma = numero1 + numero2
    print("La suma de " + str(numero1) + " + " + str(numero2) + " = " + str(suma))
    
sumar(10,20)
sumar(5,3) """

""" def mostrar_lista(lista):
    for i in lista:
        print(i)
        
alumnos = ["Juan", "David", "Andres", "Lucia"]
notas = [5,6,3,7,5,6,7]

mostrar_lista(alumnos)
mostrar_lista(notas) """

""" def sumar(numero1, numero2):
    suma = numero1 + numero2
    print(suma)
    return "La suma es: " +  str(suma)

producto1 = 3000
producto2 = 5000
total = sumar(producto1, producto2)
print(total) """

'''
Crear funcion para las diferentes operacion matematicas (+, -, /, *)
La division no puede ser realizada si el divisor es cero
Crear un menu para que el usuario ingrese la opcion deseada
Pedir al usuario los numeros a calcular
Mostrar el resultado haciendo uso de las funciones
'''
""" def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b != 0:
        return a / b
    else:
        print("No se puede dividir por cero")
        return "Error"

while True:
    print("######CALCULADORA#######")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")
    print("5.- Salir")
    opcion = input("Ingrese la opción deseada: ")
    if opcion in ["1","2","3","4"]:
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        if opcion == "1":
            resultado = sumar(numero1, numero2)
            print("Resultado de la suma: " +  str(resultado))
        elif opcion == "2":
            resultado = restar(numero1, numero2)
            print("Resultado de la resta:: "+ str(resultado))
        elif opcion == "3":
            resultado = dividir(numero1, numero2)
            print("Resultado de la division: " + str(resultado))
        elif opcion == "4":
            resultado = multiplicar(numero1, numero2)
            print("Resultado de la multiplicacion: " + str(resultado))
    elif opcion != "5":
        print("Error, la opcion ingresada no es válida")
    else:
        print("Gracias por usar la calculadora")
        break """
        
numero = 10
#print(numero)

""" def funcion():
    suma = 10 + 20
    print(suma)
    print(numero) """
    
def funcion():
    global numero
    numero = 30
    print("Desde la funcion: " + str(numero))
    
print("Global: " + str(numero))
funcion()
print("Global: " + str(numero))
