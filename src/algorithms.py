class AlgoritmosGrafo:
    @staticmethod
    def dfs_fecho_transitivo(grafo, vertice_inicial):
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
        if not grafo.vertices:
            return False, set(), None

        if tipo == "orientado":
            grafo.simetrizar()

        vertice_escolhido = next(iter(grafo.vertices))
        fecho_transitivo = AlgoritmosGrafo.dfs_fecho_transitivo(
            grafo, vertice_escolhido)
        eh_conexo = fecho_transitivo == grafo.vertices

        return eh_conexo, fecho_transitivo, vertice_escolhido
