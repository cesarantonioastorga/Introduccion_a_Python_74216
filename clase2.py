#Comentario de linea

'''
Comentario
de
bloque
'''

#Operaciones arimeticas

""" suma = 2 + 5
resta = 7 - 3
division = 10 / 2
multiplicacion = 4 * 2 """

""" resto = 10 % 3
print(resto)

divison_entera = 10 // 3 
print(divison_entera)

potenciacion = 10 ** 3
print(potenciacion) """

#Operaciones de comparación

""" numero1 = 20
numero2 = 20

print(numero1 == numero2) #Igualdad
print(numero1 != numero2) #Desigualdad
print(numero1 > numero2) #Mayor que
print(numero1 < numero2) #Menor que
print(numero1 >= numero2) #Mayor o igual que
print(numero1 <= numero2) #Menor o igual que """

#Operaciones lógicas

""" numero1 = 10
numero2 = 20
numero3 = 30

#print(numero1 < numero2 and numero3 > numero2) #Ambos deben ser True
#print(numero1 > numero2 or numero3 < numero2) #Al menos uno debe ser True
print(not True)
print(not numero1 != 10)  """

#Condicionales

""" edad = 45

if edad > 30:
    print("Estas un poco viejito")
    if edad > 50:
        print("Uh ya pasaste los 50")
    else:
        print("Tenes entre 30 y 50")
else:
    print("Aun sos joven")
    
print("Fin del programa") """

'''
Crear un programa que pida usuario y contraseña en base al tipo de usuario
Primer usuario sera "root" y el segundo usuario sera "user"
Primero preguntar que usuario es y luego pedir las respectivas credenciales
Si las credenciales son correctas, mostrar un mensaje de bienvenida
Si las credenciales no son correctas mostrar un mensaje de acceso dengeado
'''

""" usuario = "root" #"user"

root = "admin"
pass_root = "abc123"

user = "usuario"
pass_user = "pepitolospalotes" """

""" 
nombre = input("Ingrese su nombre: ")
print("Hola!", nombre) """

tipo_usuario = input("Ingrese el tipo de usuario ('root' o 'default'): ")
print(type(tipo_usuario))
if tipo_usuario == "root":
    root = "admin"
    pass_root = "admin"
    usuario = input("Ingrese el usuario root: ")
    password = input("Ingrese la contraseña root: ")
    if root == usuario and pass_root == password:
        print("Acceso correcto a root")
    else:
        print("Acceso denegado")
elif tipo_usuario == "default":
    default = "usuario"
    default_root = "abc123"
    usuario = input("Ingrese el usuario default: ")
    password = input("Ingrese la contraseña default: ")
    if default == usuario and default_root == password:
        print("Acceso correcto a default")
    else:
        print("Acceso denegado")
else:
    print("El tipo de usuario no existe")