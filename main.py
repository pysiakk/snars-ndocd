from NDOCD import NDOCD
import Community
import numpy as np
from scipy import sparse

d1k2 = sparse.csr_matrix(np.genfromtxt("Communities/D1-UNC.csv", delimiter=","))
ndocd = NDOCD(d1k2, modification=True, modification_number=100, modification_type="number")
ndocd.JS_threshold = 0.3
ndocd.MD_threshold = 0.3
coms = ndocd.find_all_communities()
for com in coms:
    print(np.sum(com.todense()))