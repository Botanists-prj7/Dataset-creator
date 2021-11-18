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
withnooccurences = pd.read_csv('csv_files\\DK_Plant_With_No_Occurences_10000.csv')
print('Setting WKT...')
withnooccurences['geometry'] = withnooccurences['geometry'].apply(wkt.loads)#.progress_apply(lambda x: x)
print('Converting projection')

withno_occurences_grid = gpd.GeoDataFrame(withnooccurences, crs='EPSG:3857')#.progress_apply(lambda x: x)
print('Converting projection...')
withno_occurences_grid = withno_occurences_grid.to_crs('EPSG:3857')#.progress_apply(lambda x: x)
#print(df)

print('Reading Grid CSV')
withoccurences = pd.read_csv('csv_files\\DK_Plant_With_Occurences_10000.csv')
print('Setting WKT...')
withoccurences['geometry'] = withoccurences['geometry'].apply(wkt.loads)#.progress_apply(lambda x: x)
print('Converting projection')
with_occurences_grid = gpd.GeoDataFrame(withoccurences, crs='EPSG:3857')#.progress_apply(lambda x: x)
print('Converting projection...')
with_occurences_grid = with_occurences_grid.to_crs('EPSG:3857')#.progress_apply(lambda x: x)
#print(df)


#rain
print('Converting rain weather stations csv')
rain_df = pd.read_csv('csv_files\\DK_ClimateRain.csv')
print('Applying geometry conversion for rain weather stations')
rain_gdf = gpd.GeoDataFrame(rain_df, geometry=gpd.points_from_xy(rain_df['x'], rain_df['y']), crs='EPSG:4326')
print('Converting rain weather data projection')
rain_gdf = rain_gdf.to_crs('EPSG:3857')
print('Setting geometry for rain weather stations')
rain_gdf.set_geometry('geometry')

print('Find nearest weather station...')
nearestjoinrain_occurences = gpd.sjoin_nearest(with_occurences_grid, rain_gdf)
#rainrefactor = nearestjoinrain.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinrain_occurences).to_csv('csv_files\\rain_nearest_gridcell_occurences.csv')
print('Find nearest weather station...')
nearestjoinrain_nooccurences = gpd.sjoin_nearest(withno_occurences_grid, rain_gdf)
#rainrefactor = nearestjoinrain.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinrain_nooccurences).to_csv('csv_files\\rain_nearest_gridcell_no_occurences.csv')



#sun
print('Converting sun weather stations csv')
sun_df = pd.read_csv('csv_files\\DK_ClimateSun.csv')
print('Applying geometry conversion for sun weather stations')
sun_gdf = gpd.GeoDataFrame(sun_df, geometry=gpd.points_from_xy(sun_df['x'], sun_df['y']), crs='EPSG:4326')
print('Converting sun weather data projection')
sun_gdf = sun_gdf.to_crs('EPSG:3857')
print('Setting geometry for sun weather stations')
sun_gdf.set_geometry('geometry')

print('Find nearest weather station...')
nearestjoinsun_occurence = gpd.sjoin_nearest(with_occurences_grid, sun_gdf)
#sunrefactor = nearestjoinsun.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinsun_occurence).to_csv('csv_files\\sun_nearest_gridcell_occurences.csv')
print('Find nearest weather station...')
nearestjoinsun_nooccurence = gpd.sjoin_nearest(withno_occurences_grid, sun_gdf)
#sunrefactor = nearestjoinsun.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinsun_nooccurence).to_csv('csv_files\\sun_nearest_gridcell_no_occurences.csv')


#wind
print('Converting wind weather stations csv')
wind_df = pd.read_csv('csv_files\\DK_ClimateWind.csv')
print('Applying geometry conversion for wind weather stations')
wind_gdf = gpd.GeoDataFrame(wind_df, geometry=gpd.points_from_xy(wind_df['x'], wind_df['y']), crs='EPSG:4326')
print('Converting wind weather data projection')
wind_gdf = wind_gdf.to_crs('EPSG:3857')
print('Setting geometry for wind weather stations')
wind_gdf.set_geometry('geometry')

