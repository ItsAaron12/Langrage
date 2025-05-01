import numpy as np
import matplotlib.pyplot as plt

# Definición de los puntos de interpolación
x_points = np.array([0.5, 1.0, 1.5, 2.0])
y_points = np.array([1.2, 2.3, 3.7, 5.2])

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

# (a) Calcular la deformación esperada en x = 1.25
x_target = 1.25
deformation_at_1_25 = lagrange_interpolation(x_target, x_points, y_points)
print(f"Deformación esperada en x = {x_target} m: {deformation_at_1_25:.4f} mm")

# (b) Graficar la interpolación en el rango [0.5, 2.0]
x_values = np.linspace(0.5, 2.0, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

# Graficar los puntos y la interpolación
plt.figure(figsize=(7,5))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Puntos originales")
plt.xlabel("Posición (m)")
plt.ylabel("Deformación (mm)")
plt.title("Interpolación de Lagrange - Predicción de Deformaciones en una Viga")
plt.legend()
plt.grid(True)
plt.show()
