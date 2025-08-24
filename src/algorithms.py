"""
Implementação seguindo EXATAMENTE o enunciado do professor.
"""

class AlgoritmosGrafo:
    """Algoritmos para verificação de conectividade conforme especificação."""
    
    @staticmethod
    def dfs_fecho_transitivo(grafo, vertice_inicial):
        """
        Computa o fecho transitivo usando DFS.
        Segue exatamente o passo 2 (não orientado) e passo 3 (orientado).
        """
        visitados = set()
        
        def dfs_recursiva(vertice):
            visitados.add(vertice)
            for vizinho in grafo.obter_vizinhos(vertice):
                if vizinho not in visitados:
                    dfs_recursiva(vizinho)
        
        dfs_recursiva(vertice_inicial)
        return visitados
    
    @staticmethod
    def verificar_conectividade(grafo, tipo):
        """
        Verifica conectividade seguindo EXATAMENTE o enunciado:
        
        CASO NÃO ORIENTADO:
        1. Construir lista de adjacência ✓ (já feito)
        2. Computar fecho transitivo de um vértice
        3. Se fecho == X → conexo, senão desconexo
        
        CASO ORIENTADO:
        1. Simetrizar o grafo
        2. Construir lista de sucessores ✓ (já feito)
        3. Computar fecho transitivo de um vértice  
        4. Se fecho == X → conexo, senão desconexo
        """
        if not grafo.vertices:
            return False, set(), None
        
        # PASSO ESPECÍFICO PARA ORIENTADO: Simetrizar
        if tipo == "orientado":
            grafo.simetrizar()
        
        # Escolhe um vértice qualquer
        vertice_escolhido = next(iter(grafo.vertices))
        
        # Computa fecho transitivo
        fecho_transitivo = AlgoritmosGrafo.dfs_fecho_transitivo(grafo, vertice_escolhido)
        
        # Verifica se fecho == X
        eh_conexo = fecho_transitivo == grafo.vertices
        
        return eh_conexo, fecho_transitivo, vertice_escolhido