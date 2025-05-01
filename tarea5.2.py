import numpy as np
import matplotlib.pyplot as plt

# Definición de los puntos de interpolación
x_points = np.array([1.0, 2.5, 4.0, 5.5])
y_points = np.array([85, 78, 69, 60])

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

# (a) Calcular la temperatura esperada en profundidad = 3.0 cm
x_target = 3.0
temperature_at_3 = lagrange_interpolation(x_target, x_points, y_points)
print(f"Temperatura estimada a 3.0 cm: {temperature_at_3:.4f} °C")

# (b) Graficar la interpolación en el rango [1.0, 5.5]
x_values = np.linspace(1.0, 5.5, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

# Graficar los puntos y la interpolación
plt.figure(figsize=(7,5))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Datos originales")
plt.xlabel("Profundidad (cm)")
plt.ylabel("Temperatura (°C)")
plt.title("Interpolación de Lagrange - Estimación de Temperatura en un Motor")
plt.legend()
plt.grid(True)
plt.show()
