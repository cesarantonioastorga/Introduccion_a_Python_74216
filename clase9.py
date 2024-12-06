""" import tkinter as tk

alumnos = {}

def verificar(dato):
    if dato == "":
        dato = "error"
    return dato

def convertir(valor):
    if valor.isdecimal():
        valor = int(valor)
    else:
        valor = "error"
    return valor

def ver():
    lista_resultados = []
    
    for nombre in alumnos:
        cursos = alumnos[nombre]
        lista_resultados.append(nombre + " - " + str(cursos)+ " cursos")
        
    resultados.config(text="\n".join(lista_resultados))
    

def agregar():
    nombre_alumno = caja_nombre.get()
    nombre_alumno = verificar(nombre_alumno)
    cursos = caja_cursos.get()
    cursos = convertir(cursos)
    if nombre_alumno == "error":
        resultados.config(text="Error, nombre vacio")
    elif cursos == "error":
        resultados.config(text="Error, ingrese solo numeros")
    else:
        alumnos[nombre_alumno] = cursos
        resultados.config(text="El alumno se ha agregado correctamente")

def ver_alumno():
    nombre = caja_nombre.get()
    if nombre in alumnos:
        resultados.config(text=nombre + " tiene " + str(alumnos[nombre]) + " cursos")
    else:
        resultados.config(text="Ese alumno no tiene cursos")



ventana = tk.Tk()

ventana.config(width=450, height=400)
ventana.title("Proyecto Integrador | Etapa 3")

#Nombre
etiqueta_nombre = tk.Label(text="Nombre alumno: ")
etiqueta_nombre.place(x=10, y=10)

caja_nombre = tk.Entry()
caja_nombre.place(x=110, y=10, width=150, height=20)

boton_cursos = tk.Button(text="Ver cantidad de cursos", command=ver_alumno)
boton_cursos.place(x=270, y=10)

#Cursos
etiqueta_cursos = tk.Label(text="Cursos: ")
etiqueta_cursos.place(x=10, y=40)

caja_cursos = tk.Entry()
caja_cursos.place(x=100, y=40, width=50, height=20)

boton_agregar = tk.Button(text="Agregar a la lsita", command=agregar)
boton_agregar.place(x=170, y=40)

#Lista de alumnos
boton_lista = tk.Button(text="Ver lista de alumnos", command=ver)
boton_lista.place(x=10, y=70)

#Mostrar información
resultados = tk.Label(text="")
resultados.place(x=10, y=100)

ventana.mainloop() """


'''
1.- Paradigma imperativo
Es darle instrucciones paso a paso a la computadora, diciendole exactamente que hacer y en que orden
'''

suma = 0

for i in range(1,11):
    suma += i

print("La suma de los primeros 10 numeros naturales es: ", suma)

'''
2.- Paradigma declarativo
Le decimos al programa que lograr pero no como hacerlo.
'''

numeros = [1,2,3,4,5,6,7,8,9,10]
pares =[]

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
        
print("Numeros pares: ", pares)


'''
3.- Paradigma lógico
Resolver un problema mediante un conjunto de reglas
'''

def puede_votar(edad):
    return edad >= 18

edad_usuario = int(input("Ingrese su edad: "))

if puede_votar(edad_usuario):
    print("Puede votar")
else:
    print("No puede votar")
    
'''
4.- Paradigma funcional
Trabaja con funciones como si fueran recetas usando datos de entrada y obteniendo resultados
'''

def sumar(lista):
    if not lista:
        return 0
    return lista[0] + sumar(lista[1:])

numeros = [1,2,3,4,5]
resultado = sumar(numeros)
print("La suma de todos los numeros es:", resultado)


'''
5.- Paradigma Orientado a objetos POO
Piensa en todo como objetos del mundo real, con sus respectivos atributos y metodos (caracteristicas y funciones)
'''

class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_info(self):
        return f"Auto: {self.marca} - {self.modelo}"
    

mi_auto = Auto("Toyota", "Corolla")
print(mi_auto.mostrar_info())