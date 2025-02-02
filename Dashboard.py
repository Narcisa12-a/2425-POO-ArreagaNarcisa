import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Semana 02/Clonación repositorio.py/Deber semana 2.py',
        '2': 'Semana 03/Programación orientada a objetos.py/Programacion tradicional_promedio del clima.py',
        '3': 'Semana 04/EjemplosMundoReal_POO.py/Gestion_de_series_vistas.py',
        '4': 'Semana 05/Registro_de_estudiantes.py',
        '5': 'Semana 06/Recetas_de_cocina.py',
        '6': 'Semana 07/GestordePersonajes.py',

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")
        # Solicita al usuario que ingrese una opción
        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        #Verifica si la eleccion es valida
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()