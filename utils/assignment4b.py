import os
import networkx as nx

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def get_color(i):
    if i==0:
        return "red"
    if i==1:
        return "green"
    if i==2:
        return "blue"
    if i==3:
        return "black"


def graphToEdgeMatrix(G):

    edgeMat = [[0 for x in range(len(G))] for y in range(len(G))]
    for node in G:
        tempNeighList = G.neighbors(node)
        for neighbor in tempNeighList:
            edgeMat[node][neighbor] = 1
        edgeMat[node][node] = 1

    return edgeMat
    plt.scatter()

def main():
    os.chdir("D:\idea projects\pycharm projects\pygraph\dataset")
    dataset = np.loadtxt("Dataset2Edges.txt")
    graph = nx.from_edgelist(dataset)
    graph = nx.convert_node_labels_to_integers(graph)
    edgeMMatrix = graphToEdgeMatrix(graph)
    cluster_map = nx.clustering(graph)
    a
    coffs = []
    for i in sorted(cluster_map):
        coffs.append([1, cluster_map.get(i)])
    print(coffs)
    partition = KMeans(n_clusters=4, precompute_distances=True).fit(coffs)
    nx.draw_networkx(graph,node_color=list((get_color(x) for x in partition.labels_)),with_labels=False)
    plt.show()


if __name__ == '__main__':
    main()