print('Find nearest weather station...')
nearestjoinwind_occurences = gpd.sjoin_nearest(with_occurences_grid, wind_gdf)
#windrefactor = nearestjoinwind.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinwind_occurences).to_csv('csv_files\\wind_nearest_gridcell_occurences.csv')
print('Find nearest weather station...')
nearestjoinwind_nooccurences = gpd.sjoin_nearest(withno_occurences_grid, wind_gdf)
#windrefactor = nearestjoinwind.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
#print(gpd.GeoDataFrame(nearestjoin))
gpd.GeoDataFrame(nearestjoinwind_nooccurences).to_csv('csv_files\\wind_nearest_gridcell_no_occurences.csv')


#maxtemp
print('Converting max temp weather stations csv')
maxtemp_df = pd.read_csv('csv_files\\DK_ClimateMaxTemp.csv')
print('Applying geometry conversion for max temp weather stations')
maxtemp_gdf = gpd.GeoDataFrame(maxtemp_df, geometry=gpd.points_from_xy(maxtemp_df['x'], maxtemp_df['y']), crs='EPSG:4326')
print('Converting max temp weather data projection')
maxtemp_gdf = maxtemp_gdf.to_crs('EPSG:3857')
print('Setting geometry for max temp weather stations')
maxtemp_gdf.set_geometry('geometry')

print('Find nearest weather station...')
maxtempnearestjoin_occurences = gpd.sjoin_nearest(with_occurences_grid, maxtemp_gdf)
#maxtemprefactor = maxtempnearestjoin.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
print(gpd.GeoDataFrame(maxtempnearestjoin_occurences))
gpd.GeoDataFrame(maxtempnearestjoin_occurences).to_csv('csv_files\\maxtemp_nearest_gridcell_occurences.csv')

print('Find nearest weather station...')
maxtempnearestjoin_nooccurences = gpd.sjoin_nearest(withno_occurences_grid, maxtemp_gdf)
#maxtemprefactor = maxtempnearestjoin.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
print(gpd.GeoDataFrame(maxtempnearestjoin_nooccurences))
gpd.GeoDataFrame(maxtempnearestjoin_nooccurences).to_csv('csv_files\\maxtemp_nearest_gridcell_no_occurences.csv')

#mintemp
print('Converting min temp weather stations csv')
mintemp_df = pd.read_csv('csv_files\\DK_ClimateMinTemp.csv')
print('Applying geometry conversion for min temp weather stations')
mintemp_gdf = gpd.GeoDataFrame(mintemp_df, geometry=gpd.points_from_xy(mintemp_df['x'], mintemp_df['y']), crs='EPSG:4326')
print('Converting min temp weather data projection')
mintemp_gdf = mintemp_gdf.to_crs('EPSG:3857')
print('Setting geometry for min temp weather stations')
mintemp_gdf.set_geometry('geometry')

print('Find nearest weather station...')
mintempnearestjoin_occurences = gpd.sjoin_nearest(with_occurences_grid, mintemp_gdf)
#mintemprefactor = mintempnearestjoin.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
print(gpd.GeoDataFrame(mintempnearestjoin_occurences))
gpd.GeoDataFrame(mintempnearestjoin_occurences).to_csv('csv_files\\mintemp_nearest_gridcell_occurences.csv') 

print('Find nearest weather station...')
mintempnearestjoin_nooccurences = gpd.sjoin_nearest(withno_occurences_grid, mintemp_gdf)
#mintemprefactor = mintempnearestjoin.drop(columns=['geometry', 'Unnamed: 0', 'x', 'y', 'stationId'])
print(gpd.GeoDataFrame(mintempnearestjoin_nooccurences))
gpd.GeoDataFrame(mintempnearestjoin_nooccurences).to_csv('csv_files\\mintemp_nearest_gridcell_no_occurences.csv') 



Plantscolumns = pd.read_csv('csv_files\DK_Plant_10000.csv')
Plantscolumns = Plantscolumns.drop(['geometry'], axis=1)

