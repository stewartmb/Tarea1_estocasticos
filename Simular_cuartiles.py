import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# Leer archivos
df_importado = pd.read_csv('archivo.csv')
data_2024 = pd.read_csv('2024.csv')
M = df_importado.to_numpy()

# Sumar filas (verificación de que cada fila suma 1)
suma_filas = np.sum(M, axis=1)
print("Suma de filas:")
print(suma_filas)

# Función de paso de la cadena de Markov
def step(row):
    r = random.random()
    for col in range(len(M[row])):
        r -= M[row, col]
        if r < 0:
            return col

# Parámetros
n_simulaciones = 50
steps = 312

# Diccionario de cambios por estado
dic = {
    0: -7.5,
    1: -3.5,
    2: -1,
    3: 0,
    4: 1,
    5: 3.5,
    6: 7.5
}

# Simulaciones
todas_las_posiciones = []

for _ in range(n_simulaciones):
    row = 1  # estado inicial
    ans = []
    for _ in range(steps):
        row = step(row)
        ans.append(row)

    cambios = [dic[v] for v in ans]
    posiciones = [100]
    for cambio in cambios:
        posiciones.append(posiciones[-1] * (100 + cambio) / 100)

    todas_las_posiciones.append(posiciones)

# Convertimos a array para estadísticas
todas_las_posiciones = np.array(todas_las_posiciones)

# Calcular Q1, media y Q3
q1 = np.percentile(todas_las_posiciones, 25, axis=0)
q3 = np.percentile(todas_las_posiciones, 75, axis=0)
media = np.mean(todas_las_posiciones, axis=0)

# Leer los datos reales
cambios = data_2024.iloc[:, 0].tolist()
posiciones_reales = [100]
for cambio in cambios:
    posiciones_reales.append(posiciones_reales[-1] * (100 + cambio) / 100)

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(q1, label='1er Cuartil (Q1)', color='blue', linestyle='--')
plt.plot(media, label='Media de Simulaciones', color='green')
plt.plot(q3, label='3er Cuartil (Q3)', color='blue', linestyle='--')
plt.plot(posiciones_reales, label='Datos Reales', color='red', linewidth=2)

plt.title('Simulación de 500 trayectorias vs datos reales')
plt.xlabel('Día')
plt.ylabel('Posición acumulada')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
