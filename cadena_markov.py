import yfinance as yf
import numpy as np
import pandas as pd
from collections import defaultdict

# Descargar datos (forzar estructura consistente)
data = yf.download("AAPL", start="2016-01-01", end="2023-12-31", auto_adjust=False)

# Asegurar que close_prices sea Serie 1D
close_prices = data['Close']
if isinstance(close_prices, pd.DataFrame):
    close_prices = close_prices.squeeze()  # Convertir a Serie si es DataFrame

# Calcular retornos (asegurar 1D)
retornos = close_prices.pct_change().dropna()
retornos = retornos * 100  # Convertir a porcentaje

# Verificar dimensionalidad
if retornos.ndim != 1:
    retornos = retornos.squeeze()  # Forzar 1D si no lo está

# Definición de estados (tu esquema económico)D
bins = [-np.inf, -5, -2, -0.5, 0.5, 2, 5, np.inf]
labels = [
    "BF", 
    "BM", 
    "BL", 
    "Es", 
    "SL",
    "SM",
    "SF"
]

# Discretización (con verificación final)
try:
    estados = pd.cut(retornos, bins=bins, labels=labels)
except ValueError as e:
    print(f"Error al discretizar: {e}")
    print(f"Tipo de retornos: {type(retornos)}, Dimensión: {retornos.ndim}")
    raise

# Matriz de transición (resto del código igual)
trans_counts = defaultdict(lambda: defaultdict(int))
for i in range(len(estados) - 1):
    if estados.iloc[i] == 'BF' and estados.iloc[i + 1] == 'BF':
        print(f"Estado BF seguido de BF en índices {i} y {i + 1}")
    trans_counts[estados.iloc[i]][estados.iloc[i + 1]] += 1

matriz = pd.DataFrame(index=labels, columns=labels, dtype=float).fillna(0.0)
for estado_inicial in trans_counts:
    total = sum(trans_counts[estado_inicial].values())
    for estado_final in trans_counts[estado_inicial]:
        matriz.loc[estado_inicial, estado_final] = round(trans_counts[estado_inicial][estado_final] / total, 3)

print("Distribución de estados:\n", estados.value_counts().sort_index())
print("\nMatriz de Transición:\n", matriz)
