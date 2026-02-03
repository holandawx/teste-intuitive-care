import zipfile
import os

RAW_FOLDER = "data/raw"
EXTRACTED_FOLDER = "data/extracted"

os.makedirs(EXTRACTED_FOLDER, exist_ok=True)


def extrair_zips():
    arquivos = os.listdir(RAW_FOLDER)

    for nome in arquivos:
        if nome.lower().endswith(".zip"):
            caminho_zip = os.path.join(RAW_FOLDER, nome)

            print(f"Extraindo: {nome}")

            with zipfile.ZipFile(caminho_zip, "r") as zip_ref:
                zip_ref.extractall(EXTRACTED_FOLDER)

    print("\nExtração concluída! ✅")


if __name__ == "__main__":
    extrair_zips()
