import yfinance as yf
import pandas as pd

# Télécharger les prix historiques d'Apple
df = yf.download('AAPL', start='2020-01-01', end='2024-01-01')

# Afficher les 5 premières lignes
print(df.head())