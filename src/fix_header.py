import pandas as pd

ARQ = "data/processed/consolidado_validado.csv"
SAIDA = "data/processed/consolidado_validado_corrigido.csv"

df = pd.read_csv(ARQ, header=None)

df.columns = ["registro_ans", "valor_despesas"]

df.to_csv(SAIDA, index=False)

print("Arquivo corrigido criado:")
print(SAIDA)
