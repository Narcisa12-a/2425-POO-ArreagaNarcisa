# Implementacion de un programa en python con POO
class Clima:
    def __init__(self , ciudad):
        self.ciudad = ciudad    # Almacenamos la ciudad
        self.temperaturas = []  # Lista para almacenar las temperaturas

    def ingresar_temperatura(self,temperatura):
        self.temperaturas.append(temperatura)  # Añadir la temperatura a la lista

    def calcular_promedio(self):
        if not self.temperaturas :  # Verificamos si la lista de temperaturas esta vacia
            return 0  # Si está vacía, retornar 0
        return sum(self.temperaturas) / len(self.temperaturas) # Calculamos el promedio
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()  # Calcular el promedio de las temperaturas
        print(f"El promedio semanal de temperaturas en {self.ciudad} es: {promedio:.2f}°C")

# Función principal
def main():
    ciudad = input("Ingresar el nombre de la ciudad:") #Solicitar al usuario que ingrese el nombre de la ciudad
    clima = Clima(ciudad)  # Crear una instancia de la clase clima con el nombre ciudad
    print("Calculo del promedio semanal de temperaturas en {ciudad}")
    for i in range (7): # Iterar 7 veces, por cada dia de la semana
        # Solicitamos la temperatura al usuario
        temp = float(input(f"Ingrese la temperatura del dia {i + 1}: "))
        # Ingresar la temperatura en la instancia de clima
    clima.ingresar_temperatura(temp)  # Ingresar la temperatura en la instancia de Clima
    clima.mostrar_promedio() # Mostrar el promedio semanal de temperaturas

# Llamada a la función principal
if __name__ == "__main__":
    main()

# En este codigo se utilizo el metodo de encapsulamiento, este se ve en la clase ´clima'
# donde las temperaturas y ciudad estan encapsuladas dentro de la clase.
