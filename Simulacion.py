import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

df_importado = pd.read_csv('archivo.csv')
data_2024 = pd.read_csv('2024.csv')
M = df_importado.to_numpy()

# suma de filas
suma_filas = np.sum(M, axis=1)
print("Suma de filas:")
print(suma_filas)

def step(row):
  r = random.random()
  for col in range(len(M[row])):
    r -= M[row,col]
    if r < 0:
      ans = col
      break
  return col


# Parámetros
n_simulaciones = 1  # número de simulaciones
steps = 365 * 1  # número de pasos en cada simulación

#BF,BM,BL,Es,SL,SM,SF
dic = {
    0: -7.5,
    1: -3.5,
    2: -1,
    3: 0,
    4: 1,
    5: 3.5,
    6: 7.5
}

todas_las_posiciones = []

# Realizar n simulaciones
for _ in range(n_simulaciones):
    row = 1  # inicializamos el valor de 'row' para cada simulación
    ans = []
    for j in range(steps):
        row = step(row)
        ans.append(row)

    # Convertir los valores de ans a cambios en el diccionario
    cambios = [dic[v] for v in ans]

    # Inicializar la lista de posiciones con el valor inicial
    posiciones = [100]

    # Calcular las posiciones acumuladas para la simulación actual
    for cambio in cambios:
        posiciones.append(posiciones[-1] * (100 + cambio) / 100)

    # Agregar las posiciones de esta simulación a la lista de todas las simulaciones
    todas_las_posiciones.append(posiciones)


cambios = data_2024.iloc[:, 0].tolist()

print(len(cambios))

# Graficar todas las simulaciones
plt.figure(figsize=(10, 6))
for i, posiciones in enumerate(todas_las_posiciones):
    plt.plot(range(312), posiciones[:312], label=f'Simulado', color='b', alpha=1)






posiciones = [100]

# Calcular las posiciones acumuladas para la simulación actual
for cambio in cambios:
    posiciones.append(posiciones[-1] * (100 + cambio) / 100)

# Agregar las posiciones de esta simulación a la lista de todas las simulaciones
print(posiciones)

plt.plot(range(len(posiciones)), posiciones, label=f'Real', color='r', alpha=1)


#plt.title('Comparación de prediccion y datos de 01/2024-03/2025')
plt.title('Comparación de prediccion y datos de 01/2024-03/2025')
plt.xlabel('Índice')
plt.legend()
plt.ylabel('Posición acumulada')
plt.grid(True)
plt.show()
