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
""" 

#tqdm.pandas()
print('Reading Grid CSV')
df = pd.read_csv('csv_files/DK_Grid_10000.csv')
print('Setting WKT...')
df['geometry'] = df['geometry'].apply(wkt.loads)#.progress_apply(lambda x: x)
print('Converting projection')
grid = gpd.GeoDataFrame(df, crs='EPSG:3857')#.progress_apply(lambda x: x)
print('Converting projection...')
grid = grid.to_crs('EPSG:3857')#.progress_apply(lambda x: x)
#print(df)

#rain
print('Converting rain weather stations csv')
rain_df = pd.read_csv('csv_files/DK_ClimateRain.csv')
print('Applying geometry conversion for rain weather stations')
rain_gdf = gpd.GeoDataFrame(rain_df, geometry=gpd.points_from_xy(rain_df['x'], rain_df['y']), crs='EPSG:4326')
print('Converting rain weather data projection')
rain_gdf = rain_gdf.to_crs('EPSG:3857')
print('Setting geometry for rain weather stations')
rain_gdf.set_geometry('geometry')

print('Find nearest weather station...')
nearestjoinrain = gpd.sjoin_nearest(grid, rain_gdf)
#rainrefactor = nearestjoinrain.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinrain).to_csv('csv_files/rainnearestgridcell.csv')

#sun
print('Converting sun weather stations csv')
sun_df = pd.read_csv('csv_files/DK_ClimateSun.csv')
print('Applying geometry conversion for sun weather stations')
sun_gdf = gpd.GeoDataFrame(sun_df, geometry=gpd.points_from_xy(sun_df['x'], sun_df['y']), crs='EPSG:4326')
print('Converting sun weather data projection')
sun_gdf = sun_gdf.to_crs('EPSG:3857')
print('Setting geometry for sun weather stations')
sun_gdf.set_geometry('geometry')

print('Find nearest weather station...')
nearestjoinsun = gpd.sjoin_nearest(grid, sun_gdf)
#sunrefactor = nearestjoinsun.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinsun).to_csv('csv_files/sunnearestgridcell.csv')


#wind
print('Converting wind weather stations csv')
wind_df = pd.read_csv('csv_files/DK_ClimateWind.csv')
print('Applying geometry conversion for wind weather stations')
wind_gdf = gpd.GeoDataFrame(wind_df, geometry=gpd.points_from_xy(wind_df['x'], wind_df['y']), crs='EPSG:4326')
print('Converting wind weather data projection')
wind_gdf = wind_gdf.to_crs('EPSG:3857')
print('Setting geometry for wind weather stations')
wind_gdf.set_geometry('geometry')

print('Find nearest weather station...')
nearestjoinwind = gpd.sjoin_nearest(grid, wind_gdf)
#windrefactor = nearestjoinwind.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinwind).to_csv('csv_files/windnearestgridcell.csv')


#maxtemp
print('Converting max temp weather stations csv')
maxtemp_df = pd.read_csv('csv_files/DK_ClimateMaxTemp.csv')
print('Applying geometry conversion for max temp weather stations')
maxtemp_gdf = gpd.GeoDataFrame(maxtemp_df, geometry=gpd.points_from_xy(maxtemp_df['x'], maxtemp_df['y']), crs='EPSG:4326')
print('Converting max temp weather data projection')
maxtemp_gdf = maxtemp_gdf.to_crs('EPSG:3857')
print('Setting geometry for max temp weather stations')
maxtemp_gdf.set_geometry('geometry')

print('Find nearest weather station...')
maxtempnearestjoin = gpd.sjoin_nearest(grid, maxtemp_gdf)
#maxtemprefactor = maxtempnearestjoin.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
print(gpd.GeoDataFrame(maxtempnearestjoin))
gpd.GeoDataFrame(maxtempnearestjoin).to_csv('csv_files/maxtempnearestgridcell.csv')


#mintemp
print('Converting min temp weather stations csv')
mintemp_df = pd.read_csv('csv_files/DK_ClimateMinTemp.csv')
print('Applying geometry conversion for min temp weather stations')
mintemp_gdf = gpd.GeoDataFrame(mintemp_df, geometry=gpd.points_from_xy(mintemp_df['x'], mintemp_df['y']), crs='EPSG:4326')
print('Converting min temp weather data projection')
mintemp_gdf = mintemp_gdf.to_crs('EPSG:3857')
print('Setting geometry for min temp weather stations')
mintemp_gdf.set_geometry('geometry')

print('Find nearest weather station...')
mintempnearestjoin = gpd.sjoin_nearest(grid, mintemp_gdf)
#mintemprefactor = mintempnearestjoin.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
print(gpd.GeoDataFrame(mintempnearestjoin))
gpd.GeoDataFrame(mintempnearestjoin).to_csv('csv_files/mintempnearestgridcell.csv') """


