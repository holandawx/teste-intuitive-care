from fastapi import FastAPI
import sqlite3

app = FastAPI()

DB_PATH = "../dados.db"

def get_db():
    return sqlite3.connect(DB_PATH)


@app.get("/api/operadoras")
def listar_operadoras(page: int = 1, limit: int = 10):
    offset = (page - 1) * limit
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT cnpj, razao_social, uf, modalidade
        FROM despesas
        LIMIT ? OFFSET ?
    """, (limit, offset))

    rows = cursor.fetchall()
    conn.close()

    return {
        "page": page,
        "limit": limit,
        "data": [
            {
                "cnpj": r[0],
                "razao_social": r[1],
                "uf": r[2],
                "modalidade": r[3]
            } for r in rows
        ]
    }


@app.get("/api/operadoras/{cnpj}")
def detalhe_operadora(cnpj: str):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT *
        FROM despesas
        WHERE cnpj = ?
        LIMIT 1
    """, (cnpj,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"error": "Operadora não encontrada"}

    return {
        "cnpj": row[2],
        "razao_social": row[3],
        "nome_fantasia": row[4],
        "modalidade": row[5],
        "cidade": row[10],
        "uf": row[11]
    }


@app.get("/api/operadoras/{cnpj}/despesas")
def despesas_operadora(cnpj: str):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT data_registro, valor_despesas
        FROM despesas
        WHERE cnpj = ?
        ORDER BY data_registro
    """, (cnpj,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {"data": r[0], "valor": r[1]}
        for r in rows
    ]


@app.get("/api/estatisticas")
def estatisticas():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(valor_despesas) FROM despesas")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(valor_despesas) FROM despesas")
    media = cursor.fetchone()[0]

    cursor.execute("""
        SELECT razao_social, SUM(valor_despesas)
        FROM despesas
        GROUP BY razao_social
        ORDER BY SUM(valor_despesas) DESC
        LIMIT 5
    """)
    top5 = cursor.fetchall()

    cursor.execute("""
        SELECT uf, SUM(valor_despesas)
        FROM despesas
        GROUP BY uf
    """)
    por_uf = cursor.fetchall()

    conn.close()

    return {
        "total": total,
        "media": media,
        "top5": [
            {"razao_social": r[0], "total": r[1]} for r in top5
        ],
        "por_uf": [
            {"uf": r[0], "total": r[1]} for r in por_uf
        ]
    }
