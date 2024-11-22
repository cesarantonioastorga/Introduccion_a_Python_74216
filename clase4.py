'''
Crear un programa que adivine un numero secreto
Si el usuario ingresa un numero mayor, debe indicarle que el numero secreto es menor
Si el usuario ingresa un numero menor, debe indicarle que el numero secreto es mayor
Si el usuario adivina el numero, mostrar el numero secreto y la cantidad de intentos (contador)
'''
""" 
alumno1= "Juan Perez"
alumno2= "Diego Tapia"
alumno3= "Luis Soto" """
""" 
alumnos = ["Juan Perez", "Diego Tapia", "Luis Soto"]
notas = [10.0, 7.0, 5.0]
datos = ["Texto", 1, True, 2.0]
print(alumnos[1])
print(alumnos[-2])

alumnos.append("Leandro Enrietto")
print(alumnos)
alumnos.append("Ezequiel Pane")
print(alumnos)
alumnos.insert(1,"Juan Angulo")
print(alumnos)

del alumnos[0]
print(alumnos)
alumnos[2] = "Cesar Astorga"
print(alumnos)
print("El largo de la lista de alumnos: " + str(len(alumnos)) + "alumnos")
 """


'''
Crear un carrito de productos
Preguntar al usuario cuantos productos desea ingresar
En base a esa cantidad de productos, pedir los nombres de los productos
Cada producto ingresado agregarlo al carrito append()
Una vez agregados los productos, mostrar la cantidad y los productos ingresados
'''

""" while True:
    print("1.- Comprar\n2.- Salir")
    opcion = input("¿Que desea hacer?")
    if opcion == "1":
        carrito = []
        
        cantidad = int(input("¿Cuántos productos desea agregar?: "))
        
        while len(carrito)< cantidad:
            producto = input("Introduce el nombre del producto " + str(len(carrito)+1)+": ")
            carrito.append(producto)
            print(str(producto) + " se ha agregado al carrito")
        
        print("\nContenido del carrito: ")
        for producto in carrito:
            print(producto)
        
    else:
        print("Gracias por usar el carrito de compras")
        break """
        
alumnos = ["Juan", "Jose", "Pedro"]

print(alumnos[0])
print(alumnos[1])
print(alumnos[2])


for alumno in alumnos:
    print(alumno)
    
'''
1.- Ciclo
for "Juan" in alumnos:
    printn("Juan")
2.- Ciclo
for "Jose" in alumnos:
    printn("Jose")
3.- Ciclo
for "Pedro" in alumnos:
    printn("Pedro")
'''

'''
Crear un programa que calcule el iva y un descuento a una lista de precios
'''

precios = [20000.0, 100000.0, 50000.0]


for precio in precios:
    precio_iva = precio * 1.21
    precio_descuento = precio - (precio * 0.2)
    print("Precio: $" + str(precio))
    print("Precio con iva: $" + str(precio_iva))
    print("Precio con descuento: $" + str(precio_descuento))
    print("##############################")