mintemp_no_occurences = pd.read_csv('csv_files\\mintemp_nearest_gridcell_no_occurences.csv', error_bad_lines=False, engine='python')
mintemp_no_occurences.drop(columns=Plantscolumns.columns, inplace=True)
maxtemp_no_occurences = pd.read_csv('csv_files\\maxtemp_nearest_gridcell_no_occurences.csv', error_bad_lines=False, engine='python')
maxtemp_no_occurences.drop(columns=Plantscolumns.columns, inplace=True)
rain_no_occurences = pd.read_csv('csv_files\\rain_nearest_gridcell_no_occurences.csv', error_bad_lines=False, engine='python')
rain_no_occurences.drop(columns=Plantscolumns.columns, inplace=True)
sun_no_occurences = pd.read_csv('csv_files\\sun_nearest_gridcell_no_occurences.csv', error_bad_lines=False, engine='python')
sun_no_occurences.drop(columns=Plantscolumns.columns, inplace=True)
wind_no_occurences = pd.read_csv('csv_files\\wind_nearest_gridcell_no_occurences.csv', error_bad_lines=False, engine='python')
wind_no_occurences.drop(columns=Plantscolumns.columns, inplace=True)

mintemp_occurences = pd.read_csv('csv_files\\mintemp_nearest_gridcell_occurences.csv', error_bad_lines=False, engine='python')
mintemp_occurences.drop(columns=Plantscolumns.columns, inplace=True)
maxtemp_occurences = pd.read_csv('csv_files\\mintemp_nearest_gridcell_occurences.csv', error_bad_lines=False, engine='python')
maxtemp_occurences.drop(columns=Plantscolumns.columns, inplace=True)
rain_occurences = pd.read_csv('csv_files\\mintemp_nearest_gridcell_occurences.csv', error_bad_lines=False, engine='python')
rain_occurences.drop(columns=Plantscolumns.columns, inplace=True)
sun_occurences = pd.read_csv('csv_files\\mintemp_nearest_gridcell_occurences.csv', error_bad_lines=False, engine='python')
sun_occurences.drop(columns=Plantscolumns.columns, inplace=True)
wind_occurences = pd.read_csv('csv_files\\mintemp_nearest_gridcell_occurences.csv', error_bad_lines=False, engine='python')
wind_occurences.drop(columns=Plantscolumns.columns, inplace=True)

mergedfiles_minmaxtemp_nooccurences = pd.merge(mintemp_no_occurences, maxtemp_no_occurences,
on = 'geometry',
how = 'inner')
print("Done xd")
gpd.GeoDataFrame(mergedfiles_minmaxtemp_nooccurences).to_csv('csv_files\\mergedfiles_minmax_nooccurences.csv')

mergedfiles_rainsun_nooccurences = pd.merge(rain_no_occurences, sun_no_occurences,
on = 'geometry',
how = 'inner')
print("done xd")
gpd.GeoDataFrame(mergedfiles_rainsun_nooccurences).to_csv('csv_files\\mergedfiles_rainsun_nooccurences.csv')
 
mergedfiles_minmaxtemp_nooccurences = pd.read_csv('csv_files\\mergedfiles_minmax_nooccurences.csv', error_bad_lines=False, engine='python')
mergedfiles_rainsun_nooccurences = pd.read_csv('csv_files\\mergedfiles_rainsun_nooccurences.csv', error_bad_lines=False, engine='python')

mergedfiles_semi_nooccurences = pd.merge(mergedfiles_minmaxtemp_nooccurences, mergedfiles_rainsun_nooccurences,
on = 'geometry',
how = 'inner')
print("done xd")
gpd.GeoDataFrame(mergedfiles_semi_nooccurences).to_csv('csv_files\\mergedfiles_semi_nooccurences.csv')
 
mergedfiles_semi = pd.read_csv('csv_files\\mergedfiles_semi_nooccurences.csv', error_bad_lines=False, engine='python')
mergedfiles = pd.merge(mergedfiles_semi_nooccurences, wind_no_occurences,
on = 'geometry',
how = 'inner')
print("donexd")
print(mergedfiles.head())
gpd.GeoDataFrame(mergedfiles).to_csv('csv_files\\weatherstationjoin_index_final_nooccurences.csv')

######################################################
mergedfiles_minmaxtemp_occurences = pd.merge(mintemp_occurences, maxtemp_occurences,
on = 'geometry',
how = 'inner')
print("Done")
gpd.GeoDataFrame(mergedfiles_minmaxtemp_occurences).to_csv('csv_files\\mergedfiles_minmax_occurences.csv')

mergedfiles_rainsun_occurences = pd.merge(rain_occurences, sun_occurences,
on = 'geometry',
how = 'inner')
print("done")
gpd.GeoDataFrame(mergedfiles_rainsun_occurences).to_csv('csv_files\\mergedfiles_rainsun_occurences.csv')
 
