# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 08:48:12 2021

@author: lasse
"""
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_Plant_With_Occurences_10000.csv')
weatherdata = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/weatherstationjoin_index_final_occurences.csv')

'''
data2=data[['Rosa spinosissima', 'Rumex sanguineus', 'Urtica dioica', 'Impatiens parviflora','Crambe maritima']]
data2.reset_index()
print(data2.sum(axis=0).plot(kind='bar')) 
'''

#print(data.drop('geometry', axis = 1).sum(axis=0)[:].plot(kind='hist', xlabel=None))#laver graf med plantarter på x aksen og grid celler op ad y aksen

#data2 = data.drop('geometry', axis=1).sum(axis=1) 
#print(data2.sort_values()[:20])
#print(data2.sort_values(ascending=False)[:].plot(kind='bar')) #lave en graf med alle gridceller på x akse og observationer på y aksen

#weather data in gridcells
#weatherdata2 = weatherdata[['stationId_x_x']]
#print(weatherdata2.value_counts().plot(kind='bar'))#laver graf med plantarter på x aksen og grid celler op ad y aksen





#data['x']= data['geometry'].centroid.x
#data['y'] = data['geometry'].centroid.y

#GeoData = []
noGeoData = data.drop('geometry', axis = 1).sum(axis=0)#laver et histogram med unikke plantarter på x aksen og grid og hvor mange gridceller de er observeret i, på y-aksen

#['sum'] = noGeoData
#plt.plot(noGeoData.sort_values())


print(noGeoData)
plt.hist(noGeoData, bins = 50)
plt.title('Amount of grid cells each plant is observed in', fontsize=25)
plt.ylabel('Number of plants', fontsize=20)
plt.xlabel('Number of grid cells', fontsize=20)
plt.show

'''
noGeoData = data.drop('geometry', axis = 1).sum(axis=1) #lave et histogram der viser en mængde planter på x-aksen og hvor mange gridcells, som har den mængde planter på y-aksen
print(noGeoData.sort_values())
plt.hist(noGeoData, bins = 50)
plt.title('Amount of plants observed in each grid cell', fontsize=25)
plt.ylabel('Number of grid cells', fontsize=20)
plt.xlabel('Number of plants', fontsize=20)
plt.show

'''


