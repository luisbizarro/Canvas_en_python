import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Canvas para Widgets")

# Crear un Canvas
canvas = tk.Canvas(ventana, width=400, height=300, bg="lightgray")
canvas.pack()

# Crear widgets
label = tk.Label(canvas, text="¡Hola, soy un Label!", bg="white")
boton = tk.Button(canvas, text="Haz clic", command=lambda: print("¡Botón presionado!"))

# Colocar widgets en posiciones específicas dentro del Canvas
canvas.create_window(100, 50, window=label)
canvas.create_window(200, 150, window=boton)

ventana.mainloop()