mergedfiles_minmaxtemp_occurences = pd.read_csv('csv_files\\mergedfiles_minmax_occurences.csv', error_bad_lines=False, engine='python')
mergedfiles_rainsun_occurences = pd.read_csv('csv_files\\mergedfiles_rainsun_occurences.csv', error_bad_lines=False, engine='python')

mergedfiles_semi_occurences = pd.merge(mergedfiles_minmaxtemp_occurences, mergedfiles_rainsun_occurences,
on = 'geometry',
how = 'inner')
print("done")
gpd.GeoDataFrame(mergedfiles_semi_occurences).to_csv('csv_files\\mergedfiles_semi_occurences.csv')
 
mergedfiles_semi_occurences = pd.read_csv('csv_files\\mergedfiles_semi_occurences.csv', error_bad_lines=False, engine='python')
mergedfiles_occurrences = pd.merge(mergedfiles_semi_occurences, wind_occurences,
on = 'geometry',
how = 'inner')
print("done")
print(mergedfiles_occurrences.head())
gpd.GeoDataFrame(mergedfiles_occurrences).to_csv('csv_files\\weatherstationjoin_index_final_occurences.csv')
 """
"""

"""
""" 
weatherstationdropped = weatherstation.drop(columns=['rainApril', 'rainMay', 'rainJune'])

print(weatherstationdropped.isnull().sum())

gpd.GeoDataFrame(weatherstationdropped).to_csv('csv_files/weatherstationdroppednull.csv') 
 """


"""

