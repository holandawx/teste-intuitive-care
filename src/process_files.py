import os
import pandas as pd

EXTRACTED_FOLDER = "data/extracted"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def ler_arquivo(caminho):
    try:
        return pd.read_csv(caminho, sep=";", encoding="latin1")
    except Exception as e:
        print("Erro ao ler:", caminho, e)
        return None


def encontrar_coluna(df, palavra):
    for col in df.columns:
        if palavra in col.upper():
            return col
    return None


def processar():
    todos = []

    for arquivo in os.listdir(EXTRACTED_FOLDER):
        if not arquivo.lower().endswith(".csv"):
            continue

        caminho = os.path.join(EXTRACTED_FOLDER, arquivo)

        print("Lendo:", arquivo)

        df = ler_arquivo(caminho)

        if df is None:
            continue

        df.columns = [c.strip().upper() for c in df.columns]

        col_reg = encontrar_coluna(df, "REG")
        col_valor = encontrar_coluna(df, "SALDO")

        if not col_reg or not col_valor:
            print("Pulando arquivo (colunas não encontradas)")
            continue

        df_final = df[[col_reg, col_valor]].copy()

        df_final.rename(columns={
            col_reg: "registro_ans",
            col_valor: "valor_despesas"
        }, inplace=True)

        todos.append(df_final)

    if not todos:
        print("Nenhum dado consolidado 😕")
        return

    consolidado = pd.concat(todos, ignore_index=True)

    saida = os.path.join(PROCESSED_FOLDER, "consolidado_despesas.csv")
    consolidado.to_csv(saida, index=False)

    print("\nCSV consolidado criado com sucesso:")
    print(saida)


if __name__ == "__main__":
    processar()
