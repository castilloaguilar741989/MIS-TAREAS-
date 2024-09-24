import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task():
    task = task_entry.get()  # Obtener el texto de la entrada
    if task != "":
        task_listbox.insert(tk.END, task)  # Insertar la nueva tarea al final de la lista
        task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Input Error", "No puedes añadir una tarea vacía")  # Mensaje de error si el campo está vacío

# Función para marcar una tarea como completada
def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
        task = task_listbox.get(selected_task_index)  # Obtener el texto de la tarea
        task_listbox.delete(selected_task_index)  # Eliminar la tarea seleccionada
        task_listbox.insert(tk.END, f"{task} - Completada")  # Insertar la tarea marcada como completada
    except IndexError:
        messagebox.showwarning("Selection Error", "Selecciona una tarea para marcarla como completada")  # Mensaje de error si no hay selección

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
        task_listbox.delete(selected_task_index)  # Eliminar la tarea de la lista
    except IndexError:
        messagebox.showwarning("Selection Error", "Selecciona una tarea para eliminarla")  # Mensaje de error si no hay selección

# Función para manejar la tecla Enter en el campo de entrada
def on_enter_key(event):
    add_task()  # Añadir la tarea cuando se presiona Enter

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada para nuevas tareas
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

# Botón para añadir tareas
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

# Lista de tareas (Listbox)
task_listbox = tk.Listbox(root, width=35, height=10)
task_listbox.pack(pady=10)

# Botón para marcar una tarea como completada
mark_completed_button = tk.Button(root, text="Marcar como Completada", command=mark_task_completed)
mark_completed_button.pack(pady=5)

# Botón para eliminar una tarea
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Vincular la tecla Enter con la función add_task
task_entry.bind("<Return>", on_enter_key)

# Iniciar el bucle principal de la aplicación
root.mainloop()
