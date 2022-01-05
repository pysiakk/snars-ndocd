import time

from NDOCD import NDOCD
import Community
import numpy as np
from scipy import sparse

def find_communities(path, k=None):


    graph = sparse.csr_matrix(np.genfromtxt(path, delimiter=","))
    adj = np.genfromtxt(path, delimiter=",")
    start = time.time()
    ndocd = NDOCD(graph, remove_all=True)
    ndocd.JS_threshold = 0.3
    ndocd.MD_threshold = 0.5
    coms = ndocd.find_all_communities()

    if k is not None:
        array_coms = []
        for com in coms[:k]:
            array_coms.append(com.toarray().reshape(-1))
        array_coms = np.asarray(array_coms)

        for com in coms[k:]:
            for node in com.indices:
                place = np.argmax(array_coms @ adj[node])
                array_coms[place][node] = 1
    else:
        array_coms = []
        for com in coms:
            array_coms.append(com.toarray().reshape(-1))
        array_coms = np.asarray(array_coms)

    tt = time.time() - start
    with open("times.txt", "a") as f:
        f.write(path[12:] + ", " + str(tt) + "\n")

    communities = np.row_stack((np.arange(1, array_coms.shape[1] + 1), np.argmax(array_coms, axis=0) + 1)).T
    np.savetxt(path[12:], communities.astype(int), fmt='%i', delimiter=",")

with open("times.txt", "w") as f:
    f.write("")

find_communities("Communities/D1-K=2.csv", k=2)
find_communities("Communities/D1-UNC.csv", k=None)
find_communities("Communities/D2-K=7.csv", k=7)
find_communities("Communities/D2-UNC.csv", k=None)
find_communities("Communities/D3-K=12.csv", k=12)
find_communities("Communities/D3-UNC.csv", k=None)