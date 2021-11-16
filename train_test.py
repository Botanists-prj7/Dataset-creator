import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

def print_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    print('True positive = ', cm[0][0])
    print('False positive = ', cm[0][1])
    print('False negative = ', cm[1][0])
    print('True negative = ', cm[1][1])

data = pd.read_csv('csv_files/hallofinalcsv.csv')

#print(data.head(10))

#print(data.isnull().values.sum())

#print(data.isnull().sum())

#data['species']=data['species'].fillna('unknown')

#data.dropna(inplace = True)

#print(data.isnull().values.sum())

data = data.drop(['geometry', 'Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1'], axis = 1)
print("data efter dropped geo og det der", data.head())
#data = data.drop(data.columns[59:2907], axis = 1)

#x = np.array(data.drop(['prediction'],1))
#y = np.array(data['prediction'])

x = np.array(data.drop(['Salix caprea'],1))
y = np.array(data['Salix caprea'])

print(x.shape)
print(y.shape)


#print(data.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

print('x_train: ', x_train.shape)
print('y_train: ', y_train.shape)
print('x_test: ', x_test.shape)
print('y_test: ', y_test.shape)

rfc = RandomForestClassifier(n_estimators = 10000, random_state= 10, max_depth = None, oob_score = True, n_jobs = -1)
rfc.fit(x_train, y_train)

predictions = rfc.predict(x_test)

print('accuracy score of training set: ', accuracy_score(y_train, rfc.predict(x_train)))
print('accuracy score of test set: ', accuracy_score(y_test, predictions))
print('confusion matrix: ')
print(confusion_matrix(y_test,predictions))
print_confusion_matrix(y_test,predictions)


feature_list = list(data.columns)
importances = list(rfc.feature_importances_)
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
counter = 0
for pair in feature_importances:
    if counter == 50:
        break
    print('Variable: {:20} Importance: {}'.format(*pair))
    counter+=1


#data1 = data.dropna()

#print(data1.isnull().values.sum())

'''
print(data['species'].value_counts())

print(data['species'].value_counts().count())

data.info()
''' 