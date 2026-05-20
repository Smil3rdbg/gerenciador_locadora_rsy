import random


def chama_id():
    id_ezin = random.randint(1000, 999999999)
    return id_ezin


# =========================
# TUPLA DE STATUS
# =========================

status_estoque = (
    "❌ Sem estoque",
    "✅ Em estoque"
)


# =========================
# LISTAS
# =========================

lista_filme = [
    {
        'id': 44444,
        'titulo': 'Vingadores: Ultimato',
        'genero': 'Ação',
        'estoque': [1, 2, 3, 4, 5],
        'estudio': 'Marvel Studios',
        'ano': 2019
    }
]

lista_livro = []

lista_hq = []
