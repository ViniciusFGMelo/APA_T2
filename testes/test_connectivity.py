"""
Testes unitários para verificação da correção dos algoritmos.
"""

import unittest
import sys
import os

# Adiciona o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.graph import Grafo
from src.algorithms import AlgoritmosGrafo
from src.utils import GrafoUtils

class TestConectividade(unittest.TestCase):
    """Classe de testes para algoritmos de conectividade."""
    
    def setUp(self):
        """Configuração inicial dos testes."""
        self.grafo_conexo = Grafo(eh_orientado=False)
        self.grafo_desconexo = Grafo(eh_orientado=False)
        
        # Grafo conexo: A-B-C-D-A (ciclo)
        vertices_conexo = ['A', 'B', 'C', 'D']
        arestas_conexo = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
        self.grafo_conexo.construir_de_listas(vertices_conexo, arestas_conexo)
        
        # Grafo desconexo: duas componentes separadas
        vertices_desconexo = ['x1', 'x2', 'x3', 'x4']
        arestas_desconexo = [('x1', 'x2'), ('x3', 'x4')]
        self.grafo_desconexo.construir_de_listas(vertices_desconexo, arestas_desconexo)
    
    def test_dfs_fecho_transitivo_conexo(self):
        """Testa DFS em grafo conexo."""
        fecho = AlgoritmosGrafo.dfs_fecho_transitivo(self.grafo_conexo, 'A')
        self.assertEqual(fecho, {'A', 'B', 'C', 'D'})
    
    def test_dfs_fecho_transitivo_desconexo(self):
        """Testa DFS em grafo desconexo."""
        fecho = AlgoritmosGrafo.dfs_fecho_transitivo(self.grafo_desconexo, 'x1')
        self.assertEqual(fecho, {'x1', 'x2'})
    
    def test_verificar_conectividade_conexo(self):
        """Testa verificação de conectividade em grafo conexo."""
        resultado = AlgoritmosGrafo.verificar_conectividade(self.grafo_conexo, "nao_orientado")
        self.assertTrue(resultado)
    
    def test_verificar_conectividade_desconexo(self):
        """Testa verificação de conectividade em grafo desconexo."""
        resultado = AlgoritmosGrafo.verificar_conectividade(self.grafo_desconexo, "nao_orientado")
        self.assertFalse(resultado)
    
    def test_validacao_entrada(self):
        """Testa validação de entrada."""
        # Entrada válida
        self.assertTrue(GrafoUtils.validar_entrada(['A', 'B'], [('A', 'B')]))
        
        # Entrada inválida - vértice inexistente
        self.assertFalse(GrafoUtils.validar_entrada(['A'], [('A', 'B')]))

if __name__ == '__main__':
    unittest.main()