import matplotlib.pyplot as plt

def write_pajek(graph, n, k):
  file = open('pajek/er_00'+n+'_'+k+'.net', 'w')
  file.write('*Vertices ')
  file.write(str(len(graph)))
  file.write('\n')
  file.write('*Edges')
  file.write('\n')
  for node in graph:
    for connection in graph[node]:
      file.write(str(node + 1) + ' ' + str(connection + 1) + '\n')

  file.close()

def plot_degree_distribution(degrees, n, p):
  '''
    Function that plots the degree distribution of a network
  '''

  plt.hist(degrees, normed=True, stacked=True, color="#3F5D7D", bins=len(degrees))
  plt.title('Degree Distribution\n Nodes = {}, Probability = {}'.format(n, round(p,2)))
  plt.ylabel('Probability', fontsize=16);
  plt.xlabel('Degree', fontsize=16);
  plt.show()

def plot_ccdf(degrees, n, p):
  '''
    Function that plots the degree distribution of a network
  '''

  plt.hist(degrees, normed=True, histtype='step', color="#3F5D7D", cumulative=True,bins=len(degrees))
  plt.title('Complementary Cumulative Degree Distribution\n Nodes = {}, Probability = {}'.format(n, round(p,2)))
  plt.ylabel('Probability', fontsize=16);
  plt.xlabel('Degree', fontsize=16);
  plt.show()