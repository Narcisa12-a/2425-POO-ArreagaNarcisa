#Programa para gestionar información básica de un registro de estudiantes
#Permite agregar, mostrar y buscar información sobre estudiantes en un sistema simple
class Estudiante:
    #Clase que representa a un estudiante
    def __init__(self,nombre: str,edad: int,matricula: str):
        #Inicializa un nuevo estudiante con nombre, edad y matricula
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    def __str__(self):
        #Devuelve una representacion en cadena del estudiante
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Matricula: {self.matricula}"

def es_nombre_valido(nombre:str) ->bool:
    #Verifica si el nombre solo contiene letras
    return all(caracter.isalpha() or caracter.isspace() for caracter in nombre)

def es_numero_valido(numero_str:str) ->bool:
    #Verifica si la cadena representa un numero entero positivo
    return numero_str.isdigit()

def agregar_estudiante(registro:list):
    #Agrega un nuevo estudiante al registro
    while True:
        nombre = input("Ingrese el nombre del estudiante:")
        if es_nombre_valido(nombre):
            break
        print("Error: El nombre solo debe contener letras.")
    while True:
        edad_str = input("Ingrese la edad del estudiante:")
        if es_numero_valido(edad_str):
            break
        print("Error: La edad debe ser un numero entero positivo.")
    while True:
        matricula = input("Ingrese la matricula del estudiante: ")
        if es_numero_valido(matricula):
            break
        print("Error: La matricula debe ser en números.")

    #Crear un nuevo objeto Estudiante y agregarlo al registro
    nuevo_estudiante = Estudiante(nombre, int(edad_str), matricula)
    registro.append(nuevo_estudiante)
    print("Estudiante agregado exitosamente")

def mostrar_registro(registro:list):
    #Muestra todos los estudiantes en el registro
    if not registro:
        print("El registro está vacío")
        return
    print("\nRegistro de Estudiantes:")
    for estudiante in registro:
        print(estudiante)

def buscar_estudiante(registro:list):
    #Busca un estudiante por su matrícula
    matricula_buscar = input("Ingrese la matricula del estudiante a buscar: ")
    if not es_numero_valido(matricula_buscar):
        print("Error: La matricula debe ser en numeros.")
        return
    for estudiante in registro:
        if estudiante.matricula == matricula_buscar:
            print(f"Estudiante encontrado: {estudiante}")
            return
    print("Estudiante no encontrado")

def main():
    #Lista para almacenar el registro de los estudiantes
    registro_estudiantes = []
    while True:
        print("\nOpciones:")
        print("1. Agregar estudiante")
        print("2. Mostrar registro")
        print("3. Buscar estudiante")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == '1':
            agregar_estudiante(registro_estudiantes)
        elif opcion == '2':
            mostrar_registro(registro_estudiantes)
        elif opcion == '3':
            buscar_estudiante(registro_estudiantes)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente otra vez.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
#En el programa se añadio la funcion 'es_nombre_valido' para verificar que el
#nombre ingresado contenga solo letras, tambien se añadio la funcion 'es_numero_valido'
#para verificar numeros enteros positivos, tambien se implemento bucles 'while' en 'agregar_estudiantes'
#para seguir solicitando el dato hasta que ingrese uno valido.
#en la funcion 'buscar_estudiantes' se valida que la amtricula usada sea en numeros.