from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def write_pajek(ntype, graph, n, k):
  file = open('pajek/'+ntype+'_'+str(n)+'_'+str(k)+'.net', 'w')
  file.write('*Vertices ')
  file.write(str(n))
  file.write('\n')
  file.write('*Edges')
  file.write('\n')
  for node in graph:
    for connection in graph[node]:
      file.write(str(node + 1) + ' ' + str(connection + 1) + '\n')

  file.close()


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


def calculate_probability(k, n):
  '''
    Function that calculates de desired probability from a wanted degree for the ER generation
  '''
  edges = k * n / 2
  print 'edges:', edges
  p = edges / (n * (n - 1) / 2)
  return p


def plot_degree_distribution(ntype, degrees, n, k, p=0.0):
  '''
    Function that plots the degree distribution of a network
  '''
  plt.hist(degrees, normed=True, stacked=True, color="#3F5D7D", bins=len(degrees))
  plt.title('Degree Distribution\n Nodes = {}, Probability = {}'.format(n, round(p,2)))
  plt.ylabel('Probability', fontsize=16);
  plt.xlabel('Degree', fontsize=16);
  fig = plt.gcf()
  fig.savefig('plots/'+ntype+'_dd_'+str(n)+'_'+str(k)+'.png')
  plt.show()


def plot_ccdf(ntype, degrees, n, k, p=None):
  '''
    Function that plots the degree distribution of a network
  '''
  plt.hist(degrees, normed=True, histtype='step', color="#3F5D7D", cumulative=True,bins=len(degrees))
  plt.title('Complementary Cumulative Degree Distribution\n Nodes = {}, Probability = {}'.format(n, round(p,2)))
  plt.ylabel('Probability', fontsize=16);
  plt.xlabel('Degree', fontsize=16)
  fig = plt.gcf()
  fig.savefig('plots/'+ntype+'_ccdf_'+str(n)+'_'+str(k)+'.png')
  plt.show()


def linear_regression(degrees, n):
  probability_log = defaultdict(float)
  probability = defaultdict(float)
  for node in degrees:
    probability_log[np.log(node)] += 1
    probability[node] += 1

  sum_x = sum_y = sum_xy = sum_x2 = 0
  for degree in probability:
    probability[degree] = np.log(probability[degree]/n)

  print probability

  for degree in probability_log:
    y = np.log(probability_log[degree]/n)
    probability_log[degree] = y
    sum_x += degree
    sum_y += y
    sum_xy += (degree * y)
    sum_x2 += (degree * degree)


  a = (sum_xy - (sum_x * sum_y) / len(probability_log)) / (sum_x2 - ((sum_x ** 2) / len(probability_log)))
  b = (sum_y - a * sum_x) / len(probability_log)
  print 'a', a
  print 'b', b
  print probability
  print probability_log

  kmax = max(degrees)
  kmin = min(degrees)

  x = []
  y = []
  x.append(np.log(kmin))
  y.append(probability_log[x[-1]])
  x.append(np.log(kmax))
  y.append(probability_log[x[-1]])
  
  return x, y


def plot_log_degree_distribution(ntype, degrees, n, m, p=0.0):
  '''
    Function that plots the degree distribution of a network
  '''
  x, y = linear_regression(degrees, n)

  plt.hist(np.log(degrees), normed=True, stacked=True, color="#3F5D7D", bins=len(degrees), log=True)
  plt.title('Degree Distribution in Log scale\n Nodes = {}, m = {}'.format(n,m))
  plt.ylabel('Probability', fontsize=16);
  plt.xlabel('Degree', fontsize=16);

  plt.plot(x, y, 'r--')
  fig = plt.gcf()
  fig.savefig('plots/'+ntype+'_log_dd_'+str(n)+'_'+str(m)+'.png')
  plt.show()

  # plt.semilogy(x, y, 'r--')
  # plt.semilogy("log", nonposy='clip')
  # plt.show()


def plot_log_ccdf(ntype, degrees, n, m, p=0.0):
  '''
    Function that plots the degree distribution of a network
  '''
  plt.hist(np.log(degrees), normed=True, histtype='step', color="#3F5D7D", cumulative=True,bins=len(degrees), log=True)
  plt.title('Complementary Cumulative Degree Distribution in Log scale\n Nodes = {}, m = {}'.format(n, m))
  plt.ylabel('Probability', fontsize=16);
  plt.xlabel('Degree', fontsize=16)
  fig = plt.gcf()
  fig.savefig('plots/'+ntype+'_ccdf_'+str(n)+'_'+str(m)+'.png')
  plt.show()


def mle(n, degrees):
  summatory = 0.0
  kmin = min(degrees)

  for degree in degrees:
    summatory += np.log( degree / (kmin - 1/2 ) )

  thingy = summatory ** -1
  result = 1 + (n * (thingy))

  print 'MLE:', result


def log_histogram(degress, bins):
    kmin = min(degress)
    kmax = max(degress)

    log_deg = []
    for degree in range(len(degress)):
        log_deg.append(np.log(degress[degree]))

    bins_vals = np.linspace(np.log(kmin), np.log(kmax+1), bins)
    digitized = np.digitize(log_deg, bins_vals)
    digitized = digitized.tolist()
    bins_values = [0] * bins
    for i in range(bins):
        bins_values[i]  = digitized.count(i+1)

    bins_prob = [0] * len(bins_values)
    bins_prob_log = [0] * len(bins_values)
    for i in range(len(bins_values)):
        bins_prob[i] = bins_values[i] / float(len(degress))
        if (bins_prob[i] != 0.0):
            bins_prob_log[i] = np.log(bins_prob[i])

    a, b = np.polyfit(bins_values, bins_prob_log, 1)
    plt.loglog(bins_prob, basex=2)
    plt.show()

    print 'log_deg:', log_deg
    print 'bins_vals', bins_vals
    print 'bins_values', bins_values
    print 'bins_prob', bins_prob
    print a, b
  