import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_pickle("data_preprocessed\\preprocessed")
y = df['booking_status_cat']
X = df.loc[:, ~df.columns.isin(['booking_status_cat'])]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25,  shuffle=True)
clf = RandomForestClassifier(n_estimators=100,
    random_state=1337,
    max_depth=14,
    min_samples_leaf=1,
    verbose=2)
clf.fit(X_train, y_train)

with open('models\\clf.pickle', 'wb') as handle:
    pickle.dump(clf, handle, protocol=pickle.HIGHEST_PROTOCOL)