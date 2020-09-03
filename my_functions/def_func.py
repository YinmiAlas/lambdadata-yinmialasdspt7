import numpy as np

def shuffle_split_data(X, y):

    arr_rand = np.random.rand(X.shape[0])
    split = arr_rand < np.percentile(arr_rand, 70)

    X_train = X[split]
    y_train = y[split]
    X_test =  X[~split]
    y_test = y[~split]

    #print(len(X_Train), len(y_Train), len(X_Test), len(y_Test))

    return X_train, y_train, X_test, y_test