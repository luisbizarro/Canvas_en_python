import tkinter as tk


def rectangulo_redondeado(canvas, x1, y1, x2, y2, radio, **opciones):
    """
    Dibuja un rectángulo con bordes redondeados en un Canvas.

    Parámetros:
    - canvas: El lienzo donde dibujar.
    - x1, y1: Esquina superior izquierda.
    - x2, y2: Esquina inferior derecha.
    - radio: Radio de las esquinas redondeadas.
    - **opciones: Opciones adicionales como fill, outline, etc.
    """
    # Rectángulo central
    canvas.create_rectangle(x1 + radio, y1, x2 - radio, y2, **opciones)
    canvas.create_rectangle(x1, y1 + radio, x2, y2 - radio, **opciones)

    # Esquinas redondeadas
    canvas.create_oval(x1, y1, x1 + 2 * radio, y1 + 2 * radio, **opciones)  # Esquina superior izquierda
    canvas.create_oval(x2 - 2 * radio, y1, x2, y1 + 2 * radio, **opciones)  # Esquina superior derecha
    canvas.create_oval(x1, y2 - 2 * radio, x1 + 2 * radio, y2, **opciones)  # Esquina inferior izquierda
    canvas.create_oval(x2 - 2 * radio, y2 - 2 * radio, x2, y2, **opciones)  # Esquina inferior derecha


# Ventana principal
ventana = tk.Tk()
ventana.title("Rectángulo con Bordes Redondeados")

# Crear un Canvas
canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack()

# Dibujar un rectángulo con bordes redondeados
rectangulo_redondeado(canvas, 50, 50, 300, 200, 20, fill="lightblue", outline="blue", width=2)

ventana.mainloop()
