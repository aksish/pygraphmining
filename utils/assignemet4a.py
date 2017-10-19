import os

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import scipy as sp
from sklearn.neighbors import NearestNeighbors


def main():
    os.chdir("D:\idea projects\pycharm projects\pygraph\dataset")
    data = np.loadtxt("Dataset1.txt", usecols=(0, 1))
    nbrs = NearestNeighbors(n_neighbors=5).fit(data)
    distances, indices = nbrs.kneighbors(data)
    g_data = nbrs.kneighbors_graph(mode='distance')
    g = nx.from_scipy_sparse_matrix(g_data)
    laplacian = nx.laplacian_matrix(g)
    # print(nx.is_connected(g))
    d = list(nx.connected_component_subgraphs(g))
    print(len(d))
    # nx.write_graphml(g, 'assignement1.graphml')
    eigen_val, eigen_vec = sp.sparse.linalg.eigsh(laplacian)
    nx.draw_networkx(g, with_labels=False, node_size=100, edge_color='blue')
    plt.show()


if __name__ == '__main__':
    main()
