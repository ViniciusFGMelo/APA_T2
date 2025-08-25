class AlgoritmosGrafo:
    @staticmethod
    def dfs_fecho_transitivo(grafo, vertice_inicial):
        visitados = set()
        pilha = [vertice_inicial]

        while pilha:
            vertice = pilha.pop()
            if vertice not in visitados:
                visitados.add(vertice)
                for vizinho in grafo.obter_vizinhos(vertice):
                    if vizinho not in visitados:
                        pilha.append(vizinho)

        return visitados

    @staticmethod
    def verificar_conectividade(grafo, tipo):
        if not grafo.vertices:
            return False, set(), None

        if tipo == "orientado":
            grafo.simetrizar()

        vertice_escolhido = next(iter(grafo.vertices))
        fecho_transitivo = AlgoritmosGrafo.dfs_fecho_transitivo(
            grafo, vertice_escolhido
        )
        eh_conexo = fecho_transitivo == grafo.vertices

        return eh_conexo, fecho_transitivo, vertice_escolhido