mintemp = pd.read_csv('csv_files/mintempnearestgridcell.csv', error_bad_lines=False, engine='python')
maxtemp = pd.read_csv('csv_files/maxtempnearestgridcell.csv', error_bad_lines=False, engine='python')
rain = pd.read_csv('csv_files/rainnearestgridcell.csv', error_bad_lines=False, engine='python')
sun = pd.read_csv('csv_files/sunnearestgridcell.csv', error_bad_lines=False, engine='python')
wind = pd.read_csv('csv_files/windnearestgridcell.csv', error_bad_lines=False, engine='python')

mergedfiles_minmaxtemp = pd.merge(mintemp, maxtemp,
on = 'geometry',
how = 'inner')
print("Done xd")
gpd.GeoDataFrame(mergedfiles_minmaxtemp).to_csv('csv_files/mergedfiles_minmax.csv')

mergedfiles_rainsun = pd.merge(rain, sun,
on = 'geometry',
how = 'inner')
print("done xd")
gpd.GeoDataFrame(mergedfiles_rainsun).to_csv('csv_files/mergedfiles_rainsun.csv')
 
mergedfiles_minmaxtemp = pd.read_csv('csv_files/mergedfiles_minmax.csv', error_bad_lines=False, engine='python')
mergedfiles_rainsun = pd.read_csv('csv_files/mergedfiles_rainsun.csv', error_bad_lines=False, engine='python')

mergedfiles_semi = pd.merge(mergedfiles_minmaxtemp, mergedfiles_rainsun,
on = 'geometry',
how = 'inner')
print("done xd")
gpd.GeoDataFrame(mergedfiles_semi).to_csv('csv_files/mergedfiles_semi.csv')
 
mergedfiles_semi = pd.read_csv('csv_files/mergedfiles_semi.csv', error_bad_lines=False, engine='python')
mergedfiles = pd.merge(mergedfiles_semi, wind,
on = 'geometry',
how = 'inner')
print("donexd")
print(mergedfiles.head())
gpd.GeoDataFrame(mergedfiles).to_csv('csv_files/weatherstationjoin_index_final.csv')

'''

weatherstation = pd.read_csv('csv_files/weatherstationjoin_index_final.csv', error_bad_lines=False, engine='python')

weatherstationdropped = weatherstation.drop(columns=['rainApril', 'rainMay', 'rainJune'])

print(weatherstationdropped.isnull().sum())

gpd.GeoDataFrame(weatherstationdropped).to_csv('csv_files/weatherstationdroppednull.csv') 



"""


'''

weatherstationsfinal = pd.read_csv('Dataset/Dataset-creator/csv_files/finalcsv.csv')
soilfinal = pd.read_csv('Dataset/Dataset-creator/csv_files/DK_Soiltypes_10000.csv')
hallofinal = pd.merge(weatherstationsfinal, soilfinal,
on = 'geometry',
how = 'inner')
print("donexd")
hallofinal = pd.get_dummies(hallofinal, columns=['soiltype'], prefix='soiltype')
print(hallofinal.head())
gpd.GeoDataFrame(hallofinal).to_csv('Dataset/Dataset-creator/csv_files/hallofinalcsv.csv')



""" weatherstations = pd.read_csv('csv_files/weatherstationdroppednull.csv')
#print(weatherstations.head())
print(weatherstations.columns.tolist())

#alle kolonner, der ikke er behov for, kasseres 
weatherstationsrefactor = weatherstations.drop(columns=['Unnamed: 0','Unnamed: 0_x','Unnamed: 0_x.1','Unnamed: 0_x_x','index_right_x_x','Unnamed: 0.1_x_x','stationId_x_x','x_x_x','y_x_x','Unnamed: 0_y_x','index_right_y_x','Unnamed: 0.1_y_x','stationId_y_x','x_y_x','y_y_x','Unnamed: 0_y','Unnamed: 0_x_y', 'index_right_x_y','Unnamed: 0.1_x_y','stationId_x_y','x_x_y','y_x_y','index_right_y_y','Unnamed: 0.1_y_y','stationId_y_y','x_y_y','y_y_y','Unnamed: 0_y.1','index_right','Unnamed: 0.1','stationId','x','y'])
print(weatherstationsrefactor.head())
gpd.GeoDataFrame(weatherstationsrefactor).to_csv('csv_files/weatherstationrefactor_geometry.csv') 

weatherstation = pd.read_csv('csv_files/weatherstationrefactor_geometry.csv', error_bad_lines=False, engine='python')
grids = pd.read_csv('csv_files/DK_Plant_10000.csv', error_bad_lines=False, engine='python')

weatherstation_grid = pd.merge(weatherstation, grids, 
on = 'geometry',
how = 'inner')

gpd.GeoDataFrame(weatherstation_grid).to_csv('csv_files/weatherstationgridjoin_final.csv')
"""


weatherstationsgrid = pd.read_csv('csv_files/weatherstationgridjoin_final.csv')

"""



#check om vejrstation er i grid 
plants_within_gdf = csvTools.convert_csv_to_gdf('csv_files/plantsoilintersection2.csv',True,'EPSG:3857')
#DK_Plant_GDF = DK_GRID
DK_Plant_gdf = csvTools.convert_csv_to_gdf('csv_files/DK_Grid_10000.csv',True,'EPSG:3857')

#nearestjoin.drop rows where index_right is None/NA or whatever NULL value
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