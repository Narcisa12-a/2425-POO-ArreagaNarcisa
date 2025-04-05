#Desarrolle una aplicacion GUI que permita a los usuarios gestionar una lista de tareas
#pendientes. La aplicación debera permitir añadir nuevas tareas, marcar tareas como completadas, y
#eliminar tareas utilizando tanto la interfaz grafica (clics de boton) como atajos de teclado.
import tkinter as tk

#Clase para gestionar la aplicación GUI de tareas
class TaskManager:
    def __init__(self, root):  #Corregido el nombre del constructor
        #Inicializa la ventana principal
        self.root = root
        #Lista para almacenar las tareas
        self.tasks = []
        #Componente para mostrar las tareas
        self.task_list = tk.Listbox(self.root)
        self.task_list.pack(padx=10, pady=10)
        #Campo de entrada para nuevas tareas
        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10, pady=5)
        #Botón para añadir tareas
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(padx=10, pady=5)
        #Botón para marcar tareas como completadas
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(padx=10, pady=5)
        #Botón para eliminar tareas
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=5)
        #Asigna atajos de teclado
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.root.bind("c", lambda event: self.complete_task())
        self.root.bind("d", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.destroy())
    #Función para añadir nuevas tareas
    def add_task(self):
        #Obtiene el texto del campo de entrada
        task = self.entry.get()
        if task:
            #Agrega la tarea a la lista y limpia el campo de entrada
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)
    #Función para marcar tareas como completadas
    def complete_task(self):
        try:
            #Obtiene el índice de la tarea seleccionada
            task_index = self.task_list.curselection()[0]
            task = self.tasks[task_index]
            #Marca la tarea como completada y actualiza la lista
            self.tasks[task_index] = f"[Completada] {task}"
            self.task_list.delete(task_index)
            self.task_list.insert(task_index, self.tasks[task_index])
        except IndexError:
            pass
    #Función para eliminar tareas
    def delete_task(self):
        try:
            #Obtiene el índice de la tarea seleccionada
            task_index = self.task_list.curselection()[0]
            #Elimina la tarea de la lista
            self.tasks.pop(task_index)
            self.task_list.delete(task_index)
        except IndexError:
            pass
#Inicializa la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestor de Tareas")
    app = TaskManager(root)
    root.mainloop()

