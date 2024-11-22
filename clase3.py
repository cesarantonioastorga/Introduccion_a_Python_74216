""" numero = input("Ingrese un numero: ")
print(numero)
print(type(numero))
numero = int(numero)
print(numero)
print(type(numero))
suma = 10 + numero
print(suma) """

""" numero = float(input("Ingrese un numero: "))
suma = 10 + numero
print(suma)

entero = 20
cadena = str(entero)
print(type(cadena)) """

""" numero1 = "as"
numero2 = "ds"

boleano1 = bool(numero1)
boleano2 = bool(numero2)

print(boleano1)
print(boleano2) """

'''
1.- Crear las variables con los tipos de dolar
2.- Pedir al usuario la cantidad de dolares a cambiar
3.- Pedir al usuario el tipo de dolar a convertir (Crear un menú de opciones)
4.- En base a las opciones ingresadas, mostrar la conversión por la consola
'''

""" dolar_blue = 1110.0
dolar_oficial = 981.0
dolar_mep = 1106.10
dolar_liqui = 1141.60
dolar_cripto = 1144.67

dolar_convertir = float(input("Ingrese los dolares a convertir: "))

print("##########TIPOS DE DOLAR##########")
print("1.- Dolar Blue")
print("2.- Dolar Oficial")
print("3.- Dolar MEP")
print("4.- Dolar Liqui")
print("5.- Dolar Cripto")
tipo_cambio = input("Ingrese la opcion del tipo de cambio que desea: ")

if tipo_cambio == "1":
    pesos = dolar_convertir * dolar_blue
    print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
elif tipo_cambio == "2":
    pesos = dolar_convertir * dolar_oficial
    print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
elif tipo_cambio == "3":
    pesos = dolar_convertir * dolar_mep
    print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
elif tipo_cambio == "4":
    pesos = dolar_convertir * dolar_liqui
    print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
elif tipo_cambio == "5":
    pesos = dolar_convertir * dolar_cripto
    print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
else:
    print("La opción ingresada no es válida, adios!") """
    
'''
1.- Crear un programa que evalue si el numero ingresado por el ususario es par o impar
'''

""" numero = int(input("Introduce un numero entero: "))
if numero % 2 == 0:
    print("El numero " + str(numero) + " es par")
else:
    print("El numero " + str(numero) + " es impar") """
    
'''
Crear un programa que evalue una nota ingresada por el usuario
Si la nota es 10, mostar un mensaje de felicitaciones
Si la nota es entre 6 y 10, mostrar que aprobo el examen
Si la nota es inferior mostrar que reporbo
Si la nota no esta ente 0 y 10 mostrar un mensaje de error
'''

""" nota = float(input("Ingrese su nota: "))
if nota >= 6 and nota <= 10:
    print("Aprobado")
    if nota == 10:
        print("¡Felicidades!")
elif nota < 6 and nota >= 1:
    print("Desaprobado")
else:
    print("La nota ingresada no es válida.") """
    
#contador = 1

""" while contador <= 10:
    print(contador)
    contador += 1 """
    
""" while True:
    if contador <= 10:
        print(str(contador)+ " ciclo.")
        contador += 1
    else:
        print("Fin del programa")
        break """
        
while True:
    print("##########CAMBIO DOLAR##########")
    print("1.- Convertir")
    print("2.- Salir")
    opcion = input("Ingrese la opcion deseada: ")
    if opcion == "2":
        print("Gracias por usar el programa.")
        break
    else:
        dolar_blue = 1110.0
        dolar_oficial = 981.0
        dolar_mep = 1106.10
        dolar_liqui = 1141.60
        dolar_cripto = 1144.67

        dolar_convertir = float(input("Ingrese los dolares a convertir: "))

        print("##########TIPOS DE DOLAR##########")
        print("1.- Dolar Blue")
        print("2.- Dolar Oficial")
        print("3.- Dolar MEP")
        print("4.- Dolar Liqui")
        print("5.- Dolar Cripto")
        tipo_cambio = input("Ingrese la opcion del tipo de cambio que desea: ")

        if tipo_cambio == "1":
            pesos = dolar_convertir * dolar_blue
            print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
        elif tipo_cambio == "2":
            pesos = dolar_convertir * dolar_oficial
            print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
        elif tipo_cambio == "3":
            pesos = dolar_convertir * dolar_mep
            print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
        elif tipo_cambio == "4":
            pesos = dolar_convertir * dolar_liqui
            print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
        elif tipo_cambio == "5":
            pesos = dolar_convertir * dolar_cripto
            print("Con " + str(dolar_convertir) + " dolares, recibes: " + str(pesos) + " pesos.")
        else:
            print("La opción ingresada no es válida")