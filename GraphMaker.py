# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 08:48:12 2021

@author: lasse
"""
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_Plant_With_Occurences_10000.csv')


#print(data.drop('geometry', axis = 1).sum(axis=0)[4:9])
print(data.drop('geometry', axis = 1).sum(axis=0)[4:9].plot()) #laver graf med plantarter på x aksen og grid celler op ad y aksen


#print(data.drop('geometry', axis=1).sum(axis=1)[:20])
print(data.drop('geometry', axis=1).sum(axis=1)[:20].plot(kind='bar', include_bool= True)) #lave en graf med alle gridceller på x akse og observationer på y aksen
