#Desarrolle un sistema de gestión de invenyatario para una tienda que incorpore las
#colecciones en POO para un manejo eficiente de los items del inventario y almacene la información
#del inventario en archivos.
# Importa las bibliotecas
import json
import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):  #Inicializa los atributos del producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self): #Metodo para obtener una representación en cadena del producto
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
    def get_id(self): #Utilizamos getters para obrener los atributos del producto
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio

    def set_id(self, id): #Urilizamos setters para modificar los atributos del producto
        self.id = id
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_precio(self, precio):
        self.precio = precio

class Inventario:
    def __init__(self): #Utilizamos diccionario para almacenar los productos donde la clave es el ID del producto
        self.productos = {}
    def agregar_producto(self, producto): #Metodo para agregar un nuevo producto
        self.productos[producto.id] = {"nombre": producto.nombre, "cantidad": producto.cantidad,
                                       "precio": producto.precio}
    def eliminar_producto(self, id): #Metodo para eliminar un producto por su ID
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"No se encontró producto con ID {id}.")
    def actualizar_cantidad(self, id, cantidad): #Metodo para actualizar la cantidad del producto
        if id in self.productos:
            self.productos[id]["cantidad"] = cantidad
            print(f"Cantidad del producto {id} actualizada.")
        else:
            print(f"No se encontró producto con ID {id}.")
    def actualizar_precio(self, id, precio): #Metodo para actualizar el precio
        if id in self.productos:
            self.productos[id]["precio"] = precio
            print(f"Precio del producto {id} actualizado.")
        else:
            print(f"No se encontró producto con ID {id}.")
    def buscar_producto(self, nombre): #Metodo para buscar productos por su nombre
        resultado = [producto for producto in self.productos.values() if producto["nombre"].lower() == nombre.lower()]
        if resultado:
            for producto in resultado:
                print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
        else:
            print(f"No se encontró producto con nombre '{nombre}'.")
    def mostrar_productos(self): #Metodo para mostrar todos los productos en el inventario
        if self.productos:
            for id, producto in self.productos.items():
                print(
                    f"ID: {id}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
        else:
            print("Inventario vacío.")
    def guardar_inventario(self, archivo): #Metodo para guardar el inventario en un archivo JSON
        with open(archivo, 'w') as f:
            json.dump(self.productos, f)
            print(f"Inventario guardado en {archivo}.")
    def cargar_inventario(self, archivo): #Metodo para cargar el inventario desde un archivo JSON
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                self.productos = json.load(f)
            print(f"Inventario cargado desde {archivo}.")
        else:
            print(f"No se encontró archivo {archivo}.")
    def mostrar_archivo_json(self, archivo): #Metodo para mostrar el archivo json
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                contenido = json.load(f)
                print(json.dumps(contenido, indent=4))
        else:
            print(f"No se encontró archivo {archivo}.")

def main():
    inventario = Inventario()  #Crea una instancia del inventario
    while True:  #Muestra el menú de opciones al usuario
        print("\n___Menú de Inventario___")
        print("1. Agregar Producto.")
        print("2. Eliminar Producto.")
        print("3. Actualizar Cantidad.")
        print("4. Actualizar Precio.")
        print("5. Buscar Producto.")
        print("6. Mostrar todos los Productos.")
        print("7. Guardar Inventario.")
        print("8. Cargar Inventario.")
        print("9. Mostrar archivo JSON.")
        print("10. Salir.")
        opcion = input("Ingrese su opción: ")  #Pide al usuario que ingrese su opcion
        if opcion == "1":  #Agrega un nuevo producto al inventario
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":  #Elimina un producto del inventario por su ID
            id = input("Ingrese ID del producto que desea eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":  #Actualiza la cantidad de un producto
            id = input("Ingrese ID del producto para actualizar la cantidad: ")
            cantidad = int(input("Ingrese nueva cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)
        elif opcion == "4": #Actualiza el precio de un producto
            id = input("Ingrese ID del producto para actualizar precio: ")
            precio = float(input("Ingrese nuevo precio: "))
            inventario.actualizar_precio(id, precio)
        elif opcion == "5":  #Busca productos por su nombre
            nombre = input("Ingrese nombre del producto que desea buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "6":  #Muestra todos los productos en el inventario
            inventario.mostrar_productos()
        elif opcion == "7":  #Guardar el inventario en un archivo
            archivo = input("Ingrese nombre del archivo para guardar (por defecto: inventario.json): ")
            if not archivo:
                archivo = "inventario.json"
            inventario.guardar_inventario(archivo)
        elif opcion == "8":  #Cargar el inventario desde un archivo
            archivo = input("Ingrese nombre del archivo para cargar (por defecto: inventario.json): ")
            if not archivo:
                archivo = "inventario.json"
            inventario.cargar_inventario(archivo)
        elif opcion == "9":#Muestra el archivo json
            archivo = input("Ingrese nombre del archivo para mostrar (por defecto: inventario.json): ")
            if not archivo:
                archivo = "inventario.json"
            inventario.mostrar_archivo_json(archivo)
        elif opcion == "10":  #Salir del programa
            break
        else:
            print("Opción inválida. Por favor, elija una opción del menú.")

if __name__ == "__main__":
    main()

