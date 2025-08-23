# 🔬 Análise e Projeto de Algoritmos - Trabalho 2

## Verificação de Conectividade em Grafos

Implementação de algoritmos para verificação de conectividade em grafos orientados e não orientados usando busca em profundidade (DFS).

---

## Objetivo

Desenvolver um algoritmo que verifique se um grafo é **conexo**:

### Caso Não Orientado:
1. Construir lista de adjacência
2. Computar fecho transitivo usando DFS
3. Verificar se fecho transitivo == conjunto de vértices

### Caso Orientado:
1. **Simetrizar** o grafo (adicionar arcos reversos)
2. Construir lista de sucessores
3. Computar fecho transitivo usando DFS  
4. Verificar se fecho transitivo == conjunto de vértices

---

## Estrutura do Projeto

```
projeto/
├── main.py                    # Arquivo principal
├── src/
│   ├── graph.py                 # Classe Grafo (lista de adjacência)
│   └── algorithms.py            # Algoritmos DFS e conectividade
├── testes/
│   ├── grafo1.json             # Exemplo não orientado desconexo
│   └── grafo2.json             # Exemplo orientado (com simetrização)
└── README.md                   # Este arquivo
```
## Slides
https://gamma.app/docs/Analise-e-Projeto-de-Algoritmos-Trabalho-2-8w8w9jnp6dasq06
---

## Como Executar

### 1. Executar o programa:
```bash
python3 main.py
```

### 2. Adicionar novos testes:
1. Crie um arquivo JSON na pasta `testes/`
2. Adicione o nome do arquivo na lista `ARQUIVOS_TESTE` em `mainat.py`

---

## Formato dos Arquivos JSON

```json
{
  "nome": "Descrição do teste",
  "tipo": "orientado",
  "vertices": ["x1", "x2", "x3", "x4", "x5", "x6"],
  "ligacoes": [
    ["x1", "x2"], 
    ["x2", "x3"], 
    ["x3", "x1"], 
    ["x4", "x5"], 
    ["x5", "x6"], 
    ["x2", "x4"]
  ]
}
```

**Campos:**
- `nome`: Descrição do teste
- `tipo`: `"orientado"` ou `"nao_orientado"`
- `vertices`: Lista de vértices
- `ligacoes`: Lista de arestas/arcos `[origem, destino]`

---

## Exemplos de Teste

### Teste 1: Grafo Não Orientado Desconexo
```
Vértices: {x1, x2, x3, x4, x5, x6}
Arestas: [x1,x2], [x2,x3], [x3,x1], [x4,x5], [x5,x6], [x6,x4]

Visualização:
   x1 ── x2        x4 ── x5
   │     │         │     │  
   └─ x3 ┘         └─ x6 ┘

Resultado: DESCONEXO (duas componentes separadas)
```

### Teste 2: Grafo Orientado (com simetrização)
```
Vértices: {x1, x2, x3, x4, x5, x6}
Arcos: (x1→x2), (x2→x3), (x3→x1), (x4→x5), (x5→x6), (x2→x4)

Após simetrização: todas as setas viram bidirecionais
Resultado: CONEXO (conectividade fraca)
```

---

## Análise de Complexidade

| Operação | Complexidade | Justificativa |
|----------|-------------|---------------|
| **Construção do grafo** | O(V + E) | Adiciona V vértices + E arestas |
| **Simetrização** | O(V + E) | Percorre todas as arestas |
| **DFS (fecho transitivo)** | O(V + E) | Visita cada vértice/aresta uma vez |
| **Comparação conjuntos** | O(V) | Compara sets de vértices |
| **TOTAL** | **O(V + E)** | Dominante para ambos os casos |

Onde:
- **V** = número de vértices
- **E** = número de arestas/arcos

---

## Conceitos Importantes

### Simetrização
Transformar um grafo orientado em não orientado, adicionando o arco reverso para cada arco existente.
**Exemplo:** A → B vira A ⟷ B

### Fecho Transitivo
Conjunto de todos os vértices alcançáveis a partir de um vértice inicial usando DFS.

### Conectividade
**Grafo conexo**: Existe caminho entre qualquer par de vértices. Para orientados testamos conectividade fraca (após simetrização).

---

## Tecnologia Utilizada

**Python 3.x** - Escolhido por:
- Sintaxe clara e legível
- Estruturas de dados nativas (set, dict, list)
- Facilidade para manipulação de JSON
- Ideal para prototipagem de algoritmos