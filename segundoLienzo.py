# Dibuja una linea cuando se da click
import tkinter as tk
def dibujar_linea(event):
    x, y = event.x, event.y
    canvas.create_line(200, 150, x, y, fill="purple", width=2)

ventana = tk.Tk()
ventana.title("Canvas Interactivo")

canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack()

# Vincular clic del ratón al evento
canvas.bind("<Button-1>", dibujar_linea)

ventana.mainloop()
