from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")

display = Entry(ventana)
# Entrada de usuario
display.grid(row=0, columnspan=4, sticky=W+E)

# Números
Button(ventana, text="1").grid(row=1, column=0)
Button(ventana, text="2").grid(row=1, column=1)
Button(ventana, text="3").grid(row=1, column=2)

Button(ventana, text="4").grid(row=2, column=0)
Button(ventana, text="5").grid(row=2, column=1)
Button(ventana, text="6").grid(row=2, column=2)

Button(ventana, text="7").grid(row=3, column=0)
Button(ventana, text="8").grid(row=3, column=1)
Button(ventana, text="9").grid(row=3, column=2)

# Signos
Button(ventana, text="+").grid(row=1, column=3)
Button(ventana, text="-").grid(row=2, column=3)
Button(ventana, text="*").grid(row=3, column=3)
Button(ventana, text="/").grid(row=4, column=3)

# Borrar, modulo y 0
Button(ventana, text="AC").grid(row=4, column=0)
Button(ventana, text="0").grid(row=4, column=1)
Button(ventana, text="%").grid(row=4, column=2)

ventana.mainloop()