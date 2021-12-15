import csvTools
import printScoreMap

crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

data = csvTools.convert_csv_to_gdf('csv_files/DK_Full_Dataset_10000.csv',True,crs=crs)
data = data.drop(columns=['geometry'])
plant_gdf_grid = csvTools.convert_csv_to_gdf('csv_files/DK_Plant_10000.csv',True,crs=crs)
plant_gdf_grid = plant_gdf_grid.drop(columns=['geometry'])

dataNoPlants = data.drop(columns=plant_gdf_grid.columns)

printScoreMap.printRandomForestScoreMap(dataNoPlants,data['Salix caprea'])