"""
Arquivo principal para execução da análise de conectividade de grafos.

Implementação do trabalho de Análise e Projeto de Algoritmos.
Verifica conectividade de grafos orientados e não orientados usando DFS.
"""

from src.graph import Grafo
from src.algorithms import AlgoritmosGrafo
from src.utils import GrafoUtils, AnalisadorComplexidade

def executar_analise_nao_orientado(vertices, arestas):
    """
    Executa análise de conectividade para grafo não orientado.
    
    Segue a especificação:
    1. Construir lista de adjacência
    2. Computar fecho transitivo via DFS
    3. Verificar se fecho == conjunto X
    
    Complexidade: O(V + E)
    """
    # Validação de entrada
    if not GrafoUtils.validar_entrada(vertices, arestas):
        print("❌ Entrada inválida!")
        return False
    
    # Construir grafo não orientado
    grafo = Grafo(eh_orientado=False)
    grafo.construir_de_listas(vertices, arestas)
    
    # Escolher vértice inicial
    vertice_inicial = next(iter(vertices))
    
    # Computar fecho transitivo
    fecho_transitivo = AlgoritmosGrafo.dfs_fecho_transitivo(grafo, vertice_inicial)
    
    # Verificar conectividade
    eh_conexo = fecho_transitivo == vertices
    
    # Exibir resultado
    GrafoUtils.imprimir_resultado("Não Orientado", vertices, arestas, 
                                 eh_conexo, fecho_transitivo, vertice_inicial)
    
    return eh_conexo

def executar_analise_orientado(vertices, arcos):
    """
    Executa análise de conectividade para grafo orientado.
    
    Segue a especificação:
    1. Simetrizar o grafo
    2. Construir lista de sucessores
    3. Computar fecho transitivo via DFS
    4. Verificar se fecho == conjunto X
    
    Complexidade: O(V + E²) [versão atual] ou O(V + E) [otimizada]
    """
    # Validação de entrada
    if not GrafoUtils.validar_entrada(vertices, arcos):
        print("❌ Entrada inválida!")
        return False
    
    # Construir grafo orientado
    grafo = Grafo(eh_orientado=True)
    grafo.construir_de_listas(vertices, arcos)
    
    print(f"Arcos originais: {arcos}")
    
    # Simetrizar conforme especificação
    grafo.simetrizar()
    
    print(f"Grafo simetrizado: {grafo.lista_adjacencia}")
    
    # Escolher vértice inicial
    vertice_inicial = next(iter(vertices))
    
    # Computar fecho transitivo
    fecho_transitivo = AlgoritmosGrafo.dfs_fecho_transitivo(grafo, vertice_inicial)
    
    # Verificar conectividade
    eh_conexo = fecho_transitivo == vertices
    
    # Exibir resultado
    GrafoUtils.imprimir_resultado("Orientado", vertices, arcos, 
                                 eh_conexo, fecho_transitivo, vertice_inicial)
    
    return eh_conexo

def main():
    """
    Função principal - executa testes conforme exemplos do trabalho.
    """
    print("🔬 TRABALHO DE ANÁLISE E PROJETO DE ALGORITMOS")
    print("📋 Verificação de Conectividade em Grafos")
    print("=" * 60)
    
    # TESTE 1: Grafo não orientado (exemplo do enunciado)
    print("\n🧪 TESTE 1 - GRAFO NÃO ORIENTADO")
    print("-" * 40)
    
    vertices_nao_orientado, arestas_nao_orientado = GrafoUtils.criar_grafo_exemplo("desconexo")
    resultado1 = executar_analise_nao_orientado(vertices_nao_orientado, arestas_nao_orientado)
    
    # TESTE 2: Grafo orientado (exemplo do enunciado)
    print("\n" + "=" * 60)
    print("\n🧪 TESTE 2 - GRAFO ORIENTADO")
    print("-" * 40)
    
    vertices_orientado = {'x1', 'x2', 'x3', 'x4', 'x5', 'x6'}
    arcos_orientado = [('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'), 
                      ('x4', 'x5'), ('x5', 'x6'), ('x2', 'x4')]
    
    resultado2 = executar_analise_orientado(vertices_orientado, arcos_orientado)
    
    # TESTE 3: Grafo conexo para comparação
    print("\n" + "=" * 60)
    print("\n🧪 TESTE 3 - GRAFO CONEXO (COMPARAÇÃO)")
    print("-" * 40)
    
    vertices_conexo, arestas_conexo = GrafoUtils.criar_grafo_exemplo("conexo")
    resultado3 = executar_analise_nao_orientado(vertices_conexo, arestas_conexo)
    
    # RESUMO E ANÁLISE
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS RESULTADOS")
    print("=" * 60)
    print(f"🔹 Teste 1 (Não orientado): {'✅ CONEXO' if resultado1 else '❌ DESCONEXO'}")
    print(f"🔹 Teste 2 (Orientado): {'✅ CONEXO' if resultado2 else '❌ DESCONEXO'}")
    print(f"🔹 Teste 3 (Conexo): {'✅ CONEXO' if resultado3 else '❌ DESCONEXO'}")
    
    # Análise de complexidade
    AnalisadorComplexidade.relatorio_complexidade()

if __name__ == "__main__":
    main()