import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

data = pd.read_csv('Dataset/Dataset-creator/csv_files/hallofinalcsv.csv')

#print(data.head(10))

#print(data.isnull().values.sum())

#print(data.isnull().sum())

#data['species']=data['species'].fillna('unknown')

#data.dropna(inplace = True)

#print(data.isnull().values.sum())

data = data.drop(['geometry', 'Unnamed: 0', 'Unnamed: 0.1'], axis = 1)


#x = np.array(data.drop(['prediction'],1))
#y = np.array(data['prediction'])

x = np.array(data.drop(['Pinus sylvestris'],1))
y = np.array(data['Pinus sylvestris'])

print(x.shape)
print(y.shape)


#print(data.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4, random_state = 42)

print('x_train: ', x_train.shape)
print('y_train: ', y_train.shape)
print('x_test: ', x_test.shape)
print('y_test: ', y_test.shape)


rfc = RandomForestClassifier(n_estimators = 100, random_state= 10, max_depth= None, oob_score = True, n_jobs = -1)
rfc.fit(x_train, y_train)

predictions = rfc.predict(x_test)

print('accuracy score of training set: ', accuracy_score(y_train, rfc.predict(x_train)))
print('accuracy score of test set: ', accuracy_score(y_test, predictions))

print('confusion matrix: ', confusion_matrix(y_test, predictions))


#data1 = data.dropna()

#print(data1.isnull().values.sum())

'''
print(data['species'].value_counts())

print(data['species'].value_counts().count())

data.info()
''' 