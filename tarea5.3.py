import numpy as np
import matplotlib.pyplot as plt

# Definición de los puntos de interpolación
x_points = np.array([2.0, 4.0, 6.0, 8.0])
y_points = np.array([2500, 2300, 2150, 2050])

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# (a) Calcular el consumo esperado a altitud = 5.0 km
x_target = 5.0
consumption_at_5 = lagrange_interpolation(x_target, x_points, y_points)
print(f"Consumo estimado a 5.0 km: {consumption_at_5:.4f} kg/h")

# (b) Graficar la interpolación en el rango [2.0, 8.0]
x_values = np.linspace(2.0, 8.0, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

# Graficar los puntos y la interpolación
plt.figure(figsize=(7,5))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Datos originales")
plt.xlabel("Altitud (km)")
plt.ylabel("Consumo (kg/h)")
plt.title("Interpolación de Lagrange - Predicción del Consumo de Combustible en Aeronaves")
plt.legend()
plt.grid(True)

# Guardar la gráfica como archivo de imagen
plt.savefig("grafica_consumo_combustible.png", dpi=300)

# Mostrar la gráfica en pantalla
plt.show()
