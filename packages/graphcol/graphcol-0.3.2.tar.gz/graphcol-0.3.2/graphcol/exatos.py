import igraph
import random
import numpy as np
import math
import collections
from graphcol.gulosos import Gulosos

class Exatos:
    
  def cromatico_lawler(grafo):
    """
    Função que devolve o número cromático de um grafo. Como se trata de uma função de devolve o valor
    exato deve ser usada com cautela, pois para instâncias a partir de 10 vértices já é possível que
    o tempo de exeução da função ultrapasse 10 minutos. Por isso recomendamos uso em pequenas instâncias
    """

    def lawler(grafo):
      """
      Função responsável por fazer o controle das chamadas recursivas do algoritmo de Lawler,
      basicamente ela faz a primeira chamada recursiva e define algumas outras constantes
      improtantes no processo.
      """
      tipo_arestas = np.dtype('int,int')
      n_vertices = grafo.vcount()
      lista_arestas = grafo.get_edgelist()
      array_arestas = np.array(lista_arestas, dtype = tipo_arestas)
      if n_vertices == 0:
        return math.inf
      if len(lista_arestas) == 0:
        return 1
      return cromatico_lawler(lista_arestas, n_vertices)
      
      def cromatico_lawler(arestas_grafo, n_vertices):
        """
        Função principal do algoritmo de Lawler responsável por fazer os testes de caso base e 
        chamar recursivamente as próximas etapas da recursão.
        """
        if n_vertices == 0:
          return math.inf
        if len(arestas_grafo) == 0:
          return 1
        if len(arestas_grafo) == 1 and n_vertices >= 2:
          return 2
        if ig.Graph(arestas_grafo).is_bipartite():
          return 2
        if ig.Graph(arestas_grafo).is_tree():
          return 2
        X_subgrafo = 0
        ids = 2**n_vertices
        for i in range(ids):
          id_subgrafo = bin(i)[2:].rjust(n_vertices, '0')
          X_subgrafo = n_vertices
          lista_vertices = [(len(id_subgrafo)-i-1) for i in range(len(id_subgrafo)) if id_subgrafo[i] == '1']
          arestas_subgrafo = [(x,y) for (x,y) in arestas_grafo if (x in lista_vertices) and (y in lista_vertices)]
          conjuntos_independentes_maximais = ig.Graph(arestas_grafo).subgraph_edges(arestas_subgrafo, delete_vertices = True).maximal_independent_vertex_sets()
          for conjunto_independente_maximal in conjuntos_independentes_maximais:
            vertices_limpo = [vertice for vertice in lista_vertices if vertice not in list(conjunto_independente_maximal)]
            vertices_limpo = [vertice for vertice in vertices_limpo if vertice in [u for (u,v) in arestas_grafo] + [v for (u,v) in arestas_grafo]]
            arestas_limpo = ig.Graph(arestas_grafo).subgraph(vertices_limpo).get_edgelist()
            X_subgrafo = min(X_subgrafo, cromatico_lawler(arestas_limpo, len(vertices_limpo)) + 1)
        return X_subgrafo
      
      return lawler(grafo)