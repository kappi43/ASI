import logging
from typing import Dict, Tuple
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
import pandas as pd

def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    y = data['booking_status_cat']
    X = data.loc[:, ~data.columns.isin(['booking_status_cat'])]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test

def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    clf = RandomForestClassifier(n_estimators=100, random_state=1337, max_depth=14, min_samples_leaf=1, verbose=2)
    clf.fit(X_train, y_train)
    return clf

def evaluate_model(
    classifier: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series
):
    y_pred = classifier.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)