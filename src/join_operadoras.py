import pandas as pd

BASE = "data/processed/consolidado_validado_corrigido.csv"
OPERADORAS = "data/operadoras.csv"
SAIDA = "data/processed/consolidado_enriquecido.csv"

base = pd.read_csv(BASE)
oper = pd.read_csv(OPERADORAS, sep=";", encoding="latin1", header=None)

# define nomes das colunas das operadoras (só as importantes)
oper.columns = [
    "registro_ans",
    "cnpj",
    "razao_social",
    "nome_fantasia",
    "modalidade",
    "logradouro",
    "numero",
    "complemento",
    "bairro",
    "cidade",
    "uf",
    "cep",
    "ddd",
    "telefone",
    "fax",
    "email",
    "representante",
    "cargo",
    "status",
    "data_registro"
]

final = base.merge(oper, on="registro_ans", how="left")

final.to_csv(SAIDA, index=False)

print("Arquivo enriquecido criado com sucesso:")
print(SAIDA)

