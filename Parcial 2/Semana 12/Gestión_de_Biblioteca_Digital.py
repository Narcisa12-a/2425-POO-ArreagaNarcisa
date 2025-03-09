#Desarrolle un sistema para gestionar una biblioteca digital. El cual permitira administrar
#los libros disponibles, las categorias de libros, los usuarios registrados y el historial de prestados.
import json
# Clase que representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor) #El atributo titulo_autor combinael titulo y el autor en una tupla
        self.categoria = categoria #Categoria del libro
        self.isbn = isbn #Codigo unico para identificar el libro
    def to_dict(self): #Convierte un objeto Libro en un Diccionario
        return {
            "titulo": self.titulo_autor[0],
            "autor": self.titulo_autor[1],
            "categoria": self.categoria,
            "isbn": self.isbn
        }
    @staticmethod
    def from_dict(data): #Reconstruye un objeto libro a partir de un diccionario
        return Libro(data["titulo"], data["autor"], data["categoria"], data["isbn"])

# Clase que representa un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre #Nombre del usuario
        self.id_usuario = id_usuario #Identificador unico del usuario
        self.libros_prestados = [] #Lista de los libros prestados
    def to_dict(self): #Convierte un objeto usuario y los libros prestados en diccionarios
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [libro.to_dict() for libro in self.libros_prestados]
        }
    @staticmethod
    def from_dict(data): #Reconstruye un objeto usuario desde un diccionario
        usuario = Usuario(data["nombre"], data["id_usuario"])
        usuario.libros_prestados = [Libro.from_dict(libro) for libro in data["libros_prestados"]]
        return usuario

# Clase que gestiona la biblioteca digital
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {} #Diccionario de libros disponibles indexados por ISBN
        self.usuarios_registrados = set() #Conjunto de IDs de usuarios registrados
        self.usuarios = {} #Diccionario de objetos Usuario indexados por ID
    def agregar_libro(self, libro): #Añade un libro a la colección de libros disponibles
        self.libros_disponibles[libro.isbn] = libro
    def quitar_libro(self, isbn): #Elimina un libro de la colección de libros disponibles por su ISBN
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
    def registrar_usuario(self, usuario): #Registra un nuevo usuario si su ID no está en el conjunto de usuarios registrados
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado.")
        else:
            print(f"El ID {usuario.id_usuario} ya está registrado.")
    def prestar_libro(self, isbn, id_usuario): #Presta un libro a un usuario registrado
        if isbn in self.libros_disponibles and id_usuario in self.usuarios_registrados:
            libro = self.libros_disponibles[isbn]
            usuario = self.usuarios[id_usuario]
            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[isbn]
            print(f"Libro {libro.titulo_autor[0]} prestado a {usuario.nombre}.")
        else:
            print(f"No se puede prestar el libro con ISBN {isbn} al usuario con ID {id_usuario}.")
    def devolver_libro(self, isbn, id_usuario): #Permite al usuario devolver los libros prestados
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro {libro.titulo_autor[0]} devuelto por {usuario.nombre}.")
                    return
            print(f"No se encontró el libro con ISBN {isbn} entre los prestados.")
        else:
            print(f"No existe usuario con ID {id_usuario}.")
    def buscar_libros(self, criterio, valor): #Busca libros según criterios (titulo, autor o categoria)
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == 'titulo' and valor.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif criterio == 'autor' and valor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif criterio == 'categoria' and valor.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados
    def listar_libros_prestados(self, id_usuario): #Lista de todos los libros prestados por un usuario
        if id_usuario in self.usuarios_registrados:
            return self.usuarios[id_usuario].libros_prestados
        else:
            print(f"No existe usuario con ID {id_usuario}.")
            return []
    def exportar_datos(self, archivo): #Exporta los datos de la biblioteca y usuario a un archivo JSON
        datos = {
            "libros_disponibles": [libro.to_dict() for libro in self.libros_disponibles.values()],
            "usuarios": [usuario.to_dict() for usuario in self.usuarios.values()]
        }
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
        print(f"Datos exportados a {archivo}.")
    def importar_datos(self, archivo): #Importa los datos desde un archivo JSON
        with open(archivo, 'r') as f:
            datos = json.load(f)
        self.libros_disponibles = {libro["isbn"]: Libro.from_dict(libro) for libro in datos["libros_disponibles"]}
        self.usuarios = {usuario["id_usuario"]: Usuario.from_dict(usuario) for usuario in datos["usuarios"]}
        self.usuarios_registrados = set(self.usuarios.keys())
        print(f"Datos importados desde {archivo}.")

# Menú interactivo
def menu_biblioteca():
    biblioteca = Biblioteca()

    while True: #Muestra las opciones disponibles para el usuario
        print("\n=== Menú Biblioteca ===")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Buscar libros")
        print("7. Listar libros prestados")
        print("8. Exportar datos")
        print("9. Importar datos")
        print("10. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1": #Agrega un libro
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)
            print(f"Libro '{titulo}' agregado.")
        elif opcion == "2": #Quita un libro
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
            print(f"Libro con ISBN {isbn} eliminado.")
        elif opcion == "3": #Registra un usuario
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
        elif opcion == "4": #Prestar un libro
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        elif opcion == "5": #Devolver un libro
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        elif opcion == "6": #Buscar libros
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            valor = input("Valor de búsqueda: ")
            resultados = biblioteca.buscar_libros(criterio, valor)
            print("\nResultados de búsqueda:")
            for libro in resultados:
                print(f"- {libro.titulo_autor[0]} de {libro.titulo_autor[1]} (Categoría: {libro.categoria})")
        elif opcion == "7": #Lista de lobros prestados
            id_usuario = input("ID del usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            print("\nLibros prestados:")
            for libro in libros_prestados:
                print(f"- {libro.titulo_autor[0]} de {libro.titulo_autor[1]}")
        elif opcion == "8": #Exportar datos
            archivo = input("Nombre del archivo para exportar datos (ej. datos.json): ")
            biblioteca.exportar_datos(archivo)
        elif opcion == "9": #Importar datos
            archivo = input("Nombre del archivo para importar datos (ej. datos.json): ")
            biblioteca.importar_datos(archivo)
        elif opcion == "10": #salir de la biblioteca
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_biblioteca()
