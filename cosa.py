import yfinance as yf
import numpy as np
import pandas as pd
from collections import defaultdict

# Descargar datos (forzar estructura consistente)
data = yf.download("AAPL", start="2024-01-01", end="2025-04-01", auto_adjust=False)

# Asegurar que close_prices sea Serie 1D
close_prices = data['Close']
if isinstance(close_prices, pd.DataFrame):
    close_prices = close_prices.squeeze()  # Convertir a Serie si es DataFrame

# Calcular retornos (asegurar 1D)
retornos = close_prices.pct_change().dropna()
retornos = retornos * 100  # Convertir a porcentaje

# Verificar dimensionalidad
if retornos.ndim != 1:
    retornos = retornos.squeeze()

print(retornos)

retornos.to_csv('2024.csv', index=False)