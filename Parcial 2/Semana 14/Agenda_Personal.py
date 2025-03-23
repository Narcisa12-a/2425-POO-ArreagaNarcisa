#Desarrollar una aplicación GUI utilizando Tkinter que funciones como una agenga personal
#La aplicación permitira al usuario agregar, ver y eliminar eventos o tareas.
#Importar las librerias necesarias
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
#Agregar ventana
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("800x600")
#Frame para el calendario
frame_calendario = tk.Frame(ventana)
frame_calendario.pack(fill="both", expand=True, side="left")
#Frame para la lista de eventos y entrada de datos
frame_eventos = tk.Frame(ventana)
frame_eventos.pack(fill="both", expand=True, side="right")
#Frame para la lista de eventos
frame_lista = tk.Frame(frame_eventos)
frame_lista.pack(fill="both", expand=True)
#Frame para la entrada de datos
frame_entrada = tk.Frame(frame_eventos)
frame_entrada.pack(fill="x")
#Frame para los botones de accion
frame_botones = tk.Frame(frame_eventos)
frame_botones.pack(fill="x")
calendario = Calendar(frame_calendario,selectmode='day', year=2025, month=3, day=21)
calendario.pack(fill="both", expand=True)

#Configuracion de columnas
columnas = ["Fecha", "Hora", "Descripción"]
tree = ttk.Treeview(frame_lista,columns=columnas, show="headings")
for columna in columnas:
    tree.heading(columna, text=columna)
tree.pack(fill="both", expand=True)

#Fecha
label_fecha = tk.Label(frame_entrada, text="Fecha:")
label_fecha.pack(side="left")
fecha_label = tk.Label(frame_entrada, width=12)
fecha_label.pack(side="left")
#Hora
label_hora = tk.Label(frame_entrada, text="Hora:")
label_hora.pack(side="left")
hora_entry= tk.Entry(frame_entrada, width=5)
hora_entry.pack(side="left")
#Descripcion
label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.pack(side="left")
descripcion_entry = tk.Entry(frame_entrada, width=20)
descripcion_entry.pack(side="left")
#Metodo para agregar una fecha
def seleccionar_fecha():
    fecha = calendario.selection_get()
    fecha_label.config(text=fecha.strftime("%Y-%m-%d"))
#Metodo para agregar un evento
def agregar_evento():
    fecha = fecha_label.cget("text")
    if fecha:
        hora = hora_entry.get()
        descripcion =(
            descripcion_entry.get())
        tree.insert("", "end", values=[fecha, hora, descripcion])
    else:
        messagebox.showinfo("Error, debes seleccionar una fecha")
#Metodo para eliminar un evento
def eliminar_evento():
    seleccionado = tree.focus()
    if seleccionado:
        confirmacion = messagebox.askyesno("Eliminar Evento", "¿Estás seguro?")
        if confirmacion:
            tree.delete(seleccionado)
#Metodo para salir de la agenda
def salir():
    ventana.destroy()
boton_seleccionar_fecha = tk.Button(frame_botones, text="Seleccionar Fecha",command=seleccionar_fecha)
boton_seleccionar_fecha.pack(side="left")
boton_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
boton_agregar.pack(side="left")
boton_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(side="left")
boton_salir = tk.Button(frame_botones, text="Salir", command=salir)
boton_salir.pack(side="left")

ventana.mainloop()
