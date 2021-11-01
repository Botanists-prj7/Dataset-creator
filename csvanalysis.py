from logging import error
from os import sep
from re import X
import geopandas as gpd
from geopandas.array import points_from_xy
from matplotlib import pyplot as plt
from pandas.io import pytables
import shapely
import numpy as np
import pandas as pd
import codecs
from shapely import wkt
from shapely import geometry
from shapely.geometry.point import Point
import rtree
from tqdm import tqdm, tqdm_notebook
import time


tqdm.pandas()
print('Reading Grid CSV')
df = pd.read_csv('csv_files/TestDK_Grid_10000.csv')
print('Setting WKT...')
df['geometry'] = df['geometry'].apply(wkt.loads).progress_apply(lambda x: x)
print('Converting projection')
soil = gpd.GeoDataFrame(df, crs='EPSG:3857').progress_apply(lambda x: x)
print('Converting projection...')
soil = soil.to_crs('EPSG:3857').progress_apply(lambda x: x)
#print(df)


print('Converting plants csv')
df2 = pd.read_csv('data/data_with_lat_long.csv')
newdf = df2
print('Applying geometry conversion for plants')
gdf = gpd.GeoDataFrame(newdf, geometry=gpd.points_from_xy(df2['decimalLongitude'], df2['decimalLatitude']), crs='EPSG:4326').progress_apply(lambda x: x)
print('Converting plants data projection')
gdf = gdf.to_crs('EPSG:3857').progress_apply(lambda x: x)
print('Setting geometry for plants')
gdf.set_geometry('geometry').progress_apply(lambda x: x)
#print(gdf.head())

print('Finding intersecting points...')
points_within = gpd.sjoin(gdf, soil, op='within', how='inner').progress_apply(lambda x: x)
gpd.GeoDataFrame(points_within).to_csv('csv_files/plantsoilintersection2.csv')


"""
plants = pd.read_csv('/Users/kaspermadsen/Desktop/data/outfiles/floradanica.csv', error_bad_lines=False, sep='\t', engine='python')

 
for df in plants:
    print(df)
newplants = plants[['decimalLongitude','decimalLatitude','species']]
newplants.to_csv('outfiles/data_with_lat_long.csv')

newplants = plants[['decimalLongitude','decimalLatitude','species']]

newplants['geometry'] = "Point"+"(" + newplants['decimalLatitude'].map(str) + ', ' + newplants['decimalLongitude'].map(str) + ")"}
newnewplants = newplants[['species','geometry']]


newnewplants.to_csv('csv_files/plantsdata.csv')
 
plants = pd.read_csv('floradanicaupdate.csv')
print(plants)
list_of_plants = pd.DataFrame([])
for df in pd.read_csv("floradanica.csv", error_bad_lines=False, sep='\t', engine='python', iterator=True, chunksize=1000):
    print("+1")
    list_of_plants = list_of_plants.append(pd.DataFrame(df.groupby(["kingdom"]).size()))

print(list_of_plants.sort_values(by="kingdom", ascending=False).head(10))

print("Total rows: " + str(sum(list_of_plants)))

"""