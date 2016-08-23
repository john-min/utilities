from __future__ import division
import numpy as np
import cPickle as pickle

def normalize(X):
    P = X.shape[1]
    for p in xrange(P):
        mean = np.mean(X[:,p]).real.astype(float)
        var = np.var(X[:,p]).real.astype(float)
        col = X[:,p]
        X[:,p] = (col-mean)/var
    return X

def split_train_test(X, y, train_prop):
    assert train_prop > 0 and train_prop < 1
    N, P = X.shape
    N_train = int(train_prop*N)
    N_test = N - N_train
    row_idx = [i for i in xrange(N)]
    random.shuffle(row_idx)
    train_idx = row_idx[:N_train]
    test_idx = row_idx[N_train:]
    X_train = X[train_idx,:]
    y_train = y[train_idx,:]
    X_test = X[test_idx,:]
    y_test = y[test_idx,:]
    return X_train, y_train, X_test, y_test, N_train, N_test
