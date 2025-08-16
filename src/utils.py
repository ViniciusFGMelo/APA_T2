"""
Módulo com funções utilitárias para formatação, validação e exibição de resultados.
"""

class GrafoUtils:
    """Classe com métodos utilitários para manipulação de grafos."""
    
    @staticmethod
    def validar_entrada(vertices, arestas):
        """
        Valida os dados de entrada do grafo.
        
        Args:
            vertices (set/list): Conjunto de vértices
            arestas (list): Lista de arestas/arcos
            
        Returns:
            bool: True se válido, False caso contrário
            
        Complexidade: O(E)
        """
        if not vertices or not isinstance(vertices, (set, list)):
            return False
        
        vertices_set = set(vertices)
        
        for aresta in arestas:
            if len(aresta) != 2:
                return False
            origem, destino = aresta
            if origem not in vertices_set or destino not in vertices_set:
                return False
        
        return True
    
    @staticmethod
    def imprimir_resultado(tipo_grafo, vertices, arestas, eh_conexo, fecho_transitivo, vertice_inicial):
        """
        Imprime resultado formatado da análise de conectividade.
        
        Args:
            tipo_grafo (str): "Orientado" ou "Não Orientado"
            vertices (set): Conjunto de vértices
            arestas (list): Lista de arestas
            eh_conexo (bool): Resultado da conectividade
            fecho_transitivo (set): Fecho transitivo computado
            vertice_inicial: Vértice usado como ponto de partida
            
        Complexidade: O(1)
        """
        print(f"=== GRAFO {tipo_grafo.upper()} ===")
        print(f"Vértices (X): {vertices}")
        print(f"Arestas/Arcos: {arestas}")
        print(f"\nVértice escolhido para DFS: {vertice_inicial}")
        print(f"Fecho transitivo: {fecho_transitivo}")
        print(f"Fecho == X? {fecho_transitivo == vertices}")
        print(f"Resultado: O grafo é {'CONEXO' if eh_conexo else 'DESCONEXO'}")
    
    @staticmethod
    def criar_grafo_exemplo(tipo="desconexo"):
        """
        Cria grafos de exemplo para testes.
        
        Args:
            tipo (str): "desconexo" ou "conexo"
            
        Returns:
            tuple: (vertices, arestas)
            
        Complexidade: O(1)
        """
        if tipo == "desconexo":
            vertices = {'x1', 'x2', 'x3', 'x4', 'x5', 'x6'}
            arestas = [('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'), 
                      ('x4', 'x5'), ('x5', 'x6'), ('x6', 'x4')]
        else:  # conexo
            vertices = {'A', 'B', 'C', 'D'}
            arestas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
        
        return vertices, arestas

class AnalisadorComplexidade:
    """Classe para análise e relatório de complexidade."""
    
    @staticmethod
    def relatorio_complexidade():
        """
        Gera relatório detalhado da complexidade dos algoritmos.
        
        Complexidade: O(1)
        """
        print("\n📊 ANÁLISE DETALHADA DE COMPLEXIDADE")
        print("=" * 60)
        print("🔹 GRAFO NÃO ORIENTADO:")
        print("  • Construção da lista de adjacência: O(V + E)")
        print("  • DFS para fecho transitivo: O(V + E)")
        print("  • Comparação de conjuntos: O(V)")
        print("  • COMPLEXIDADE TOTAL: O(V + E)")
        
        print("\n🔹 GRAFO ORIENTADO:")
        print("  • Simetrização: O(E²) [versão atual] ou O(E) [com otimização]")
        print("  • Construção da lista de adjacência: O(V + E)")
        print("  • DFS para fecho transitivo: O(V + E)")
        print("  • Comparação de conjuntos: O(V)")
        print("  • COMPLEXIDADE TOTAL: O(V + E²) [atual] ou O(V + E) [otimizada]")
        
        print("\n🔹 ONDE:")
        print("  • V = |vertices| = número de vértices")
        print("  • E = |arestas| = número de arestas/arcos")
        
        print("\n🔹 JUSTIFICATIVAS:")
        print("  • DFS visita cada vértice exatamente uma vez: O(V)")
        print("  • DFS explora cada aresta exatamente uma vez: O(E)")
        print("  • Operações em conjuntos (add, in): O(1) amortizado")
        print("  • Comparação de conjuntos: O(min(|A|, |B|))")