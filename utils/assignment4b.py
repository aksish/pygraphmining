import os

import numpy as np
import scipy as sp
from sklearn.cluster import KMeans

os.chdir('D:\idea projects\pycharm projects\pygraph')

data1 = np.loadtxt('dataset/Dataset2Edges.txt')
node_pos = np.loadtxt('dataset/Dataset2Nodes_Layout.txt')

import networkx as nx

graph = nx.from_edgelist(data1)

# In[72]:


laplacian1 = nx.laplacian_matrix(graph)

import matplotlib.pyplot as plt

nx.draw_networkx(graph, with_labels=False, node_size=10, width=.3)
plt.show()

eig, eiv = sp.linalg.eigh(laplacian1.todense())

x = np.column_stack((eiv[:, 1], eiv[:, 2]))
kmeans = KMeans(n_clusters=4).fit(x)
labels = kmeans.labels_


def getlbl(i):
    color = ""
    if i == 0:
        color = 'red'
    elif i == 1:
        color = 'blue'
    elif i == 2:
        color = 'green'
    elif i == 3:
        color = 'yellow'
    return color


nx.draw_spectral(graph, node_color=list((getlbl(i) for i in labels)), with_labels=False, width=0.5, node_size=50)
plt.show()


plt.grid(True)
plt.scatter(eiv[:, 1], eiv[:, 2], c=list((getlbl(i) for i in labels)))
plt.show()
