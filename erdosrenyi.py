from collections import defaultdict
import itertools
import numpy as np

import operator

import common

def calculate_probability(k, n):
  '''
    Function that calculates de desired probability from a wanted degree for the ER generation
  '''
  edges = k * n / 2
  print 'edges:', edges
  p = edges / (n * (n - 1) / 2)
  return p


def node_degree(graph):
  '''
    Function that returns the degrees of a graph and the average degree
  '''
  degrees = []
  average = 0
  for node in graph:
    number_of_nodes = len(graph[node])
    average += number_of_nodes
    degrees.append(number_of_nodes)
  average = average/len(graph)
  return degrees, average


def erdos_renyi_gnp(n, p):
  '''
    Function that generates an Erdos Renyi graph with n nodes with probability p
  '''
  graph = defaultdict(list)
  
  for i in itertools.permutations(range(n),2): 
    if np.random.random() < p:
      graph[i[0]].append(i[1])

  common.write_pajek(graph,str(1))
  degrees, average = node_degree(graph)
  print 'actual average degree: ', average 
  common.plot_degree_distribution(degrees, n, p)
  common.plot_ccdf(degrees, n, p)


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

  degrees, average = node_degree(graph)
  print 'average degree: ', average 

options = raw_input('What do you want to do? \n A) Erdos Renyi G(N,p) run.\n B) Erdos Renyi G(N,K)\n C) Barabasi & Albert run.\nChoice: ')
if options in ['A','a']:
  k = raw_input('Desired average degree?:')
  n = raw_input('Number of nodes?:')
  print 'probability will be calculated based on the desired degree for you.'
  p = calculate_probability(float(k), float(n))
  print 'probability: ', p
  erdos_renyi_gnp(int(n), float(p))
elif options in ['B','b']:
  n = raw_input('Number of nodes?:')
  k = raw_input('Number of edges?:')
  erdos_renyi_gnk(int(n), int(k))
elif options in ['C','c']:
  print 'hehe'






