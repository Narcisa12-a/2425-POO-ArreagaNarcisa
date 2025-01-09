# Ejemplo de una tienda en linea utilizando POO
# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto  # Id del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto

    def mostrar_info(self):  # Muestra la información del producto
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Precio: ${self.precio}'
# Clase que representa el carrito de compras
class carrito:
    def __init__(self):
        self.productos = [] # Lista para almacenar productos en el carrito

    def agregar_producto(self, producto):  # Agrega un producto al carrito
        self.productos.append(producto)

    def mostrar_carrito(self):  # Muestra los productos en el carrito y total
        total = 0
        print("Productos en el carrito:")
        for producto in self.productos:
            print(producto.mostrar_info())
            total += producto.precio
        print(f'Total a pagar: ${total}')

# Ejemplo de uso
if __name__== "__main__":
  # Crear algunos productos
    producto1 = Producto(1,"album BTS", 70)
    producto2 = Producto(2,"Figura de colección anime", 35)
    producto3 = Producto(3,"zapatos",10)
    producto4 = Producto(3,"lienzo", 2.00)
    producto5 = Producto(5,"arcilla",10)

# Crear un carrito y agregar productos
carrito = carrito()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)
carrito.agregar_producto(producto4)
carrito.agregar_producto(producto5)

# Mostrar el contenido del carrito
carrito.mostrar_carrito()