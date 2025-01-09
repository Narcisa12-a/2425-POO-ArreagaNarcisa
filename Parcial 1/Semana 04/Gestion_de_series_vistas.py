# Crear una lista de series vistas
# Clase que representa un episodio de una serie
class Episodio:
    def __init__(self, titulo, duracion):
        self.titulo = titulo  # Ingresar el titulo de la serie
        self.duracion = duracion  # Ingresar la duración de la serie en minutos

    def mostrar_info(self):
        # Muestra la informacion del episodio
        return f'Episodio: {self.titulo}, duración: {self.duracion} minutos'

# Clase que representa una serie
class Serie:
    def __init__(self, nombre):
        self.nombre = nombre  # Ingresar el nombre de la serie
        self.episodios = []  # Lista de episodios
        self.vistos = []  # Lista de episodios vistos

    def agregar_episodio(self, episodio):
        # Agregar un episodio a la serie
        self.episodios.append(episodio)

    def marcar_visto(self, episodio):
        # Marcar un episodio como visto
        if episodio in self.episodios and episodio not in self.vistos:
            self.vistos.append(episodio)
            print(f'Has visto el episodio: {episodio.titulo}')
        else:
            print(f'El episodio {episodio.titulo} no está en la serie o ha sido marcado como visto')

    def mostrar_info(self):
        # Muestra la informacion de la serie y los episodios vistos
        print(f'Serie: {self.nombre}')
        print('Episodios:')
        for episodio in self.episodios:
            estado = "Visto" if episodio in self.vistos else "No visto"
            print(f'{episodio.mostrar_info()} ({estado})')


# Clase que representa un usuario que gestiona sus series vistas
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre  # Ingresar el nombre del usuario
        self.series = []  # Lista de series vistas por el usuario

    def agregar_serie(self, serie):
        # Agrega una nueva serie a la lista del usuario
        self.series.append(serie)

    def mostrar_series(self):
        # Muestra todas las series y su estado
        print(f'Series vistas por {self.nombre}:')
        for serie in self.series:
            serie.mostrar_info()
            print()  # Linea en blanco para mejor legibilidad

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un usuario
    usuario = Usuario("Lilibeth")
    # Crear lista de series
    serie1 = Serie("Squid Game T2")
    serie2 = Serie("Tomorrow")
    # Crear episodios para Squid Game T2
    episodio1_SGt2 = Episodio("Capítulo 1: Sustento y azar", 65)
    episodio2_SGt2 = Episodio("Fiesta de Halloween", 58)
    # Agregar episodios a Squid Game T2
    serie1.agregar_episodio(episodio1_SGt2)
    serie1.agregar_episodio(episodio2_SGt2)
    # Crear episodios para Tomorrow
    episodio1_Tomorrow = Episodio("Flores que caen 1", 60)
    episodio2_Tomorrow = Episodio("Flores que caen 2",60)
    # Agregar episodios a Tomorrow
    serie2.agregar_episodio(episodio1_Tomorrow)
    serie2.agregar_episodio(episodio2_Tomorrow)
    # Marcar episodios como vistos
    serie1.marcar_visto(episodio1_SGt2)
    serie2.marcar_visto(episodio1_Tomorrow)
    # Agregar series al usuario
    usuario.agregar_serie(serie1)
    usuario.agregar_serie(serie2)
    # Mostrar todas las series vistas por el usuario
    usuario.mostrar_series()