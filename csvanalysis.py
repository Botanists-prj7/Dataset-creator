from logging import error
from os import sep
import geopandas as gpd
from matplotlib import pyplot as plt
from pandas.io import pytables
import shapely
import numpy as np
import pandas as pd
import codecs


plants = pd.read_csv('outfiles/floradanica.csv', error_bad_lines=False, sep='\t', engine='python')
for df in plants:
    print(df)
newplants = plants[['decimalLongitude','decimalLatitude','species']]
newplants.to_csv('outfiles/data_with_lat_long.csv')

newplants['POINT'] = newplants['decimalLatitude'].map(str) + ', ' + newplants['decimalLongitude'].map(str)
newnewplants = newplants[['species','POINT']]


newnewplants.to_csv('outfiles/data_with_points_column.csv')

plants = pd.read_csv('floradanicaupdate.csv')
print(plants)
list_of_plants = pd.DataFrame([])
for df in pd.read_csv("floradanica.csv", error_bad_lines=False, sep='\t', engine='python', iterator=True, chunksize=1000):
    print("+1")
    list_of_plants = list_of_plants.append(pd.DataFrame(df.groupby(["kingdom"]).size()))

print(list_of_plants.sort_values(by="kingdom", ascending=False).head(10))

print("Total rows: " + str(sum(list_of_plants)))

