class Grafo:
    def __init__(self, eh_orientado=False):
        self.vertices = set()
        self.lista_adjacencia = {}
        self.eh_orientado = eh_orientado

    def adicionar_vertice(self, vertice):
        self.vertices.add(vertice)
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.lista_adjacencia[origem].append(destino)
        if not self.eh_orientado:
            self.lista_adjacencia[destino].append(origem)

    def construir_de_listas(self, vertices, arestas):
        for vertice in vertices:
            self.adicionar_vertice(vertice)
        for origem, destino in arestas:
            self.adicionar_aresta(origem, destino)

    def simetrizar(self):
        arestas_para_adicionar = []
        for origem in self.lista_adjacencia:
            for destino in self.lista_adjacencia[origem]:
                if origem not in self.lista_adjacencia[destino]:
                    arestas_para_adicionar.append((destino, origem))
        for origem, destino in arestas_para_adicionar:
            self.lista_adjacencia[origem].append(destino)

    def obter_vizinhos(self, vertice):
        return self.lista_adjacencia.get(vertice, [])

    def __str__(self):
        tipo = "Orientado" if self.eh_orientado else "Não Orientado"
        return f"Grafo {tipo}: {self.lista_adjacencia}"
