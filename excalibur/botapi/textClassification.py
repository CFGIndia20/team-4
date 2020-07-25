import json as j
import pandas as pd
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
# from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2

# Reading the models
data = pd.read_csv('./cd_mumbai_complaints.csv')
print(data['category_id'].isnull().sum())
y = data['category_id'].values.astype(np.int64)
z = data['sub_category_id']

print(pd.DataFrame(y).info())

# Preprocessing
stemmer = SnowballStemmer('english')
words = stopwords.words("english")

data['cleaned'] = data['description'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ", str(x)).split() if i not in words]).lower())

print(data['cleaned'].head(5))

# Word Vectorization
from sklearn.feature_extraction.text import CountVectorizer
# min_df=5, max_df=0.7,
# max_features=100, min_df=1, max_df=7,stop_words=stopwords.words('english')
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['cleaned']).toarray()

tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, y_train) 

print(classifier)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

def preprocessData(descp):
    """
        Preprocesses the sentences
    """
    # Stopwords removed
    # descp = descp.apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ", str(x)).split() if i not in words]).lower())
    descp = " ".join([w.lower() for w in descp.split() if w not in words])
    
    # Words to bag
    # vectorizer = CountVectorizer(max_features=1500, min_df=1, max_df=0.7, stop_words=stopwords.words('english'))
    # vectorizer = TfidfVectorizer(min_df=1, max_df=1, stop_words=stopwords.words('english'))
    X = vectorizer.transform([descp]).toarray()
    
    # Tfidf Convertor
    tfidfconverter = TfidfTransformer()
    X = tfidfconverter.fit_transform(X).toarray()
    
    return X

def predictClass(x_pred):
    return classifier.predict(x_pred)

# 
# function textClassifier
# @param(descp) : str, descprition of the user complaint
# Return - category id
def textClassifier(descp):
    """
        Predicts category from description
    """
    processedDescp = preprocessData(descp=descp)
    return int(predictClass(processedDescp))