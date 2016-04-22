from collections import defaultdict
import itertools as it
import numpy as np

import common


def generate_clique():
  '''
    Function that returns the initial graph to work with in the BA network (its a clique size n/4)
  '''
  graph = defaultdict(list)
  small_network_size = 5

  for i in it.permutations(range(small_network_size),2): 
    graph[i[0]].append(i[1])

  return graph


def connections(degrees):
  '''
    Function that returns indexes for checking the connection probabilities
  '''
  connection_index = []
  connection_index.append(degrees[0])
  for i in range(1, len(degrees)):
    connection_index.append(connection_index[i - 1] + degrees[i])
  return connection_index


def get_node(p, slot_indexes):
  # Handle edges
  length = len(slot_indexes)
  if p < slot_indexes[0]:
    return 0

  for i in range(1, length):
    if p > slot_indexes[i - 1] and p <= slot_indexes[i]:
      return i


def barabasi_albert(n, m):
  '''
    Function that generates a BA network with n nodes and m edges per node
  '''
  starting_network = generate_clique()
  graph = starting_network

  for node in range(len(starting_network), n):
    # Recalculate degrees
    degrees, average = common.node_degree(graph)
    degree_sum = average * len(graph)
    slot_indexes = connections(degrees)

    for edge in range(m):
      p = np.random.random() * degree_sum
      selected_node = get_node(p, slot_indexes)

      # if the connection is already done, get another node
      while selected_node in graph[node]:
        p = np.random.random() * degree_sum
        selected_node = get_node(p, slot_indexes)
      
      graph[node].append(selected_node)
      graph[selected_node].append(node)

  degrees, average = common.node_degree(graph)
  common.mle(n, degrees)
  common.write_pajek('ba', graph, n, average)
  common.plot_degree_distribution('ba', degrees, n, average, 0.0)
  print "PLOTING"
  common.log_histogram(degrees, 10)
  common.plot_log_degree_distribution('ba', degrees, n, m, 0.0)
  common.plot_log_ccdf('ba', degrees, n, m, 0.0)

