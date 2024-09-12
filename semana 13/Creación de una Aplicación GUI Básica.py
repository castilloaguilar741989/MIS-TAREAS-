import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Gestión de Datos")

# Lista donde se almacenarán los datos
data_list = []

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry.get()
    if dato:
        data_list.append(dato)
        actualizar_lista()
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para actualizar la lista visualmente
def actualizar_lista():
    listbox.delete(0, tk.END)  # Limpiar la lista actual
    for item in data_list:
        listbox.insert(tk.END, item)  # Agregar los datos a la lista

# Función para limpiar toda la lista
def limpiar_lista():
    data_list.clear()
    actualizar_lista()

# Etiqueta para el campo de entrada
label = tk.Label(root, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto para ingresar datos
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Botón para agregar el dato
add_button = tk.Button(root, text="Agregar", command=agregar_dato)
add_button.pack(pady=5)

# Listbox para mostrar los datos ingresados
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Botón para limpiar la lista
clear_button = tk.Button(root, text="Limpiar", command=limpiar_lista)
clear_button.pack(pady=5)

# Iniciar la ventana
root.mainloop()
