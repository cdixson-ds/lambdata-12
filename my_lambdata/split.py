import pandas
from sklearn.model_selection import train_test_split

import cdixson-ds-lambdata-12==1.0

def split(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.22, random_state=42)
    #length of train, test, and df
    len(X_train), len(X_test), len(X_train) + len(X_test)
    return X_train, X_test, y_train, y_test




