from collections import defaultdict
import numpy as np
# import itertools as it
import time

import common

APROX_COMP_PER_SECOND = 150000.0

def generate_random_degrees(n, k):
  '''
    Function that returns an array with the degree for each node
  '''
  degrees = []
  degree_sum = n * k
  for node in range(n):
    x = np.random.randint(1, n)
    if node == n-1:
      degrees.append(degree_sum)
    elif degree_sum - x < 0:
      degrees.append(degree_sum)
      degree_sum = degree_sum - degree_sum
    else:
      degrees.append(x)
      degree_sum -= x

  return degrees


def stubs_vector(degrees):
  '''
    Function that returns a stubs vector
  '''
  stubs = []
  for node, degree in enumerate(degrees):
    for i in range(degree):
      stubs.append(node)
  return stubs


def check_network(n1, n2, stubs, graph):
  if n1 == n2:
    return False
  elif n1 in graph:
    if n2 in graph[n1]:
      return False
  elif n2 in graph:
    if n1 in graph[n2]:
      return False

  return True


def generate_network(stubs, n, waiting_time):
  '''
    Function that returns the cm network
  '''
  start_time = time.time()
  print 'start_time', start_time
  print 'timecontrol: ', waiting_time

  # network = []
  graph = defaultdict(list)
  while len(stubs) > 0:
    i = np.random.randint(0, len(stubs))
    j = np.random.randint(0, len(stubs))
    n1 = stubs[i]
    n2 = stubs[j]
    if check_network(n1, n2, stubs, graph):
      graph[n1].append(n2)
      # Get rid of those nodes
      if i < j:
        del stubs[j]
        del stubs[i]
      else:
        del stubs[i]
        del stubs[j]

    # control loop
    if time.time() - start_time > waiting_time:
      break

  return graph


def configuration_model(n, k):
  '''
    Function that returns the a configuration model graph
  '''
  time_control = n * k / APROX_COMP_PER_SECOND * 60
  degrees = generate_random_degrees(n, k)
  stubs = stubs_vector(degrees)
  network = generate_network(stubs, n, time_control)
  print network
  common.write_pajek('cm', network, n, k)
  common.plot_degree_distribution('cm', degrees, n, None, k)

  