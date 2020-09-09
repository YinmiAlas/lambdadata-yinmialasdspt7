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


