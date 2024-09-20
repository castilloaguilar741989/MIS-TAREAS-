import tkinter as tk
from tkinter import ttk, messagebox
import datetime


# Función para agregar un evento a la lista
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    # Verificar que todos los campos estén llenos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Datos faltantes", "Todos los campos deben estar completos.")
        return

    try:
        # Verificar formato de fecha y hora
        datetime.datetime.strptime(fecha, '%Y-%m-%d')  # Formato de fecha: Año-Mes-Día
        datetime.datetime.strptime(hora, '%H:%M')  # Formato de hora: HH:MM
    except ValueError:
        messagebox.showwarning("Formato incorrecto",
                               "Por favor ingrese la fecha en formato AAAA-MM-DD y la hora en formato HH:MM.")
        return

    # Agregar a la Treeview
    treeview.insert("", "end", values=(fecha, hora, descripcion))
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)


# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccionado = treeview.selection()
    if not seleccionado:
        messagebox.showwarning("Selección", "Por favor seleccione un evento para eliminar.")
        return

    confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar este evento?")
    if confirmacion:
        treeview.delete(seleccionado)


# Configurar la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Treeview para mostrar los eventos
treeview = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
treeview.heading("Fecha", text="Fecha")
treeview.heading("Hora", text="Hora")
treeview.heading("Descripción", text="Descripción")
treeview.pack()

# Frame para la entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada
label_fecha = tk.Label(frame_entrada, text="Fecha (AAAA-MM-DD):")
label_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

label_desc = tk.Label(frame_entrada, text="Descripción:")
label_desc.grid(row=2, column=0, padx=5, pady=5)
entry_desc = tk.Entry(frame_entrada)
entry_desc.grid(row=2, column=1, padx=5, pady=5)

# Frame para los botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botones
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=10)

# Iniciar el loop principal de la aplicación
root.mainloop()
