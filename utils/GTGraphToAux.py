import os

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def to_auxiliary_matrix(gt_graph_file):
    data = np.loadtxt(gt_graph_file, dtype=int, skiprows=8, usecols=(1, 2))
    with open(gt_graph_file) as meta:
        meta.readline();
        meta_line = meta.readline();
        nodes_count = int(meta_line.split(" ")[4])

    auxiliary = np.zeros(shape=(nodes_count, nodes_count), dtype=int)
    for item in data:
        print(item)
        row = item[0] - 1
        col = item[1] - 1
        auxiliary[row, col] = 1
    return auxiliary


def main():
    os.chdir("D:\Linux VM\shared")
    auxiliary_matrix = to_auxiliary_matrix("test1.gh")

    G = nx.from_numpy_matrix(auxiliary_matrix)
    nx.draw_random(G, with_labels=True)
    plt.show()


if __name__ == "__main__":
    main()
