"""
Implementação simples seguindo EXATAMENTE o enunciado do professor.
"""

import json
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
    """Carrega grafo de arquivo JSON."""
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
    """Executa teste seguindo exatamente o enunciado do professor."""
    vertices = dados['vertices']
    ligacoes = dados['ligacoes']
    tipo = dados['tipo']
    
    print(f"{dados['nome']}")
    print(f"🔹 Tipo: {tipo}")
    
    # PASSO 1: Construir lista de adjacência
    eh_orientado = (tipo == "orientado")
    grafo = Grafo(eh_orientado=eh_orientado)
    grafo.construir_de_listas(vertices, ligacoes)
    
    if tipo == "orientado":
        print(f"Arcos originais: {ligacoes}")
    
    # PASSOS 2-4: Executar algoritmo conforme enunciado
    eh_conexo, fecho_transitivo, vertice_escolhido = AlgoritmosGrafo.verificar_conectividade(grafo, tipo)
    
    if tipo == "orientado":
        print(f"Grafo após simetrização: {dict(grafo.lista_adjacencia)}")
    
    # Resultado conforme enunciado
    print(f"\n=== RESULTADO ===")
    print(f"Vértices (X): {vertices}")
    print(f"{'Arcos' if tipo == 'orientado' else 'Arestas'}: {ligacoes}")
    print(f"Vértice escolhido para DFS: {vertice_escolhido}")
    print(f"Fecho transitivo: {fecho_transitivo}")
    print(f"Fecho == X? {eh_conexo}")
    print(f"Resultado: O grafo é {'CONEXO' if eh_conexo else 'DESCONEXO'}")
    
    return eh_conexo

def main():
    """Função principal."""
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
            resultados.append(False)
            continue
        
        resultado = executar_teste(dados)
        resultados.append(resultado)
        print("=" * 60)
    
    # Resumo
    print(f"\n RESUMO")
    print("=" * 60)
    for i, (arquivo, resultado) in enumerate(zip(ARQUIVOS_TESTE, resultados), 1):
        status = " CONEXO" if resultado else " DESCONEXO"
        print(f"🔹 Teste {i} ({arquivo}): {status}")

if __name__ == "__main__":
    main()