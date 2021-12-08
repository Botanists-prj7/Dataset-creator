from math import e
from geopandas import geodataframe
from numpy.core.numeric import cross
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import csvTools
from sklearn.model_selection import cross_val_score
import geopandas as gpd
from sklearn.utils import shuffle
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV
from sklearn.datasets import make_classification

def print_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    print('True positive = ', cm[1][1])
    print('False positive = ', cm[0][1])
    print('False negative = ', cm[1][0])
    print('True negative = ', cm[0][0])


crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

#Selinum dubium <-- Kun på amar. Meget få forekomster (8)
#Salix caprea <-- Over hele Danmark. Mange observationer. (2000+) 
#Urtica dioica <-- Stornælde MANGE observationer (5000+)
#Dactylis glomerata <-- Hundegræs, mange oberservationer (5000+)
#Crambe maritima <-- Strandkål få observationer (400+) Vokser kun ved kysten.

#Rosa spinosissima
#Rumex sanguineus(wood dock)
#Urtica dioica <-- Stornælde MANGE observationer (5000+)
#Impatiens parviflora
#Crambe maritima <-- Strandkål få observationer (400+) Vokser kun ved kysten.


thePlantToFind = input('Indtast en plante her: ')

#plant_gdf_grid = csvTools.convert_csv_to_gdf('csv_files\\DK_Plant_10000.csv',True,crs=crs)
#plant_gdf_grid = plant_gdf_grid.drop(columns=['geometry'])
data = csvTools.convert_csv_to_gdf('/Users/christianekiel/Desktop/7. semester/Projekt/Dataset/Dataset-creator/csv_files/hallofinalcsv.csv',True,crs=crs)
#data = data.drop(['geometry','Unnamed: 0'], axis = 1)
#dataNoPlants = data.drop(columns=plant_gdf_grid.columns)

""" x_shuffled = shuffle(x, random_state=42)
y_shuffled = shuffle(y, random_state=42)

x_train, x_test, y_train, y_test = train_test_split(x_shuffled, y_shuffled, test_size = 0.30, random_state = 42) """

x = np.array(data.drop(columns=[thePlantToFind]))
y = np.array(data[thePlantToFind])

print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

new_x_train = np.delete(x_train, [0, 1, 2, 3], axis = 1)
new_x_test  = np.delete(x_test, [0, 1 , 2, 3], axis = 1)

#k = 8
#kf = KFold(n_splits=k, random_state=None)

print('x_train: ', x_train.shape)
print('y_train: ', y_train.shape)
print('x_test: ', x_test.shape)
print('y_test: ', y_test.shape)

rfc = RandomForestClassifier(random_state=42)
rfc.fit(new_x_train, y_train)


param_grid = {"n_estimators": [100, 300, 500, 1000],
              "max_depth": [3, 5, 7, 10, 30, 50]}
HGS = HalvingGridSearchCV(rfc, param_grid, cv=5, random_state=42).fit(new_x_train,y_train)

print(HGS.best_estimator_)


#rfc.fit(new_x_train, y_train)
#print(rfc.get_params)

predictions = rfc.predict(new_x_test)
probabilities = rfc.predict_proba(new_x_test)
trueplots = []
negativeplots = []
for index, values in enumerate(predictions):
    #for probality in enumerate(probabilities):
        geo = x_test[index][3]
        prob = probabilities[index][1]
        probabilitylist.append(prob)
        trueplots.append(geo)
    else: 
         geo = x_test[index][3]
         negativeplots.append(geo)
#for i in range(len(x_test)):
    #print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ \n Probability (False, True)=%s \n Prediction=%s \n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ \n" % ((probality[i]*100), (predictions[i])))

rfc2 = RandomForestClassifier(max_depth=7, n_estimators=500, random_state=42)
rfc2.fit(new_x_train, y_train)
predictions2 = rfc2.predict(new_x_test)

print('NY accuracy score of training set: ', accuracy_score(y_train, rfc2.predict(new_x_train)))
print('NY accuracy score of test set: ', accuracy_score(y_test, predictions2))


dataplot = pd.DataFrame({'geometry':trueplots})
dataplot.to_csv('Dataset/Dataset-creator/csv_files/trueplots.csv')
dataplot = pd.DataFrame({'geometry':negativeplots})
dataplot.to_csv('Dataset/Dataset-creator/csv_files/negativeplots.csv')

print(probabilities[1])
print(x_test[3])
#allPlotsGDF = geodataframe({'geometry':x_test[3],'probality':probabilities[1]})
#print(allPlotsGDF)

print('accuracy score of training set: ', accuracy_score(y_train, rfc.predict(new_x_train)))
print(rfc.get_params())


print('accuracy score of training set: ', accuracy_score(y_train, rfc.predict(new_x_train)))

print('accuracy score of test set: ', accuracy_score(y_test, predictions))
print('confusion matrix: ')
print(confusion_matrix(y_test,predictions,labels=[1,0]))
print_confusion_matrix(y_test,predictions)
#for index, values in enumerate(probality):
#  print(index, values)


#result = cross_val_score(rfc2 , x, y, cv = kf)
#print(result)


""" 

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

 """

#print("Cross val score: {}".format(result.mean()),result)
#data1 = data.dropna()

#print(data1.isnull().values.sum())

plants = pd.read_csv('Dataset/Dataset-creator/data/data_with_lat_long.csv', error_bad_lines = False, engine='python')
plantsdub = plants[(plants['species']!=thePlantToFind)].index
plants.drop(plantsdub, inplace=True)

#Make axis :O
fig, ax = plt.subplots(1, figsize=(10,10))

#plot map on axis
countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
countries[countries["name"] == "Denmark"].plot(color="lightgrey", ax=ax)

plants.plot(x="decimalLongitude", y="decimalLatitude", kind="scatter", colormap='PiYG', ax=ax)



#add grid XD
ax.grid(which = "major", b=True, alpha=0.6)
plt.minorticks_on()
ax.grid(which = "minor", b=True, alpha=0.6)

plt.show()

########PLOT DETTE LORTE KORT HER DER IKKE VIRKER LOL
'''
f, ax = plt.subplots(1)

#plot map on axis
countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
countries[countries["name"] == "Denmark"].plot(color="lightgrey", ax=ax)

dataplot = gpd.GeoSeries.from_wkt(dataplot['geometry'])
gdf_plot = gpd.GeoDataFrame(dataplot, geometry=dataplot, crs="EPSG:3857")

print(gdf_plot.describe())
gdf_plot.plot(ax=ax)

#add grid XD
ax.grid(which = "major", b=True, alpha=0.6)
plt.minorticks_on()
ax.grid(which = "minor", b=True, alpha=0.6)

'''

gdf = csvTools.convert_csv_to_gdf('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/completedataset_DK_with_occurences_10K.csv', True, 'EPSG:3857')
gdf.geometry = gdf['geometry']
gdf = gdf.to_crs('EPSG:4326')


gdf['x'] = gdf['geometry'].centroid.x
gdf['y'] = gdf['geometry'].centroid.y


sns.kdeplot(data=gdf, x='x', y= 'y', fill= True, cmap = 'coolwarm', alpha = 0.3, gridsize = 200, levels = 20, ax = ax)


