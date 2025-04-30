import numpy as np

# Tu matriz de transición
matriz = np.array([
    [0.000, 0.250, 0.050, 0.200, 0.250, 0.150, 0.100],
    [0.018, 0.146, 0.181, 0.205, 0.269, 0.158, 0.023],
    [0.012, 0.098, 0.210, 0.306, 0.283, 0.077, 0.014],
    [0.005, 0.053, 0.223, 0.334, 0.285, 0.092, 0.008],
    [0.007, 0.067, 0.211, 0.342, 0.283, 0.085, 0.005],
    [0.021, 0.119, 0.233, 0.269, 0.233, 0.119, 0.005],
    [0.048, 0.238, 0.286, 0.095, 0.190, 0.143, 0.000]
])

# Transponer la matriz y restar la identidad
A = matriz.T - np.eye(7)

# Reemplazar la última fila por la condición de suma = 1
A[-1, :] = 1

# Vector del lado derecho
b = np.zeros(7)
b[-1] = 1

# Resolver el sistema lineal
pi = np.linalg.solve(A, b)

print("Distribución límite π:")
for i, prob in enumerate(pi):
    print(f"π_{i} = {prob:.4f}")


verificacion = pi @ matriz
print("\nVerificación (πP - π):")
print(verificacion - pi)
