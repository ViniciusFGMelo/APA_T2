# llm.py
"""
🎯 Segundo Trabalho de Implementação – Análise e Projeto de Algoritmos

Objetivo:
- Verificar se um grafo é conexo (orientado ou não orientado) utilizando DFS.
- Entrada em formato JSON.
"""

import json
import sys
import time
from collections import defaultdict


# ======================================================
# FUNÇÕES AUXILIARES
# ======================================================

def construir_lista_adjacencia(vertices, arestas):
    """
    📝 Constrói lista de adjacência para grafo não orientado.

    ⚡ Complexidade:
    - Tempo: O(|V| + |E|)
    - Espaço: O(|V| + |E|)
    """
    adj = defaultdict(list)
    for u, v in arestas:
        adj[u].append(v)
        adj[v].append(u)  # não orientado
    return adj


def construir_lista_sucessores(vertices, arcos):
    """
    📝 Constrói lista de sucessores para grafo orientado (já simetrizado).

    ⚡ Complexidade:
    - Tempo: O(|V| + |E|)
    - Espaço: O(|V| + |E|)
    """
    adj = defaultdict(list)
    for u, v in arcos:
        adj[u].append(v)
    return adj


def dfs(grafo, inicio, visitados):
    """
    🔍 Busca em profundidade (DFS).

    ⚡ Complexidade:
    - Tempo: O(|V| + |E|)
    - Espaço: O(|V|) (para a pilha de recursão e conjunto de visitados)
    """
    visitados.add(inicio)
    for viz in grafo[inicio]:
        if viz not in visitados:
            dfs(grafo, viz, visitados)


def eh_conexo_nao_orientado(vertices, arestas):
    """
    🌐 Verifica conectividade em grafo não orientado.

    ⚡ Complexidade:
    - Tempo: O(|V| + |E|)
    - Espaço: O(|V| + |E|)
    """
    adj = construir_lista_adjacencia(vertices, arestas)
    inicio = next(iter(vertices))  # pega um vértice qualquer
    visitados = set()
    dfs(adj, inicio, visitados)
    return visitados == vertices


def eh_conexo_orientado(vertices, arcos):
    """
    🌐 Verifica conectividade em grafo orientado (com simetrização).

    ⚡ Complexidade:
    - Tempo: O(|V| + |E|)
    - Espaço: O(|V| + |E|)
    """
    # 1. Simetrizar
    arcos_simetrizados = set(arcos)
    for u, v in arcos:
        arcos_simetrizados.add((v, u))

    # 2. Construir lista de sucessores
    adj = construir_lista_sucessores(vertices, arcos_simetrizados)

    # 3. DFS
    inicio = next(iter(vertices))
    visitados = set()
    dfs(adj, inicio, visitados)

    # 4. Comparar fecho
    return visitados == vertices


# ======================================================
# MAIN – LEITURA DO ARQUIVO JSON
# ======================================================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Uso: python3 llm.py <arquivo.json>")
        sys.exit(1)

    arquivo = sys.argv[1]

    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    nome = dados["nome"]
    tipo = dados["tipo"]
    vertices = set(dados["vertices"])
    ligacoes = [tuple(l) for l in dados["ligacoes"]]

    inicio_tempo = time.perf_counter()

    if tipo == "nao_orientado":
        conexo = eh_conexo_nao_orientado(vertices, ligacoes)
    elif tipo == "orientado":
        conexo = eh_conexo_orientado(vertices, ligacoes)
    else:
        print("❌ Tipo inválido! Use 'nao_orientado' ou 'orientado'.")
        sys.exit(1)

    fim_tempo = time.perf_counter()
    tempo_execucao = fim_tempo - inicio_tempo

    # === Saída com emojis ===
    print(f"📌 Grafo: {nome}")
    print("✅ Resultado: CONEXO" if conexo else "❌ Resultado: DESCONEXO")
    print(f"⏱️ Tempo de execução: {tempo_execucao:.6f} segundos")
