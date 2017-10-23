import math
import os

import networkx as nx
import numpy as np
import scipy as sp
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors

os.chdir('D:\idea projects\pycharm projects\pygraph')

data1 = np.loadtxt('dataset/Dataset1.txt', usecols=(0, 1, 2))

nbrs1 = NearestNeighbors(n_neighbors=8).fit(data1[:, 0:2])
distances, indices = nbrs1.kneighbors(data1[:, 0:2])
sparse_adj = nbrs1.kneighbors_graph(mode='distance')
adj = sparse_adj.todense()


#     Reference:
#     Lihi Zelnik-Manor and Pietro Perona. "Self-tuning spectral clustering." In NIPS, pp. 1601-1608. 2005.
def get_tuned(adj, k_distance):
    tuned_adj = np.zeros_like(adj)
    for ix, dist in np.ndenumerate(adj):
        sigma_i = k_distance[ix[0], 6]
        sigma_j = k_distance[ix[1], 6]
        if ix[0] != ix[1] and dist != 0:
            tuned_adj[ix[0], ix[1]] = math.exp(-dist ** 2 / (sigma_i * sigma_j))
    return tuned_adj


tuned_adj = get_tuned(adj, distances)

graph1 = nx.from_numpy_matrix(tuned_adj)

laplacian1 = nx.laplacian_matrix(graph1)

import matplotlib.pyplot as plt

nx.draw_networkx(graph1, with_labels=False, node_size=10, width=.3, pos=data1[:, 0:2])
plt.show()

eig, eiv = sp.linalg.eigh(laplacian1.todense())

node_rank = graph1.nodes()

zeros = np.zeros(eig.shape)

x = np.column_stack((zeros, eiv[:, 1]))
kmeans = KMeans(n_clusters=2).fit(x)
labels = kmeans.labels_


def getlbl_kmeans(i):
    if i == 0:
        return 'red'
    elif i == 1:
        return 'blue'
    elif i == 2:
        return 'green'
    elif i == 3:
        return 'black'


for ix, d in enumerate(data1[:, 0:2]):
    x, y = d
    plt.scatter(x, y, c=getlbl_kmeans(labels[ix]))
plt.show()

plt.scatter(graph1.nodes(), eiv[:, 1], c=labels)
plt.grid(True)
plt.show()
