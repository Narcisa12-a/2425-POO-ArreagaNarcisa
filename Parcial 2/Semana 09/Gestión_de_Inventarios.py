#Desarrollar un sistema de Gestión de Inventarios simple para una tienda que permita añadir,
#actualizar, eliminar y buscar productos utilizando una estructura de datos personalizada.
# CLASE PRODUCTO
class Producto:
    def __init__(self, ID, Nombre, Cantidad, Precio):  #Inicializa un nuevo Producto
        self.ID = ID
        self.Nombre = Nombre
        self.Cantidad = Cantidad
        self.Precio = Precio

    def get_ID(self):  #Utilizamos Getters para obtener valores de los atributos del producto
        return self.ID
    def get_Nombre(self):
        return self.Nombre
    def get_Cantidad(self):
        return self.Cantidad
    def get_Precio(self):
        return self.Precio

    def set_Nombre(self, Nombre):  #Utilizamos Setters para actualizar los valores de los
        # atributos del producto
        self.Nombre = Nombre
    def set_Cantidad(self, Cantidad):
        self.Cantidad = Cantidad
    def set_Precio(self, Precio):
        self.Precio = Precio

# CLASE INVENTARIO
class Inventario:
    def __init__(self):  #Inicializa un nuevo inventario con una lista vacía
        self.Productos = []

    def añadir_Producto(self, Producto):  #Añade un nuevo producto al inventario y verifica que el ID del producto sea único
        if any(p.get_ID() == Producto.get_ID() for p in self.Productos):
            print("Error: El ID del Producto ya existe.")
        else:
            self.Productos.append(Producto)
            print("Producto añadido exitosamente.")

    def eliminar_Producto(self, ID):  #Elimina un producto del inventario basado en su ID
        self.Productos = [p for p in self.Productos if p.get_ID() != ID]
        print("Producto eliminado exitosamente.")

    def actualizar_Producto(self, ID, Cantidad=None, Precio=None):  #Actualiza la cantidad o el precio de un producto basado
        #en su ID. Si el producto no está, muestra un mensaje de error
        for p in self.Productos:
            if p.get_ID() == ID:
                if Cantidad is not None:
                    p.set_Cantidad(Cantidad)
                if Precio is not None:
                    p.set_Precio(Precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def busca_Producto(self, Nombre):  #Busca productos en el inventario cuyo nombre contenga la cadena
        # de búsqueda ignorando mayúsculas o minúsculas
        resultados = [p for p in self.Productos if Nombre.lower() in p.get_Nombre().lower()]
        return resultados

    def mostrar_Productos(self):  #Muestra todos los productos del inventario con sus detalles
        for p in self.Productos:
            print(f"ID: {p.get_ID()}, Nombre: {p.get_Nombre()}, Cantidad: {p.get_Cantidad()}, Precio: {p.get_Precio()}")

#Ejemplo de Uso
inventario = Inventario()
#Añadir Productos
producto1 = Producto(1, "Galletas Oreo", 50, 0.25)
producto2 = Producto(2, "Gomitas de limón", 69, 0.20)
producto3 = Producto(3, "Sprite", 20, 0.50)
producto4 = Producto(4, "Mogu Mogu", 50, 1.00)
inventario.añadir_Producto(producto1)
inventario.añadir_Producto(producto2)
inventario.añadir_Producto(producto3)
inventario.añadir_Producto(producto4)
#Mostrar Productos
inventario.mostrar_Productos()
#Actualizar Producto
inventario.actualizar_Producto(1, Cantidad=30, Precio=0.25)
inventario.actualizar_Producto(4, Cantidad=10, Precio=1.00)
#Buscar Producto
resultados = inventario.busca_Producto("Mogu Mogu")
for p in resultados:
    print(f"Encontrado - ID: {p.get_ID()}, Nombre: {p.get_Nombre()}, Cantidad: {p.get_Cantidad()}, Precio: {p.get_Precio()}")
#Eliminar Producto
inventario.eliminar_Producto(2)
inventario.mostrar_Productos()