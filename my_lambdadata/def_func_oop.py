import numpy as np


class confusion_matrix():
    def compute_confusion_matrix(self, X_true, y_pred):
        K = len(np.unique(X_true))  # Number of classes
        result = np.zeros((K, K))

        for i in range(len(X_true)):
            result[X_true[i]][y_pred[i]] += 1
        return result

if __name__ == "__main__":

    confusion_matrix_result = confusion_matrix()
    




''' ----------------------------------------------'''

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from IPython.display import display


class my_data_splitter():
    def __init__(self, df, features, target):
        self.df = df
        self.features = features
        self.target = target
        self.X = df[features]
        self.y = df[features]

    def train_validation_test_split(self,
                                    train_size=0.7, val_size=0.1,
                                    test_size=0.2, random_state=None,
                                    shuffle=True):
        '''
        This function is a utility wrapper around the Scikit-Learn train_test_split that splits arrays or 
        matrices into train, validation, and test subsets.
        Args:
            df (pandas dataframe) dataframe with code
            X (list): A list of features.
            y (str): A string with target column.
            train_size (float or int): Proportion of the dataset to include in the train split (0 to 1).
            val_size (float or int): Proportion of the dataset to include in the validation split (0 to 1).
            test_size (float or int): Proportion of the dataset to include in the test split (0 to 1).
            random_state (int): Controls the shuffling applied to the data before applying the split for reproducibility.
            shuffle (bool): Whether or not to shuffle the data before splitting
        Returns:
            Train, test, and validation dataframes for features (X) and target (y). 
        '''
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, shuffle=shuffle)

        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
            random_state=random_state, shuffle=shuffle)

        return X_train, X_val, X_test, y_train, y_val, y_test
    
    def print_split_summary(self, X_train, X_val, X_test):

        print('############# Training Data ################')
        print(f'X_train shape: {X_train.shape}')
        display(X_train.describe(include='all').transpose())
        print('')

        print('############# Validation Data #############')
        print(f'X_val shape: {X_val.shape}')
        display(X_val.describe(include='all').transpose())
        print('')

        print('############## Test Data ##################')
        print(f'X_test shape: {X_test.shape}')
        display(X_test.describe(include='all').transpose())
        print('')


if __name__ == "__main__":
   

  # test for train_validation_test_split function
    raw_data = load_wine()
    df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    df['target'] = raw_data['target']

