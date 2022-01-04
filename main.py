from NDOCD import NDOCD
import Community
import numpy as np

d1k2 = np.genfromtxt("Communities/D1-K=2.csv", delimiter=",")
ndocd = NDOCD(d1k2)
ndocd.JS_threshold = 0.3
ndocd.MD_threshold = 0.3
coms = ndocd.find_all_communities()
print(coms)