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
#from tqdm import tqdm, tqdm_notebook
import time
import csvTools
from progress.bar import Bar
import gridmaker

#dk_grid_gdf = csvTools.convert_csv_to_gdf('csv_files\\DK_Grid_10000.csv',True,'EPSG:3857')

"""
#tqdm.pandas()
print('Reading Grid CSV')
df = pd.read_csv('csv_files/DK_Grid_10000.csv')
print('Setting WKT...')
df['geometry'] = df['geometry'].apply(wkt.loads)#.progress_apply(lambda x: x)
print('Converting projection')
soil = gpd.GeoDataFrame(df, crs='EPSG:3857')#.progress_apply(lambda x: x)
print('Converting projection...')
soil = soil.to_crs('EPSG:3857')#.progress_apply(lambda x: x)
#print(df)


print('Converting plants csv')
df2 = pd.read_csv('data/data_with_lat_long.csv')
newdf = df2
print('Applying geometry conversion for plants')
gdf = gpd.GeoDataFrame(newdf, geometry=gpd.points_from_xy(df2['decimalLongitude'], df2['decimalLatitude']), crs='EPSG:4326')
print('Converting plants data projection')
gdf = gdf.to_crs('EPSG:3857')
print('Setting geometry for plants')
gdf.set_geometry('geometry')
#print(gdf.head())

print('Finding intersecting points...')
points_within = gpd.sjoin(gdf, soil, predicate='within', how='inner')
#gpd.GeoDataFrame(points_within).to_csv('csv_files/plantsoilintersection2.csv')
"""

plants_within_gdf = csvTools.convert_csv_to_gdf('csv_files/plantsoilintersection2.csv',True,'EPSG:3857')
#DK_Plant_GDF = DK_GRID
DK_Plant_gdf = csvTools.convert_csv_to_gdf('csv_files/DK_Grid_10000.csv',True,'EPSG:3857')

#points_within.drop rows where index_right is None/NA or whatever NULL value
plants_within_gdf = plants_within_gdf.dropna()
plants_within_gdf = plants_within_gdf.drop(columns=['decimalLongitude','decimalLatitude','geometry'])

bar = Bar('Finding soiltype of all gridcells', max=len(plants_within_gdf.index))
for index,row in plants_within_gdf.iterrows():
    #Check om kolonne for planten findes i DK_Plant_GDF
    
    if not row['species'] in DK_Plant_gdf.columns:
        #Hvis ikke tilføj kollonen med navn = plantens navn og værdi False i alle række
        DK_Plant_gdf[row['species']] = False
    #find række i DK_Plant_GDF fil med index_right 
    #sæt værdi i kollonnen med plantens navn = True
    DK_Plant_gdf.loc[row['index_right'],[row['species']]] = True
    bar.next()
    #if index == 10:
        #break
bar.finish()    

print(DK_Plant_gdf.head())
#Gem oprettet geodataframe som en CSV med filnat DK_PLants_10k
gridmaker.save_gdf_to_csv_in_folder('csv_files','DK_Plant_10000.csv',DK_Plant_gdf)


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