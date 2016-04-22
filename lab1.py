import erdos_renyi as er
import barabasi_albert as ba
import config_model as cm

import common

options = raw_input('What do you want to do? \n A) Erdos Renyi G(N,p) run.\n B) Erdos Renyi G(N,K)\n C) Barabasi Albert run.\n D) Configuration Network run.\nChoice: ')

if options in ['A','a']:
  k = raw_input('Desired average degree?:')
  n = raw_input('Number of nodes?:')
  print 'probability will be calculated based on the desired degree for you.'
  p = common.calculate_probability(float(k), float(n))
  print 'probability: ', p
  er.erdos_renyi_gnp(int(n), float(p))
elif options in ['B','b']:
  n = raw_input('Number of nodes?:')
  k = raw_input('Number of edges?:')
  er.erdos_renyi_gnk(int(n), int(k))
elif options in ['C','c']:
  n = raw_input('Number of nodes?:')
  m = raw_input('Number of edges per node:')
  ba.barabasi_albert(int(n), int(m))
elif options in ['D','d']:
  k = raw_input('Desired average degree?:')
  n = raw_input('Number of nodes?:')
  cm.configuration_model(int(n), int(k))