weatherstationsfinal = pd.read_csv('Dataset/Dataset-creator/csv_files/finalcsv.csv')
soilfinal = pd.read_csv('Dataset/Dataset-creator/csv_files/DK_Soiltypes_10000.csv')
hallofinal = pd.merge(weatherstationsfinal, soilfinal,
on = 'geometry',
how = 'inner')
print("donexd")
hallofinal = pd.get_dummies(hallofinal, columns=['soiltype'], prefix='soiltype')
print(hallofinal.head())
gpd.GeoDataFrame(hallofinal).to_csv('Dataset/Dataset-creator/csv_files/hallofinalcsv.csv')
"""


weatherstations_nooccurences = pd.read_csv('csv_files\\weatherstationjoin_index_final_nooccurences.csv')

not_needed_columns = ['Unnamed: 0', 'Unnamed: 0_x', 'Unnamed: 0_x_x', 'index_right_x_x', 'Unnamed: 0.1_x_x', 'stationId_x_x', 'x_x_x', 'y_x_x', 'Unnamed: 0_y_x', 'index_right_y_x', 'Unnamed: 0.1_y_x', 'stationId_y_x', 'x_y_x', 'y_y_x','Unnamed: 0_y', 'Unnamed: 0_x_y', 'index_right_x_y', 'Unnamed: 0.1_x_y', 'stationId_x_y', 'x_x_y', 'y_x_y', 'Unnamed: 0_y_y', 'index_right_y_y', 'Unnamed: 0.1_y_y', 'stationId_y_y', 'x_y_y', 'y_y_y','Unnamed: 0.1', 'index_right', 'Unnamed: 0.1.1', 'stationId', 'x', 'y']

weatherstations_nooccurences.drop(columns=not_needed_columns, inplace=True)

weatherstations_occurences = pd.read_csv('csv_files\\weatherstationjoin_index_final_occurences.csv')

not_needed_columns2 = ['Unnamed: 0', 'Unnamed: 0_x', 'Unnamed: 0_x.1', 'Unnamed: 0_x_x', 'index_right_x_x', 'Unnamed: 0.1_x_x', 'stationId_x_x', 'x_x_x', 'y_x_x', 'minTempJanuary_x_x', 'minTempFebruary_x_x', 'minTempMarch_x_x', 'minTempApril_x_x', 'minTempMay_x_x', 'minTempJune_x_x', 'minTempJuly_x_x', 'minTempAugust_x_x', 'minTempSeptember_x_x', 'minTempOctober_x_x', 'minTempNovember_x_x', 'minTempDecember_x_x', 'Unnamed: 0_y_x', 'index_right_y_x', 'Unnamed: 0.1_y_x', 'stationId_y_x', 'x_y_x', 'y_y_x', 'minTempJanuary_y_x', 'minTempFebruary_y_x', 'minTempMarch_y_x', 'minTempApril_y_x', 'minTempMay_y_x', 'minTempJune_y_x', 'minTempJuly_y_x', 'minTempAugust_y_x', 'minTempSeptember_y_x', 'minTempOctober_y_x', 'minTempNovember_y_x', 'minTempDecember_y_x', 'Unnamed: 0_y', 'Unnamed: 0_x_y', 'index_right_x_y', 'Unnamed: 0.1_x_y', 'stationId_x_y', 'x_x_y', 'y_x_y', 'minTempJanuary_x_y', 'minTempFebruary_x_y', 'minTempMarch_x_y', 'minTempApril_x_y', 'minTempMay_x_y', 'minTempJune_x_y', 'minTempJuly_x_y', 'minTempAugust_x_y', 'minTempSeptember_x_y', 'minTempOctober_x_y', 'minTempNovember_x_y', 'minTempDecember_x_y', 'Unnamed: 0_y_y', 'index_right_y_y', 'Unnamed: 0.1_y_y', 'stationId_y_y', 'x_y_y', 'y_y_y', 'minTempJanuary_y_y', 'minTempFebruary_y_y', 'minTempMarch_y_y', 'minTempApril_y_y', 'minTempMay_y_y', 'minTempJune_y_y', 'minTempJuly_y_y', 'minTempAugust_y_y','minTempSeptember_y_y', 'minTempOctober_y_y', 'minTempNovember_y_y', 'minTempDecember_y_y', 'Unnamed: 0_y.1', 'index_right', 'Unnamed: 0.1', 'stationId', 'x', 'y']

weatherstations_occurences.drop(columns=not_needed_columns2, inplace=True)

print(weatherstations_occurences.columns.tolist())

#print(weatherstations.head())
#print(weatherstations.columns.tolist())

#alle kolonner, der ikke er behov for, kasseres 
grids = pd.read_csv('csv_files\\DK_Plant_10000.csv', error_bad_lines=False, engine='python')

weatherstation_grid_nooccurences = pd.merge(weatherstations_nooccurences, grids, 
on = 'geometry',
how = 'inner')

gpd.GeoDataFrame(weatherstation_grid_nooccurences).to_csv('csv_files\\weatherstationgridjoin_final_nooccurences.csv')

grids = pd.read_csv('csv_files\\DK_Plant_10000.csv', error_bad_lines=False, engine='python')

weatherstation_grid_occurences = pd.merge(weatherstations_occurences, grids, 
on = 'geometry',
how = 'inner')

gpd.GeoDataFrame(weatherstation_grid_occurences).to_csv('csv_files\\weatherstationgridjoin_final_occurences.csv')


weatherstationsfinal_occurences = pd.read_csv('csv_files\\weatherstationgridjoin_final_occurences.csv')
soilfinal_occur = pd.read_csv('csv_files\\DK_Soiltypes_10000.csv')
final_occur = pd.merge(weatherstationsfinal_occurences, soilfinal_occur,
on = 'geometry',
how = 'inner')
print("donexd")
final_occur = pd.get_dummies(final_occur, columns=['soiltype'], prefix='soiltype')
print(final_occur.head())
final_occur.drop(columns='Unnamed: 0', inplace=True)
gpd.GeoDataFrame(final_occur).to_csv('csv_files\\completedataset_DK_with_occurences_10K.csv')

weatherstationsfinal_nooccurences = pd.read_csv('csv_files\\weatherstationgridjoin_final_nooccurences.csv')
soilfinal_nooccur = pd.read_csv('csv_files\\DK_Soiltypes_10000.csv')
final_nooccur = pd.merge(weatherstationsfinal_nooccurences, soilfinal_nooccur,
on = 'geometry',
how = 'inner')
print("donexd")
final_nooccur = pd.get_dummies(final_nooccur, columns=['soiltype'], prefix='soiltype')
print(final_nooccur.head())
final_nooccur.drop(columns='Unnamed: 0', inplace=True)
gpd.GeoDataFrame(final_nooccur).to_csv('csv_files\\completedataset_DK_no_occurences_10K.csv')
"""


#weatherstationsgrid = pd.read_csv('csv_files/weatherstationgridjoin_final.csv')





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