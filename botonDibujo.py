import tkinter as tk

def cambiar_color(color):
    global color_actual
    color_actual = color

def dibujar(event):
    x, y = event.x, event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=color_actual, outline=color_actual)

# Ventana principal
ventana = tk.Tk()
ventana.title("Interfaz con Canvas")

color_actual = "black"  # Color por defecto

# Crear un Canvas
canvas = tk.Canvas(ventana, width=500, height=400, bg="white")
canvas.pack()

# Vincular el evento del mouse para dibujar
canvas.bind("<B1-Motion>", dibujar)

# Botones para cambiar colores
frame_colores = tk.Frame(ventana)
frame_colores.pack()

colores = ["black", "red", "blue", "green", "yellow"]
for color in colores:
    boton = tk.Button(frame_colores, bg=color, width=5, command=lambda c=color: cambiar_color(c))
    boton.pack(side=tk.LEFT)

ventana.mainloop()
