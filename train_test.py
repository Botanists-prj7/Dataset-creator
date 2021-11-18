import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import csvTools

def print_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    print('True positive = ', cm[0][0])
    print('False positive = ', cm[0][1])
    print('False negative = ', cm[1][0])
    print('True negative = ', cm[1][1])


crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

thePlantToFind = input('Indtast en plante her: ')

#plant_gdf_grid = csvTools.convert_csv_to_gdf('csv_files\\DK_Plant_10000.csv',True,crs=crs)
#plant_gdf_grid = plant_gdf_grid.drop(columns=['geometry'])
data = csvTools.convert_csv_to_gdf('csv_files\\completedataset_DK_with_occurences_10K.csv',True,crs=crs)
data = data.drop(['geometry','Unnamed: 0'], axis = 1)
#dataNoPlants = data.drop(columns=plant_gdf_grid.columns)

x = np.array(data.drop(columns=[thePlantToFind]))
y = np.array(data[thePlantToFind])

print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

print('x_train: ', x_train.shape)
print('y_train: ', y_train.shape)
print('x_test: ', x_test.shape)
print('y_test: ', y_test.shape)

rfc = RandomForestClassifier(n_estimators = 10000, random_state= 42)
rfc.fit(x_train, y_train)

predictions = rfc.predict(x_test)
probality = rfc.predict_proba(x_test)
print("Probability: ", probality)

print('accuracy score of training set: ', accuracy_score(y_train, rfc.predict(x_train)))
print('accuracy score of test set: ', accuracy_score(y_test, predictions))
print('confusion matrix: ')
print(confusion_matrix(y_test,predictions))
print_confusion_matrix(y_test,predictions)


feature_list = list(data.columns)
importances = list(rfc.feature_importances_)
feature_importances = [(feature, round(importance, 4)) for feature, importance in zip(feature_list, importances)]
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
#[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]
counter = 0
for pair in feature_importances:
    if counter == 200:
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