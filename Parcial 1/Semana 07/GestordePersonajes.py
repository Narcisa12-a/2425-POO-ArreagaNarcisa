#Elabora un programa que gestione los miembros de la Legión de Recinocimiento y
#la Policia Militar  en Shingeki no Kyojin utilizando el metodo Constructor y Destructor.
class UnidadMilitar:
    def __init__(self, nombre, rango):  # Constructor que inicializa el nombre y rango de la unidad militar
        self.nombre = nombre
        self.rango = rango
        print(f"Unidad Militar creada: {self.nombre}, Rango: {self.rango}")

    def __del__(self):  # Destructor que se llama al eliminar un objeto
        print(f"Unidad Militar eliminada: {self.nombre}")

class Policia_Militar(UnidadMilitar):
    def __init__(self, nombre, rango):  #Constructor que inicializa el policia militar
        super().__init__(nombre, rango)  #Llama al constructor UnidadMilitar

class Legion_De_Reconocimiento(UnidadMilitar):
    def __init__(self, nombre, rango):  #Constructor que inicializa la legión de reconocimiento
        super().__init__(nombre, rango)  #Llama al constructor de UnidadMilitar

# Ejemplo de uso
def main():  # Crear miembros de las diferentes clases
    miembros_policia_militar = [
        Policia_Militar("Nile Dok", "Comandante"),
        Policia_Militar("Annie Leonhart", "Soldado raso"),
        Policia_Militar("Marlowe Freudenberg", "Soldado")
    ]

    miembros_legion_reconocimiento = [
        Legion_De_Reconocimiento("Levi Ackerman", "Capitán"),
        Legion_De_Reconocimiento("Hange Zoe", "Sargento"),
        Legion_De_Reconocimiento("Armin Arlert", "Comandante")
    ]

    # Mostrar miembros
    print("\nMiembros de la Policía Militar:")
    for miembro in miembros_policia_militar:
        print(f"{miembro.nombre} es un Policía Militar con rango {miembro.rango}")


    print("\nMiembros de la Legión de Reconocimiento:")
    for miembro in miembros_legion_reconocimiento:
        print(f"{miembro.nombre} es un Explorador con rango {miembro.rango}")
    print() #Linea en blanco para mejor legibilidad


    # Eliminación Forzada para mostrar los Destructores
    del miembros_policia_militar[0]
    del miembros_legion_reconocimiento[0]

# Ejecutar la función principal
if __name__ == "__main__":
    main()

#la clase base "UnidadMilitar" contiene el constructor que inicialoza los atributos comunes, tambien
#incluye el destructor que se invoca al eliminar cualquier instancia.
#Las clases "Policia_Militar" y "Legion_de_Recocnocimineto" son la herencia de la clase "UnidadMilitar"
#Se usa 'super() en las clases derivadas para asegurarse de que el costructor de base se ejecute correctamente
#Tambien se imprime una linea en blanco en la linea 43 para mejorar la visualizacion