import gridmaker
import csvTools
from geopandas import geodataframe as gdf
from pandas import Index

crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

updateCsvFiles = True

dk_plants_gdf = csvTools.convert_csv_to_gdf('csv_files/DK_Plant_5000.csv',True,crs)

dk_plants_gdf_without_geometry_column = dk_plants_gdf.drop(columns=['geometry'])
series_defining_grids_with_observations =  dk_plants_gdf_without_geometry_column.eq(False,axis='index').all(1)

index_of_grids_with_no_occurences = series_defining_grids_with_observations[series_defining_grids_with_observations == True]
index_of_grids_with_occurences = series_defining_grids_with_observations[series_defining_grids_with_observations == False]

if updateCsvFiles:
    csvTools.save_gdf_to_csv_in_folder('csv_files','DK_Plant_With_No_Occurences_5000.csv',dk_plants_gdf.iloc[index_of_grids_with_no_occurences.index])
    csvTools.save_gdf_to_csv_in_folder('csv_files','DK_Plant_With_Occurences_5000.csv',dk_plants_gdf.iloc[index_of_grids_with_occurences.index])