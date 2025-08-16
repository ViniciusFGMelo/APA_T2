"""
Módulo contendo a classe principal para representação e manipulação de grafos.

Este módulo implementa a estrutura de dados grafo usando lista de adjacência
e fornece métodos para construção de grafos orientados e não orientados.
"""

class Grafo:
    """
    Classe para representação de grafos usando lista de adjacência.
    
    Atributos:
        vertices (set): Conjunto de vértices do grafo
        lista_adjacencia (dict): Lista de adjacência representando o grafo
        eh_orientado (bool): Indica se o grafo é orientado ou não
    """
    
    def __init__(self, eh_orientado=False):
        """
        Inicializa um grafo vazio.
        
        Args:
            eh_orientado (bool): True para grafo orientado, False para não orientado
            
        Complexidade: O(1)
        """
        self.vertices = set()
        self.lista_adjacencia = {}
        self.eh_orientado = eh_orientado
    
    def adicionar_vertice(self, vertice):
        """
        Adiciona um vértice ao grafo.
        
        Args:
            vertice: Identificador do vértice
            
        Complexidade: O(1)
        """
        self.vertices.add(vertice)
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []
    
    def adicionar_aresta(self, origem, destino):
        """
        Adiciona uma aresta ao grafo.
        
        Args:
            origem: Vértice de origem
            destino: Vértice de destino
            
        Complexidade: O(1)
        """
        # Garante que os vértices existem
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        
        # Adiciona a aresta
        self.lista_adjacencia[origem].append(destino)
        
        # Se não é orientado, adiciona aresta reversa
        if not self.eh_orientado:
            self.lista_adjacencia[destino].append(origem)
    
    def construir_de_listas(self, vertices, arestas):
        """
        Constrói o grafo a partir de listas de vértices e arestas.
        
        Args:
            vertices (list/set): Lista de vértices
            arestas (list): Lista de tuplas (origem, destino)
            
        Complexidade: O(V + E)
        """
        # Adiciona todos os vértices
        for vertice in vertices:
            self.adicionar_vertice(vertice)
        
        # Adiciona todas as arestas
        for origem, destino in arestas:
            self.adicionar_aresta(origem, destino)
    
    def simetrizar(self):
        """
        Simetriza o grafo adicionando arcos reversos.
        Utilizado para grafos orientados conforme especificação.
        
        Complexidade: O(V + E)
        """
        arestas_para_adicionar = []
        
        for origem in self.lista_adjacencia:
            for destino in self.lista_adjacencia[origem]:
                # Verifica se arco reverso já existe
                if origem not in self.lista_adjacencia[destino]:
                    arestas_para_adicionar.append((destino, origem))
        
        # Adiciona arcos simétricos
        for origem, destino in arestas_para_adicionar:
            self.lista_adjacencia[origem].append(destino)
    
    def obter_vizinhos(self, vertice):
        """
        Retorna os vizinhos de um vértice.
        
        Args:
            vertice: Vértice para consulta
            
        Returns:
            list: Lista de vértices adjacentes
            
        Complexidade: O(1)
        """
        return self.lista_adjacencia.get(vertice, [])
    
    def __str__(self):
        """Representação string do grafo."""
        tipo = "Orientado" if self.eh_orientado else "Não Orientado"
        return f"Grafo {tipo}: {self.lista_adjacencia}"