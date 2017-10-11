import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
from seaborn.linearmodels import corrplot,symmatplot
from sklearn.model_selection import KFold
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics
import csv

##To convert categorical data to numerical data

def label_encoding(column):
    le = LabelEncoder()
    le.fit(column)
    column = le.transform(column)
    return column


def encode(df):
      for column in df.columns:
        df[column]=label_encoding(df[column])
            
            
def cv(folds,model,X,y):
            scores = cross_val_score(model, X, y, cv=folds)
            print "Cross-validated scores:", scores

  

## Reading the data
df = pd.read_csv('mushroom_train.csv')
df_test = pd.read_csv('mushroom_test.csv')


encode(df)
encode(df_test)
            
            
y_df=df['class']
df.drop(['class'],axis=1,inplace=True)
df.drop(['veil-type'],axis=1,inplace=True)
df_test.drop(['veil-type'],axis=1,inplace=True)
            
X=df.values
y=y_df.values            
            
## model
model=RandomForestClassifier(n_estimators=300)

model.fit(X,y)
predictions=model.predict(df_test.values)

# To csv
prediction = pd.DataFrame(predictions,columns=['Class']).to_csv('Submission.csv',columns=['Class'],index=False)

