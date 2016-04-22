from collections import defaultdict
import itertools as it
import numpy as np

import operator

import common


def erdos_renyi_gnp(n, p):
  '''
    Function that generates an Erdos Renyi graph with n nodes with probability p
  '''
  graph = defaultdict(list)
  
  for i in it.permutations(range(n),2): 
    if np.random.random() < p:
      graph[i[0]].append(i[1])

  degrees, average = common.node_degree(graph)
  print 'actual average degree: ', average 
  common.write_pajek('er', graph, n, average)
  common.plot_degree_distribution('er', degrees, n, average, p)
  common.plot_ccdf('er', degrees, n, average, p)


def erdos_renyi_gnk(n, k):
  '''
    Function that generates an Erdos Renyi graph with n nodes with k edges
  '''
  edges = 0
  graph = defaultdict(list)
  while edges < k:
    i = np.random.randint(n)
    j = np.random.randint(n)
    if i == j or j in graph[i]: continue
    graph[i].append(j)
    edges += 1

  degrees, average = common.node_degree(graph)
  print 'average degree: ', average 







