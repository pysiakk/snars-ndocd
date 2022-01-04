import time

from NDOCD import NDOCD
import Community
import numpy as np
from scipy import sparse

d1k2 = sparse.csr_matrix(np.genfromtxt("Communities/D1-UNC.csv", delimiter=","))
# print(d1k2[60])
start = time.time()
ndocd = NDOCD(d1k2, remove_all=True)
ndocd.JS_threshold = 0.3
ndocd.MD_threshold = 0.5
coms = ndocd.find_all_communities()
print(time.time() - start)
print(len(coms))
for com in coms:
    print(np.sum(com.todense()))
    print(com.indices)
