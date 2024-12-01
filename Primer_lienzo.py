import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Canvas")

# Crear el widget Canvas
canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack()

# Dibujar una línea
canvas.create_line(50, 50, 200, 50, fill="blue", width=2)

# Dibujar un rectángulo
canvas.create_rectangle(100, 100, 250, 200, outline="red", width=3)

# Dibujar un círculo (usando create_oval)
canvas.create_oval(50, 100, 150, 200, fill="yellow")

# Dibujar texto
canvas.create_text(200, 250, text="¡Hola, Canvas!", font=("Arial", 16), fill="green")

# Mostrar la ventana
ventana.mainloop()
