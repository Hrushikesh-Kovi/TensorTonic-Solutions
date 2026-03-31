import numpy as np

def mean_squared_error(y_pred, y_true):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return np.sum((y_pred - y_true)**2) / len(y_true)