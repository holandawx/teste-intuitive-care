import pandas as pd
import os

INPUT_FILE = "data/processed/consolidado_despesas.csv"
OUTPUT_FILE = "data/processed/consolidado_validado.csv"

df = pd.read_csv(INPUT_FILE)

print("Linhas lidas:", len(df))

# só garante número
df["valor_despesas"] = pd.to_numeric(df["valor_despesas"], errors="coerce")

# remove apenas NaN
df = df.dropna(subset=["valor_despesas"])

print("Linhas após limpeza:", len(df))

df.to_csv(OUTPUT_FILE, index=False)

print("Arquivo validado criado com sucesso!")
