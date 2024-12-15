# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []  # Crearemos una lista vacia para almacenar las temperaturas
    for i in range(7): # Iterar 7 veces, por cada dia de la semana
        # Pedir al usuario que ingrese la temperatura y convertirla en float
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp) # Añadimos las temperaturas a la lista
    return temperaturas # Devolvemos la lista de temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    # Calculamos el promedio dividiendo la suma de las temperaturas por el numero de dias
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    # Pedimos al usuario que ingrese el nombre de la ciudad
    ciudad = input("Ingrese el nombre de la ciudad:")
    print("Cálculo del promedio semanal de temperaturas en {ciudad}")
    temperaturas = ingresar_temperaturas() # Llamamos a la funcion para ingresar las temperaturas
    promedio = calcular_promedio(temperaturas) # Calcular el promedio usando su funcion correspondiente
    # Mostrar el resultado del promedio semanal
    print(f"El promedio semanal de temperaturas en {ciudad} es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
