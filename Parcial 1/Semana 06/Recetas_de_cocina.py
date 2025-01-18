#Sistema de gestion de recetas de cocina, que permite gestionar recetas de cocina,
#incluyendo la capacidad de agregar ingredientes y pasos de preparación.

#Clase Base Receta
class Receta:
    def __init__(self, nombre):
        self.__nombre = nombre  #Nombre de la Receta(atributo encapsulado)
        self.__ingredientes = []  #Lista para almacenar ingredientes(atributo encapsulado)
        self.__pasos = []  #Lista para almacenar pasos de preparación(atributo encapsulado)
    def agregar_ingredientes(self,ingrediente): #Agrega un ingrediente a la receta.
        self.__ingredientes.append(ingrediente)
    def agregar_paso(self,paso): #Agrega un paso a la preparacion de la receta.
        self.__pasos.append(paso)
    def mostrar_receta(self): #Muestra los detalles de la receta.
        receta = f"Receta:{self.__nombre}\nIngredientes:\n"
        for ing in self.__ingredientes: receta += f"-{ing}\n"
        receta += "Pasos:\n"
        for paso in self.__pasos: receta += f"-{paso}\n"
        return receta
#Clase derivada RecetaPostre que hereda de Receta
class RecetaPostre(Receta):
    def mostrar_receta(self): #Metodo sobreescrito para mostrar los detalles de la receta postre, incluyendo una nota.
        return super().mostrar_receta() + "Nota:Esta es una receta de un postre."

#Ejemplo de uso
#Creacion de una instancia de la clase Receta
receta1 = Receta("Tostadas Francesas")
receta1.agregar_ingredientes("Pan")
receta1.agregar_ingredientes("huevo")
receta1.agregar_ingredientes("Leche")
receta1.agregar_ingredientes("Chocolate")
receta1.agregar_ingredientes("Mantequilla")
receta1.agregar_ingredientes("Miel")
receta1.agregar_ingredientes("Fresas")
receta1.agregar_paso("Batir un huevo junto con el chocolate")
receta1.agregar_paso("Remojar el pan con la mezcla")
receta1.agregar_paso("Calentar la sarten con mantequilla e introducir el pan")
receta1.agregar_paso("Sacar el pan cuando este dorado")
receta1.agregar_paso("Servir y decorar con miel y fresas")

#Creacion de una instancia de la clase RecetaPostre
receta_postre = RecetaPostre("Pudin de chocolate")
receta_postre.agregar_ingredientes("Chocolate")
receta_postre.agregar_ingredientes("Leche")
receta_postre.agregar_ingredientes("Maicena")
receta_postre.agregar_ingredientes("Canela")
receta_postre.agregar_paso("Mezclar la leche con la maicena y el chocolate")
receta_postre.agregar_paso("Agregar canela y poner a fuego lento")
receta_postre.agregar_paso("Mezclar hasta obtener una masa homogenea")
receta_postre.agregar_paso("Sacar del fuego y dejar que se enfrie")

#Mostrar las recetas
print(receta1.mostrar_receta())
print(receta_postre.mostrar_receta())

#La clase RecetaPostre deriva de la clase receta, demostrando asi el concepto de herencia.
#Los atributos __nombre, __ingredientes y __pasos estan emcapsulados en la clase Receta.
#El metodo mostrar_receta esta sobreescrito en la clase RecetaPostre, domostrando asi el polimorfismo.
#Los atributos y metodos estan definidos en las clases Recetas y RecetaPostre.
#Se crearon instancias de las clases y se utilizan sus metodos para demostrar la funcionalidad del programa.
