import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime


# Función para agregar un evento a la lista
def agregar_evento():
    # Obtener los valores de los campos de entrada
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    # Validar que todos los campos estén llenos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Datos faltantes", "Todos los campos deben estar completos.")
        return

    # Validar que la hora esté en el formato correcto
    try:
        datetime.datetime.strptime(hora, '%H:%M')  # Formato de hora: HH:MM
    except ValueError:
        messagebox.showwarning("Formato incorrecto", "Por favor ingrese la hora en formato HH:MM.")
        return

    # Si todo está correcto, agregar el evento al Treeview
    treeview.insert("", "end", values=(fecha, hora, descripcion))
    # Limpiar los campos de entrada de hora y descripción
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)


# Función para eliminar el evento seleccionado
def eliminar_evento():
    # Obtener la selección del usuario
    seleccionado = treeview.selection()

    # Verificar que algo esté seleccionado
    if not seleccionado:
        messagebox.showwarning("Selección", "Por favor seleccione un evento para eliminar.")
        return

    # Preguntar confirmación antes de eliminar
    confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar este evento?")
    if confirmacion:
        treeview.delete(seleccionado)  # Eliminar el evento del Treeview


# Configurar la ventana principal
root = tk.Tk()
root.title("Agenda Personal")  # Título de la ventana
root.geometry("500x400")  # Establecer el tamaño de la ventana

# Frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Configurar el Treeview para mostrar los eventos
treeview = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
treeview.heading("Fecha", text="Fecha")  # Encabezado de columna para la fecha
treeview.heading("Hora", text="Hora")  # Encabezado de columna para la hora
treeview.heading("Descripción", text="Descripción")  # Encabezado de columna para la descripción
treeview.pack()

# Frame para la entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada
label_fecha = tk.Label(frame_entrada, text="Fecha (AAAA-MM-DD):")
label_fecha.grid(row=0, column=0, padx=5, pady=5)  # Etiqueta para la fecha

# Usar DateEntry en lugar de Entry para la fecha
entry_fecha = DateEntry(frame_entrada, date_pattern='y-mm-dd')
entry_fecha.grid(row=0, column=1, padx=5, pady=5)  # Campo de entrada para la fecha

label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0, padx=5, pady=5)  # Etiqueta para la hora
entry_hora = tk.Entry(frame_entrada)  # Campo de entrada para la hora
entry_hora.grid(row=1, column=1, padx=5, pady=5)

label_desc = tk.Label(frame_entrada, text="Descripción:")
label_desc.grid(row=2, column=0, padx=5, pady=5)  # Etiqueta para la descripción
entry_desc = tk.Entry(frame_entrada)  # Campo de entrada para la descripción
entry_desc.grid(row=2, column=1, padx=5, pady=5)

# Frame para los botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para agregar un nuevo evento
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)  # Colocar el botón en la interfaz

# Botón para eliminar el evento seleccionado
btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)  # Colocar el botón en la interfaz

# Botón para salir de la aplicación
btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=10)  # Colocar el botón en la interfaz

# Iniciar el loop principal de la aplicación
root.mainloop()
