import requests
import os

URL = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Operadoras_de_Plano_de_Saude_Ativas.csv"
DESTINO = "data/operadoras.csv"

os.makedirs("data", exist_ok=True)

try:
    print("Baixando cadastro das operadoras...")

    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    with open(DESTINO, "wb") as f:
        f.write(response.content)

    print("Download concluído com sucesso!")
    print("Arquivo salvo em:", DESTINO)

except Exception as e:
    print("Erro ao baixar arquivo:")
    print(e)
