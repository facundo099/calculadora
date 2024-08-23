from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")

display = Entry(ventana)
# Entrada de usuario
display.grid(row=0, columnspan=4, sticky=W+E)

i = 0

def escribir_numeros(numero):
    global i
    display.insert(i, numero)
    i += 1

def escribir_operador(operador):
    global i
    longitud = len(operador)
    display.insert(i, operador)
    i += longitud

def limpiar():
    display.delete(0, END)

def borrar():
    estado_display = display.get()
    if len(estado_display):
        nuevo_estado = estado_display[:-1]
        limpiar()
        display.insert(0, nuevo_estado)
    else:
        limpiar()

def calcular():
    estado_display = display.get()
    try:
        resultado = eval(estado_display)
        limpiar()
        display.insert(0, resultado)
    except Exception:
        limpiar()
        display.insert(0, "Error")



# Números
Button(ventana, text="1", command=lambda:escribir_numeros(1)).grid(row=1, column=0, sticky=W+E)
Button(ventana, text="2", command=lambda:escribir_numeros(2)).grid(row=1, column=1, sticky=W+E)
Button(ventana, text="3", command=lambda:escribir_numeros(3)).grid(row=1, column=2, sticky=W+E)

Button(ventana, text="4", command=lambda:escribir_numeros(4)).grid(row=2, column=0, sticky=W+E)
Button(ventana, text="5", command=lambda:escribir_numeros(5)).grid(row=2, column=1, sticky=W+E)
Button(ventana, text="6", command=lambda:escribir_numeros(6)).grid(row=2, column=2, sticky=W+E)

Button(ventana, text="7", command=lambda:escribir_numeros(7)).grid(row=3, column=0, sticky=W+E)
Button(ventana, text="8", command=lambda:escribir_numeros(8)).grid(row=3, column=1, sticky=W+E)
Button(ventana, text="9", command=lambda:escribir_numeros(9)).grid(row=3, column=2, sticky=W+E)

# Signos
Button(ventana, text="+", command=lambda:escribir_operador("+")).grid(row=1, column=3, sticky=W+E)
Button(ventana, text="-", command=lambda:escribir_operador("-")).grid(row=2, column=3, sticky=W+E)
Button(ventana, text="*", command=lambda:escribir_operador("*")).grid(row=3, column=3, sticky=W+E)
Button(ventana, text="/", command=lambda:escribir_operador("/")).grid(row=4, column=3, sticky=W+E)
Button(ventana, text="(", command=lambda:escribir_operador("(")).grid(row=1, column=4, sticky=W+E)
Button(ventana, text=")", command=lambda:escribir_operador(")")).grid(row=2, column=4, sticky=W+E)
Button(ventana, text="=", command=lambda:calcular()).grid(row=3, column=4, sticky=W+E)

# Borrar, modulo y 0
Button(ventana, text="AC", command=lambda:limpiar()).grid(row=4, column=0, sticky=W+E)
Button(ventana, text="0" , command=lambda:escribir_numeros(0)).grid(row=4, column=1, sticky=W+E)
Button(ventana, text="⌫", command=lambda:borrar()).grid(row=4, column=2, sticky=W+E)


ventana.mainloop()