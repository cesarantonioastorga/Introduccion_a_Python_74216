"""
import tkinter as tk

 def saludar():
    print(entrada.get())

ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Mi primera aplicación en Python")

label = tk.Label(text="Ingrese el saludo: ")
label.place(x=10, y=10)

entrada = tk.Entry()
entrada.place(x=10, y=40)

boton = tk.Button(text="Saludar", command=saludar)
boton.place(x=10, y=70)

ventana.mainloop() """

""" import tkinter as tk

valor_dolar = {
    "blue": 1105,
    "oficial": 1050,
    "bolsa": 1130,
    "liqui": 1120,
    "cripto": 1250,
    "tarjeta": 1650
}


def convertir_dolar():
    dolares = float(dolar.get())
    
    resultados = []
    for nombre, valor in valor_dolar.items():
        resultado = nombre + ": " + str(valor * dolares) + " pesos"
        resultados.append(resultado)
        
    cadena = "\n"+"#"*30 + "\n"+"\n".join(resultados) + "\n"+"#"*30
    
    conversion.config(text=cadena)

ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Dolar a peso")

label = tk.Label(text="Ingrese los dolares que desea cambiar: ")
label.place(x=10, y=10)

dolar = tk.Entry()
dolar.place(x=230, y=10, width=100)

convertir = tk.Button(text="Convertir", command=convertir_dolar)
convertir.place(x=10, y=40, width=100)

conversion = tk.Label(text="")
conversion.place(x=10, y=80)

ventana.mainloop() """

import tkinter as tk
import random

numeros = []
carton = []
acertados = []


def comprar_numeros():
    numero = int(numero_comprar.get())
    if numero > 40 or numero <=0:
       mensaje.config(text="El numero debe ser entre 1 y 40")
    elif numero in carton:
        mensaje.config(text="Ese numero ya fue agregado")
    else:
        carton.append(numero)
        carton.sort()
        comprados.config(text=carton)
        if len(carton) == 6:
            comprar.config(state=tk.DISABLED)
            sorteo.config(state=tk.NORMAL)

def hacer_sorteo():
    while len(numeros) < 6:
        numero = random.randint(1,40)
        if numero not in numeros:
            numeros.append(numero)
    numeros.sort()
    resultado_sorteo.config(text=numeros)
    sorteo.config(state=tk.DISABLED)
    resultado.config(state=tk.NORMAL)

def verificar_resultados():
    for numero in numeros:
        if numero in carton:
            acertados.append(numero)
    
    if len(acertados) == 6:
        mensaje.config(text="¡FELICITACIONES, HAZ GANADO LA LOTERIA!")
    elif len(acertados) == 5:
        mensaje.config(text="Ganaste el premio menor!")
    else:
        mensaje.config(text="No ganaste nada XD")
        

window = tk.Tk()
window.config(width=400, height=300)
window.title("Loteria")

###########COMPRAR NUMEROS###########
label_numero = tk.Label(text="Ingrese el numero que desea comprar: ")
label_numero.place(x=10, y=10)

numero_comprar = tk.Entry()
numero_comprar.place(x=230, y=10, width=20)

comprar = tk.Button(text="Comprar", command=comprar_numeros)
comprar.place(x=10, y=40, width=100)

label_comprados = tk.Label(text="Numeros comprados: ")
label_comprados.place(x=10, y=80)

comprados = tk.Label(text="")
comprados.place(x=130, y=80)

###########HACER SORTEO###########

sorteo = tk.Button(text="Sorteo", command=hacer_sorteo, state=tk.DISABLED)
sorteo.place(x=10, y=110, width=100)

label_sorteo = tk.Label(text="Numeros sorteados: ")
label_sorteo.place(x=10, y=150)

resultado_sorteo = tk.Label(text="")
resultado_sorteo.place(x=120, y=150)


###########VERIFICAR RESULTADOS###########

resultado = tk.Button(text="Resultado: ", command=verificar_resultados, state=tk.DISABLED)
resultado.place(x=10, y=190, width=100)

mensaje =tk.Label(text="")
mensaje.place(x=10, y=250)

window.mainloop()