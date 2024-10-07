import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x300")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Atajo para añadir tarea con 'Enter'

        # Botones de acción
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_task_complete)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista para mostrar tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Vinculación de atajos de teclado
        self.root.bind("<c>", self.mark_task_complete)  # Atajo 'C' para completar tarea
        self.root.bind("<d>", self.delete_task)  # Atajo 'D' para eliminar tarea
        self.root.bind("<Delete>", self.delete_task)  # Atajo 'Delete' para eliminar tarea
        self.root.bind("<Escape>", lambda e: self.root.quit())  # Atajo 'Escape' para salir

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.update_task_list()
            self.entry.delete(0, tk.END)  # Limpiar campo de entrada
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía")

    def mark_task_complete(self, event=None):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]['completed'] = True
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla como completada")

    def delete_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task['task']
            if task['completed']:
                display_text += " (Completada)"
            self.task_listbox.insert(tk.END, display_text)


# Inicialización de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
