# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:46:26 2021

@author: lasse
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import csvTools


HeatmapData = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_Plant_With_Occurences_10000.csv')

gdf = csvTools.convert_csv_to_gdf('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_Plant_With_Occurences_10000.csv', True, 'EPSG:3857')
gdf = gdf.to_crs('EPSG:4326')


gdf['x'] = gdf['geometry'].centroid.x
gdf['y'] = gdf['geometry'].centroid.y

print(gdf['x'])

sns.kdeplot(data=gdf, x='x', y= 'y', fill= True, cmap = 'coolwarm', alpha = 0.3, gridsize = 200, levels = 20, ax = ax)


'''HeatmapData[['occurences']] = HeatmapData.drop('geometry', axis=1).sum(axis=1)
h2 = HeatmapData[['geometry','occurences']]
plt.imshow(h2, cmap = 'PiYG')

plt.title('test map')
plt.show()
'''
