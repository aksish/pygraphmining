import os

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import sys
import utils.SpiderSolatire as sp


def get_graph(gt_graph_file):
    data = np.loadtxt(gt_graph_file, dtype=int, skiprows=8, usecols=(1, 2))
    with open(gt_graph_file) as meta:
        print(meta.readline())
        meta_line = meta.readline()
        nodes_count = int(meta_line.split(" ")[4])
        print(meta_line)
        meta_line_2 = meta.readline()
        print(meta_line_2)
        edge_count = int(meta_line_2.split(" ")[5])
        print(meta.readline())
        print(meta.readline())

    auxiliary = np.zeros(shape=(nodes_count, nodes_count), dtype=int)
    for item in data:
        row = item[0] - 1
        col = item[1] - 1
        auxiliary[row, col] = 1
    save_degree_distribution(auxiliary, gt_graph_file + ".png", nodes_count, edge_count)
    return auxiliary


def save_degree_distribution(auxiliary_matrix, image_file_name, nodes_count, edge_count):
    degree_count = np.sum(auxiliary_matrix, axis=0, dtype=int)
    degree, count = np.unique(degree_count, return_counts=True)
    x_degree = degree.flatten()
    y_column = count.flatten()
    title = " Node Degree distribution of a "
    if "rmat" in image_file_name:
        title += " R-Mat "
    else:
        title += " Random "
    title += " Graph n = " + str(nodes_count) + " m = " + str(edge_count)
    plt.title(title)
    plt.xlabel("Node degree")
    plt.ylabel("Number of nodes")
    plt.scatter(x_degree, y_column)
    plt.yscale('symlog')
    plt.xscale('symlog')
    plt.margins(0.2)
    # plt.savefig(image_file_name)
    plt.show();
    plt.close()


def draw_graph(auxiliary_matrix):
    G = nx.from_numpy_matrix(auxiliary_matrix)
    nx.draw_random(G, with_labels=True)
    plt.show()


def main():
    os.chdir("D:\Linux VM\shared")
    for i in range(1, len(sys.argv)):
        get_graph(sys.argv[i])


if __name__ == "__main__":
    main()

