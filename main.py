import json
import time
from src.graph import Grafo
from src.algorithms import AlgoritmosGrafo

# ============================================
# CONFIGURAÇÃO: ALTERE APENAS ESTA LISTA
# ============================================
ARQUIVOS_TESTE = [
    "grafo1.json",  # Não orientado desconexo
    "grafo2.json"   # Orientado (com simetrização)
]


def carregar_grafo_json(nome_arquivo):
    try:
        with open(f"testes/{nome_arquivo}", 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return {
                'vertices': set(dados["vertices"]),
                'ligacoes': dados["ligacoes"],
                'tipo': dados["tipo"],
                'nome': dados["nome"]
            }
    except Exception as e:
        print(f"Erro: {e}")
        return None


def executar_teste(dados):
    vertices = dados['vertices']
    ligacoes = dados['ligacoes']
    tipo = dados['tipo']

    print(f"{dados['nome']}")
    print(f" Tipo: {tipo}")

    grafo = Grafo(eh_orientado=(tipo == "orientado"))
    grafo.construir_de_listas(vertices, ligacoes)

    if tipo == "orientado":
        print(f"Arcos originais: {ligacoes}")

    inicio = time.perf_counter()
    eh_conexo, fecho_transitivo, vertice_escolhido = AlgoritmosGrafo.verificar_conectividade(
        grafo, tipo)
    fim = time.perf_counter()
    tempo_execucao = fim - inicio

    if tipo == "orientado":
        print(f"Grafo após simetrização: {dict(grafo.lista_adjacencia)}")

    print(f"\n=== RESULTADO ===")
    print(f"Vértices (X): {vertices}")
    print(f"{'Arcos' if tipo == 'orientado' else 'Arestas'}: {ligacoes}")
    print(f"Vértice escolhido para DFS: {vertice_escolhido}")
    print(f"Fecho transitivo: {fecho_transitivo}")
    print(f"Fecho == X? {eh_conexo}")
    print(f"Resultado: O grafo é {'CONEXO' if eh_conexo else 'DESCONEXO'}")
    print(f" Tempo de execução: {tempo_execucao:.6f} segundos")

    return eh_conexo, tempo_execucao


def main():
    print("TRABALHO DE ANÁLISE E PROJETO DE ALGORITMOS")
    print("Verificação de Conectividade em Grafos")
    print("=" * 60)

    resultados = []

    for i, arquivo in enumerate(ARQUIVOS_TESTE, 1):
        print(f"\nTESTE {i}")
        print(f"Arquivo: {arquivo}")
        print("-" * 40)

        dados = carregar_grafo_json(arquivo)
        if dados is None:
            resultados.append((False, 0))
            continue

        resultado, tempo_execucao = executar_teste(dados)
        resultados.append((resultado, tempo_execucao))
        print("=" * 60)

    print(f"\n RESUMO")
    print("=" * 60)
    for i, (arquivo, (resultado, tempo_execucao)) in enumerate(zip(ARQUIVOS_TESTE, resultados), 1):
        status = " CONEXO" if resultado else " DESCONEXO"
        print(
            f" Teste {i} ({arquivo}): {status} | Tempo: {tempo_execucao:.6f}s")


if __name__ == "__main__":
    main()
