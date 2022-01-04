import time

import numpy as np
from scipy.sparse import coo_matrix
import pandas as pd

from NDOCD import NDOCD


def replace(array, to_replace):
    new_array = np.zeros(array.shape)
    for key in to_replace:
        new_array[array == key] = to_replace[key]
    return new_array


def create_graph_by_cols_and_rows(size, cols, rows):
    vals = np.ones(shape=[cols.shape[0]])
    rang = np.arange(size)
    mat = coo_matrix((vals, (rows, cols)), shape=[size, size]).todok()
    mat[cols, rows] = vals
    mat[rang, rang] = np.zeros(shape=[size])
    mat = mat.tocsr()
    mat.data = np.ones(mat.data.shape[0])
    return mat


def get_email_graph():
    data = pd.read_csv("data/email-Eu-core.txt", delimiter=" ", comment='#', header=None)
    uniques = np.unique(data.iloc[:, 0:2])
    size = uniques.shape[0]
    to_replace = dict((val, i) for (i, val) in enumerate(uniques))
    cols = replace(np.array(data.iloc[:, 0]), to_replace)
    rows = replace(np.array(data.iloc[:, 1]), to_replace)
    return create_graph_by_cols_and_rows(size, cols, rows)


graph = get_email_graph()
start = time.time()
ndocd = NDOCD(graph, remove_all=True, modification=True, modification_type="number", modification_number=20)
ndocd.JS_threshold = 0.8
ndocd.MD_threshold = 0.25

coms = ndocd.find_all_communities(prune_every=1)

print(f'n communities {len(coms)}')
