
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
        
def generate_csv(model,train,target,test,filename):
  model.fit(train,target)
  pred=model.predict(target)
  with open(filename,'wb) as file:
            
  

## Reading the data
df = pd.read_csv('mushroom_train.csv')
df_test = pd.read_csv('mushroom_test.csv')

