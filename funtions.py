import pandas as pd

df = pd.read_csv("spam.csv", encoding='unicode_escape')

df['spam'] = df['Category'].apply(lambda x: 1 if x=='spam' else 0)

from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam)
X_train = df.Message
y_train = df.spam

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

clf.fit(X_train, y_train)

import pickle

with open('model_pickle', 'wb') as file:
    pickle.dump(clf, file)
