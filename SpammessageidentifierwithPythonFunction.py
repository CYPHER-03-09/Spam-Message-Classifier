#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

def predict_spam(message):
    df = pd.read_csv('SPAM text message 20170820 - Data.csv')
    X = df['Message']
    Y = df['Category']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=22)
    pipeSVC = Pipeline([
      ('tfidf', TfidfVectorizer(stop_words='english')),
      ('clf', LinearSVC())])
    pipeSVC.fit(X_train, Y_train)
    preprocessed_message = [message]
    prediction = pipeSVC.predict(preprocessed_message)
    new_predict = " ".join(str(element) for element in prediction)
    return new_predict


# In[10]:




# In[ ]:



