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
#dk_grid_gdf = csvTools.convert_csv_to_gdf('csv_files\\DK_Grid_10000.csv',True,'EPSG:3857')
import csvTools

#tqdm.pandas()
nooccurences = csvTools.convert_csv_to_gdf('csv_files/DK_Plant_With_No_Occurences_5000.csv', True, crs="EPSG:3857")
occurences = csvTools.convert_csv_to_gdf('csv_files/DK_Plant_With_Occurences_5000.csv', True, crs="EPSG:3857")

def weatherfactor_to_gdf(csvfile:str, input_crs:str):
    print('Converting rain weather stations csv')
    df = pd.read_csv(csvfile)
    print('Applying geometry conversion for rain weather stations')
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['x'], df['y']), crs='EPSG:4326')
    print('Converting rain weather data projection')
    crs = gdf.to_crs(input_crs)
    print('Setting geometry for rain weather stations')
    gdf.set_geometry('geometry')
    return gdf


rain_gdf = weatherfactor_to_gdf('csv_files/DK_ClimateRain.csv', "EPSG:3857")
sun_gdf = weatherfactor_to_gdf('csv_files/DK_ClimateSun.csv', "EPSG:3857")
wind_gdf = weatherfactor_to_gdf('csv_files/DK_ClimateWind.csv', "EPSG:3857")
mintemp_gdf = weatherfactor_to_gdf('csv_files/DK_ClimateMinTemp.csv', "EPSG:3857")
maxtemp_gdf = weatherfactor_to_gdf('csv_files/DK_ClimateMaxTemp.csv', "EPSG:3857")



#Rain
print('Find nearest weather station...')
nearestjoin_occurences_rain = gpd.sjoin_nearest(occurences, rain_gdf)
print('Find nearest weather station...')
nearestjoin_nooccurences_rain = gpd.sjoin_nearest(nooccurences, rain_gdf)

#Sun
print('Find nearest weather station...')
nearestjoin_occurences_sun = gpd.sjoin_nearest(occurences, sun_gdf)
print('Find nearest weather station...')
nearestjoin_nooccurences_sun = gpd.sjoin_nearest(nooccurences, sun_gdf)

#Wind
print('Find nearest weather station...')
nearestjoin_occurences_wind = gpd.sjoin_nearest(occurences, wind_gdf)
print('Find nearest weather station...')
nearestjoin_nooccurences_wind = gpd.sjoin_nearest(nooccurences, wind_gdf)

#mintemp
print('Find nearest weather station...')
nearestjoin_occurences_mintemp = gpd.sjoin_nearest(occurences, mintemp_gdf)
print('Find nearest weather station...')
nearestjoin_nooccurences_mintemp = gpd.sjoin_nearest(nooccurences, mintemp_gdf)

#maxtemp
print('Find nearest weather station...')
nearestjoin_occurences_maxtemp = gpd.sjoin_nearest(occurences, maxtemp_gdf)
print('Find nearest weather station...')
nearestjoin_nooccurences_maxtemp = gpd.sjoin_nearest(nooccurences, maxtemp_gdf)

Plantscolumns = pd.read_csv('csv_files/DK_Plant_5000.csv')
Plantscolumns = Plantscolumns.drop(['geometry'], axis=1)

nearestjoin_occurences_rain.drop(columns=Plantscolumns.columns, inplace=True)
nearestjoin_nooccurences_rain.drop(columns=Plantscolumns.columns, inplace=True)

nearestjoin_nooccurences_maxtemp.drop(columns=Plantscolumns.columns, inplace=True)
nearestjoin_occurences_maxtemp.drop(columns=Plantscolumns.columns, inplace=True)

nearestjoin_nooccurences_mintemp.drop(columns=Plantscolumns.columns, inplace=True)
nearestjoin_occurences_mintemp.drop(columns=Plantscolumns.columns, inplace=True)

nearestjoin_nooccurences_wind.drop(columns=Plantscolumns.columns, inplace=True)
nearestjoin_occurences_wind.drop(columns=Plantscolumns.columns, inplace=True)

nearestjoin_nooccurences_sun.drop(columns=Plantscolumns.columns, inplace=True)
nearestjoin_occurences_sun.drop(columns=Plantscolumns.columns, inplace=True)

def mergefiles(a, b):
    out = pd.merge(a, b,
    on = 'geometry',
    how = 'inner')
    print("Done xd")
    return gpd.GeoDataFrame(out)

mergedminmax_nooccurences = mergefiles(nearestjoin_nooccurences_mintemp, nearestjoin_nooccurences_maxtemp)
mergedrainsun_nooccurence = mergefiles(nearestjoin_nooccurences_rain, nearestjoin_nooccurences_sun)
mergedfiles_semi_nooccurences = mergefiles(mergedminmax_nooccurences, mergedrainsun_nooccurence)
mergedfiles_final_nooccurences = mergefiles(mergedfiles_semi_nooccurences, nearestjoin_nooccurences_wind)

gpd.GeoDataFrame(mergedfiles_final_nooccurences).to_csv('csv_files/weatherstation_joined_nooccurences.csv')


mergedminmax_occurences = mergefiles(nearestjoin_occurences_mintemp, nearestjoin_occurences_maxtemp)
mergedrainsun_occurence = mergefiles(nearestjoin_occurences_rain, nearestjoin_occurences_sun)
mergedfiles_semi_occurences = mergefiles(mergedminmax_occurences, mergedrainsun_occurence)

mergedfiles_final_occurences = mergefiles(mergedfiles_semi_occurences, nearestjoin_occurences_wind)
gpd.GeoDataFrame(mergedfiles_final_occurences).to_csv('csv_files/weatherstation_joined_with_occurences.csv')



#Get soiltype and input them as columns
print(mergedfiles_final_nooccurences.columns.tolist())
print(mergedfiles_final_occurences.columns.tolist())
soil = pd.read_csv('csv_files/DK_Soiltypes_5000.csv')

mergedfiles_final_nooccurences = pd.read_csv('csv_files/weatherstation_joined_nooccurences.csv')
mergedfiles_final_occurences = pd.read_csv('csv_files/weatherstation_joined_with_occurences.csv')

soil_and_weather_nooccurences = pd.merge(mergedfiles_final_nooccurences, soil)
soil_and_weather_nooccurences = pd.get_dummies(soil_and_weather_nooccurences, columns=['soiltype'], prefix='soiltype')

#Merge the geodata with the plants csv
grids = pd.read_csv('csv_files/DK_Plant_5000.csv', error_bad_lines=False, engine='python')
soil_and_weather_nooccurences_gridded = pd.merge(soil_and_weather_nooccurences, grids)
gpd.GeoDataFrame(soil_and_weather_nooccurences_gridded).to_csv('csv_files/new_dataset_no_occurences.csv')

soil2 = pd.read_csv('csv_files/DK_Soiltypes_5000.csv')

#Same for data with occurences
soil_and_weather_occurences = pd.merge(mergedfiles_final_occurences, soil2)
soil_and_weather_occurences = pd.get_dummies(soil_and_weather_occurences, columns=['soiltype'])

grids2 = pd.read_csv('csv_files/DK_Plant_5000.csv', error_bad_lines=False, engine='python')
soil_and_weather_occurences_gridded = pd.merge(soil_and_weather_occurences, grids2)
gpd.GeoDataFrame(soil_and_weather_occurences_gridded).to_csv('csv_files/new_dataset_with_occurences.csv')

