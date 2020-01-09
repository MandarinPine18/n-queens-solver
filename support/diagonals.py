from collections import deque
import numpy as np


def posDiagonalMan(array, offset=1):
    columns = np.ma.size(array, axis=1)
    rows = np.ma.size(array, axis=0)
    newar = np.zeros((1, rows))

    for i in range(columns):
        d1 = np.array([np.diag(array, i * offset)])
        d2 = np.array([np.diag(array, -columns + (i*offset))])
        d = np.hstack((d1, d2))
        newar = np.vstack((newar, d))

    newar = np.delete(newar, 0, 0)
    return newar


def negDiagonalMan(arr, offset=1):
    array = np.flip(arr, 1)
    columns = np.ma.size(array, axis=1)
    rows = np.ma.size(array, axis=0)
    newar = np.zeros((1, rows))

    for i in range(columns):
        d1 = np.array([np.diag(array, i * offset)])
        d2 = np.array([np.diag(array, -columns + (i * offset))])
        d = np.hstack((d1, d2))
        newar = np.vstack((newar, d))

    newar = np.delete(newar, 0, 0)
    return newar


def diagVer(array):
    columns = np.ma.size(array, axis=1)
    err = False

    for i in range(columns*2-1):
        d = np.array([np.diag(array, i + 2 - columns)])
        if np.sum(d) > 1:
            err = True
            break
        else:
            pass

    return not err
