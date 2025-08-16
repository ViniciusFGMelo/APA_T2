"""
Módulo contendo algoritmos de busca e análise de grafos.

Implementa DFS para cálculo de fecho transitivo e verificação de conectividade
conforme especificações do trabalho.
"""

class AlgoritmosGrafo:
    """
    Classe contendo algoritmos para análise de grafos.
    """
    
    @staticmethod
    def dfs_fecho_transitivo(grafo, vertice_inicial):
        """
        Computa o fecho transitivo usando busca em profundidade.
        
        Args:
            grafo (Grafo): Grafo para análise
            vertice_inicial: Vértice de partida
            
        Returns:
            set: Conjunto de vértices alcançáveis
            
        Complexidade: O(V + E)
        """
        visitados = set()
        
        def dfs_recursiva(vertice):
            """Função auxiliar recursiva para DFS."""
            visitados.add(vertice)
            
            for vizinho in grafo.obter_vizinhos(vertice):
                if vizinho not in visitados:
                    dfs_recursiva(vizinho)
        
        dfs_recursiva(vertice_inicial)
        return visitados
    
    @staticmethod
    def verificar_conectividade(grafo, tipo="nao_orientado"):
        """
        Verifica se um grafo é conexo.
        
        Args:
            grafo (Grafo): Grafo para análise
            tipo (str): "orientado" ou "nao_orientado"
            
        Returns:
            bool: True se conexo, False caso contrário
            
        Complexidade: 
            - Não orientado: O(V + E)
            - Orientado: O(V + E) após simetrização
        """
        if not grafo.vertices:
            return True
        
        # Para grafo orientado, precisa simetrizar
        if tipo == "orientado":
            grafo.simetrizar()
        
        # Escolhe um vértice inicial
        vertice_inicial = next(iter(grafo.vertices))
        
        # Computa fecho transitivo
        fecho = AlgoritmosGrafo.dfs_fecho_transitivo(grafo, vertice_inicial)
        
        # Verifica se todos os vértices foram alcançados
        return fecho == grafo.vertices