import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Canvas con Scroll")

# Frame principal
frame = tk.Frame(ventana)
frame.pack(fill=tk.BOTH, expand=True)

# Canvas con barra de desplazamiento
canvas = tk.Canvas(frame, bg="white", width=400, height=300)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Frame interno
frame_interno = tk.Frame(canvas, bg="lightblue")
canvas.create_window((0, 0), window=frame_interno, anchor="nw")

# Agregar contenido al Frame interno
for i in range(50):
    tk.Label(frame_interno, text=f"Etiqueta {i+1}").pack()

# Configurar el tamaño del canvas para que funcione el scroll
def configurar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_interno.bind("<Configure>", configurar_scroll)

ventana.mainloop()
