#Matrices

""" matriz = ["Juan",
          [2,3,4], 
          "Diego",
          [1,2,3, ["Luis", "Pablo"]],
          "David"
          ]

print(matriz[3][3][1]) """

""" personas = [
    ["Ana", "Ingeniera de Software", 35],
    ["Carlos", "Médico", 42],
    ["Laura", "Profesora", 28],
    ["Miguel", "Arquitecto", 39]
] """


####PROYECTO INTEGRADOR####

""" alumnos = []

while True:
    print('''
        ############## ALUMNI ##############
        1.- Ver lista de alumnos.
        2.- Añadir alumno a la lista
        3.- Salir
        ####################################
        ''')
    opcion = input("Ingrese la opcion desdeada >>> ")
    if opcion == "1":
        if len(alumnos) == 0:
            print("\nNo hay alumnos registrados\n")
        else:
            for alumno in alumnos:
                print(alumno)
    elif opcion == "2":
        nombre_alumno = input("Ingrese el nombre del alumno >>> ")
        cursos_alumno = input("Ingrese la cantidad de cursos del alumno >>> ")
        if nombre_alumno == "" or cursos_alumno == "":
            print("\nError, uno o ambos datos están vacíos\n")
        else:
            alumno = nombre_alumno + " - " + cursos_alumno
            alumnos.append(alumno)
            print("\nEl alumno "+ nombre_alumno  + " se ha agregado correctamente\n")
    elif opcion == "3":
        print("Gracias por usar el programa, Adios! :D")
        break
    else:
        print("La opción ingresada no es válida. Intente nuevamente.") """
        

####COLECCIONES####

""" tupla = ("Juan", 1, 4.0, True)
print(tupla[3])
tupla.insert(0, "Diego") """
""" 
diccionario = {
    "juan": 3,
    "diego":5
    }

print(diccionario["diego"])
diccionario["pedro"] = 10
print(diccionario)
del diccionario["juan"]
print(diccionario) """

""" for nombre in diccionario:
    print(nombre)
    print(diccionario[nombre])
print(diccionario) """

#print("pablo" in diccionario)


'''
Crear un diccionario de productos
pedirle al usuario los productos a ingresar
Si el producto no existe, indicarle que no hay stock
Si el producto exite agregarlo a un diccionario carrito
Mostrar los productos  elegidos por la consola junto con el total
'''

productos = {
    "yerba":3900,
    "endulzante":1900,
    "arroz":2200,
    "aceite":3000,
    "fideos":900,
    "leche":890
}

carrito = {}
total = 0

while True:
    print("########SUPERMERCADO JUANITO########")
    producto = input("Ingrese el nombre del producto a comprar (o 'pagar' si desea finalizar) >>> ").strip().lower()
    
    if producto == 'pagar':
        break
    elif producto in productos:
        carrito[producto] = productos[producto]
        total += productos[producto]
        print("\nEl producto " + producto + " se ha agregado correctamente\n")
    else:
        print("\nNo hay stock de ese producto, disculpe el inconveniente.\n")
        
print("Productos seleccionados: ", carrito)
print("El total a pagar es de: $"+ str(total) + " pesos")