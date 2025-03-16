#Desarrollar una aplicación de interfaz gráfica de usuario (GUI) que permita a los usuarios
#interactuar con datos de manera visual, utilizando los conceptos aprendidos sobre GUI.
import tkinter as tk
from tkinter import ttk #Importar las librerias necesarias
class AplicacionGUI:
    def __init__(self, root): #Inicializa la ventana principal
        self.root = root
        self.root.title("Aplicación GUI Básica") #Establecer título a la ventana
        self.root.geometry("400x300") #Establecer el tamaño de la ventana (ancho x alto)

        #Etiqueta para mostrar un mensaje al usuario
        self.etiqueta =  tk.Label(root, text="Ingrese su texto:")
        self.etiqueta.pack()  #Agregar etiqueta a la ventana

        #Campo de texto donde el usuario puede ingresar información
        self.campo_texto = tk.Entry(root, width=40)
        self.campo_texto.pack()  #Agregar campo de texto a la ventana

        #Boton "agregar" que llamara a la funcion agregar_texto cuando se haga clic
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_texto)
        self.boton_agregar.pack()  #Agregar boton a la ventana

        #Lista para mostrar los textos agregados por el usuario
        self.lista = tk.Listbox(root, width=40)
        self.lista.pack()  #Agregar lista a la ventana

        #Boton "limpiar" que llamara a la funcion limpiar_lista cuando se haga clic
        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_lista)
        self.boton_limpiar.pack()  #Agregar boton a la ventana
    #Funcion que se ejecuta cuando se hace clic en el boton "Agregar"
    def agregar_texto(self):
        texto = self.campo_texto.get()  #Obtener el texto ingresado por el usuario en el campo de texto
        if texto:   #Verificar si el campo no esta vacio
            self.lista.insert(tk.END,texto)  #Agregar el texto a la lista
            self.campo_texto.delete(0,tk.END)  #Limpiar el campo de texto para el proximo ingreso

    #Funcion que se ejecuta cuando se hace clic en el boton "Limpiar"
    def limpiar_lista(self):  #Eliminar todos los elementos de la lista
        self.lista.delete(0,tk.END)
#Inicia la aplicacion
if __name__ == "__main__":
    root = tk.Tk()  #Crea la ventana principal
    app = AplicacionGUI(root)  #Inicia el bucle principal de la aplicacion
    root.mainloop()
