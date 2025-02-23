import os
class Producto:
    def __init__(self, nombre, cantidad, precio):  #Inicializa un nuevo producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):  #Devuelve una representacion em cadena del producto para su almacenamiento en el archivo.
        return f"{self.nombre}, {self.cantidad}. {self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):  #Inicializa el inventario y define el archivo dende se almacenara.
        self.archivo = archivo
        self.productos = {} #Diccionario para almacenar productos
        self.cargar_inventario = () #Carga el inventario al iniciar
    def cargar_inventario(self):  #Carga los productos desde el archivo al iniciar el programa
        if os.path.exists(self.archivo):  #Verifica si el archivo existe
            try:
                with open(self.archivo,"r") as file:  #Lee cada linea del archivo y crea objetos producto.
                   for linea in file:
                       nombre, cantidad, precio = linea.strip().split(',')
                       self.productos [nombre] = Producto(nombre, int(cantidad), float(precio))
                print("Inventario cargado exitosamente.")
            except Exception as e:  #Maneja cualquier excepcion, que ocurra durante la lectura del archivo.
                print(f"Error al cargar el inventario:{e}")
        else:
            print("El archivo de inventario no existe. Se creara uno nuevo")
    def guardar_inventario(self): #Guarda los productos en el archivo
        try:
            with open(self.archivo, 'w') as file:  #Escribe cada producto en el archivo
                for producto in self.productos.values():
                    file.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except (FileNotFoundError, PermissionError) as e: #Maneja errores relacionados con la escritura en el archivo.
            print(f"Error al guardar el inventario: {e}")
    def agregar_producto(self, nombre, cantidad, precio):  #Agrega un nuevo producto al inventario y lo guarda en el archivo,
        if nombre in self.productos:  #Verifica si el producto ya existe
            print("El producto ya existe. Actualizando cantidad.")
            self.productos[nombre].cantidad += cantidad  #Actualiza la cantidad si existe
        else:  #Crea un nuevo ebjeto Producto y lo agrega al diccionario
            self.productos[nombre] = Producto(nombre, cantidad, precio)
        self.guardar_inventario() #Guarda los cambios en el archivo
    def eliminar_producto(self, nombre):  #Elimina un producto del inventario y actualiza el archivo.
        if nombre in self.productos:  #Verifica si el producto existe
            del self.productos[nombre]  #Elimina el producto del diccionario
            self.guardar_inventario()  #Guarda los cambios en el archivo
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print("El producto no se encuentra en el inventario.")
    def actualizar_producto(self, nombre, cantidad=None, precio=None): #Actualiza la informacion de un producto existente.
        if nombre in self.productos:  #Verifica si el producto existe
            if cantidad is not None:  #Actualiza la cantidad si se proporciona
                self.productos[nombre].cantidad = cantidad
                if precio is not None:  #Actualiza el precio si se proporciona
                    self.productos[nombre].precio = precio
                self.guardar_inventario()  #Guarda los cambios en el invemtario
                print(f"Producto '{nombre}' actualizado.")
            else:
                print("El producto no se encuentra en el inventario.")

def menu():
    inventario = Inventario()  #Crea una instancia de Inventario

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4.Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1': #Opcion para agregar un nuevo producto
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion =='2':  #Opcion para eliminar un producto existente
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '3':  #Opcion para actualizar un producto existente
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacio si no se quiere cambiar): ")
            precio = input("Nuevo precio (dejar vacio si no se quiere cambiar): ")
            #Convierte las entrada a tipos apropiados o deja como None si estan vacias
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == '4':
            print("Saliendo del programa...")
            break  #Sale del bucle y termina el programa
        else:
            print("Opcion no valida. Intente nuevamente.")
if __name__ == "__main__":
    menu()  #Llama a la funcion menu para iniciar el programa