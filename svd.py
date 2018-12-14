# This script is a naive implementation of SVD

import numpy as np

def svd(A):
    A = np.array(A)
    B = np.matmul(A.T, A)
    w, v = np.linalg.eig(B)
    u = []
    for i in range(len(w)):
        u_i = 1/w[i]*np.matmul(A, v[:,i])
        u.append(u_i)
    return np.array(u).T, w, v.T