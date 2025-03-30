#Desarrolle una aplicación GUI simple para gestionar una lista de tareas, permitiendo al
#usuario añadir nuevas tareas, marcarlas como hechas o completadas, y eliminarlas. La
#aplicación debera responder adecuadamente a los eventos del usuario, como clics del ratón y pulsaciones del teclado.
import tkinter as tk
from tkinter import ttk

class TaskManagerApp:
    def __init__(self, root):  #Inicialización del objeto principal
        self.root = root
        self.tasks = []  #Lista interna para almacenar tareas
        self.task_list = ttk.Treeview(self.root, columns=('Task', 'Status'), show='headings')
        #Configuración de columnas para la lista de tareas
        self.task_list.heading('Task', text='Tarea')
        self.task_list.heading('Status', text='Estado')
        self.task_list.column('Status', width=100)  #Ajuste de ancho para columna de estado
        #Configuración de la interfaz
        self.create_widgets()  #Crea todos los elementos gráficos
        self.configure_layout()  #Organiza la disposición de los widgets
        self.configure_events()  #Configura los eventos de interacción
    def create_widgets(self):
        #Campo de entrada para nuevas tareas
        self.entry = ttk.Entry(self.root, width=40)
        #Botones de acción
        self.add_btn = ttk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.complete_btn = ttk.Button(self.root, text="Marcar como Completada", command=self.mark_as_completed)
        self.delete_btn = ttk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        #Etiqueta para mostrar mensajes de estado
        self.status_label = ttk.Label(self.root, text="")
    def configure_layout(self):  #Organización de los widgets en la ventana
        self.task_list.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=5, pady=5)
        self.entry.grid(row=1, column=0, padx=5, pady=5)
        self.add_btn.grid(row=1, column=1, padx=5, pady=5)
        self.complete_btn.grid(row=2, column=0, padx=5, pady=5)
        self.delete_btn.grid(row=2, column=1, padx=5, pady=5)
        self.status_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        #Configuración de expansión de la ventana
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
    def configure_events(self):  #Eventos de interacción
        self.entry.bind('<Return>', lambda e: self.add_task())  #Enter para añadir tarea
        self.task_list.bind('<Double-Button-1>', lambda e: self.mark_as_completed())  #Doble clic para completar
    def add_task(self):  #Lógica para añadir nuevas tareas
        task_text = self.entry.get()
        if task_text:  #Verificación de entrada no vacía
            self.tasks.append({'text': task_text, 'completed': False})  #Almacenamiento en lista interna
            self.update_task_list()  #Actualización de la interfaz
            self.entry.delete(0, tk.END)  #Limpieza del campo de entrada
            self.status_label.config(text="Tarea añadida correctamente")  #Feedback al usuario
    def mark_as_completed(self):  #Lógica para marcar tareas como completadas
        selected = self.task_list.selection()
        if selected:  #Verificación de selección
            index = self.task_list.index(selected[0])  #Obtención del índice de la tarea
            self.tasks[index]['completed'] = not self.tasks[index]['completed']  #Alternancia de estado
            self.update_task_list()  #Actualización de la interfaz
            self.status_label.config(text="Estado actualizado")  #Feedback al usuario
    def delete_task(self):  #Lógica para eliminar tareas
        selected = self.task_list.selection()
        if selected:  #Verificación d seección
            index = self.task_list.index(selected[0])  #Obtención del índice de la tarea
            del self.tasks[index]  #Eliminación de la lista interna
            self.update_task_list()  #Actualización de la interfaz
            self.status_label.config(text="Tarea eliminada")  #Feedback al usuario
    def update_task_list(self):  #Actualización completa de la lista de tareas
        self.task_list.delete(*self.task_list.get_children())  #Limpieza de la lista
        for task in self.tasks:
            status = "Completada" if task['completed'] else "Pendiente"  #Determinación del estado
            self.task_list.insert('', 'end', values=(task['text'], status))  #Inserción de datos
            if task['completed']:
                self.task_list.item(self.task_list.get_children()[-1], tags=('completed',))  #Aplicación de estilo
        self.task_list.tag_configure('completed', foreground='green')  #Configuración del estilo para completadas

if __name__ == "__main__":
    #Inicialización de la aplicación
    root = tk.Tk()
    root.title("Lista de Tareas")  #Título de la ventana
    app = TaskManagerApp(root)
    root.mainloop()  #Bucle principal de la aplicación