import csvTools
import gridmaker
import matplotlib.pyplot as plt
import pandas as pd

def ColumnOfDataframeAsPercantageOfSum(column : str):
    return 'ole'

crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

DK_Soiltypes_Grid10k = csvTools.convert_csv_to_gdf('csv_files\\DK_Soiltypes_10000.csv',True,crs)
DK_Soiltypes_Grid5k = csvTools.convert_csv_to_gdf('csv_files\\DK_Soiltypes_5000.csv',True,crs)
DK_Soiltypes_SHP = gridmaker.convert_shp_to_gdf_using_crs('data\\Jordart_200000_Shape\\jordart_200000.shp',crs)


DK_Soiltypes_SHP_Total_Area_by_soiltype = DK_Soiltypes_SHP.groupby('TSYM').sum()
DK_Total_Area_km2 = DK_Soiltypes_SHP_Total_Area_by_soiltype['Area_km2'].sum()
DK_Grid5k_rows_cell_count = len(DK_Soiltypes_Grid5k.index)
DK_Grid10k_rows_cell_count = len(DK_Soiltypes_Grid10k.index)

#fig, axes = plt.subplots(nrows=1, ncols=3)
DK_Grid10k_Grids_By_Soiltype = DK_Soiltypes_Grid10k['soiltype'].value_counts().sort_values()
DK_Grid5k_Grids_By_Soiltype = DK_Soiltypes_Grid5k['soiltype'].value_counts().sort_values()
DK_shp_area_km2_By_Soiltype = DK_Soiltypes_SHP_Total_Area_by_soiltype['Area_km2'].sort_values()

DK_Grid10k_Grids_By_Soiltype_Percentage = (DK_Grid10k_Grids_By_Soiltype/DK_Grid10k_rows_cell_count)*100
DK_Grid5k_Grids_By_Soiltype_Percentage = (DK_Grid5k_Grids_By_Soiltype/DK_Grid5k_rows_cell_count)*100
DK_shp_area_km2_By_Soiltype_Percentage = (DK_shp_area_km2_By_Soiltype/DK_Total_Area_km2)*100

DK_Grid10k_Grids_By_Soiltype_Percentage.name = '10 km grid'
DK_Grid5k_Grids_By_Soiltype_Percentage.name = '5 km grid'
DK_shp_area_km2_By_Soiltype_Percentage.name = 'GEUS Shapefile'

#DK_Grid10k_Grids_By_Soiltype_Percentage.plot(kind="bar", grid=True)
#DK_Grid5k_Grids_By_Soiltype_Percentage.plot(kind="bar", grid=True)
#DK_shp_area_km2_By_Soiltype_Percentage.plot(kind="bar", grid=True)

concatinatedSeries = pd.concat([DK_Grid10k_Grids_By_Soiltype_Percentage,DK_Grid5k_Grids_By_Soiltype_Percentage,DK_shp_area_km2_By_Soiltype_Percentage], axis=1).sort_values('GEUS Shapefile')

print(concatinatedSeries)

concatinatedSeries.plot(kind='bar', xlabel='Soiltype', ylabel='Percentage of total area')
plt.show()

concatinatedSeries.dropna(inplace=True)

concatinatedSeries.plot(kind='bar', xlabel='Soiltype', ylabel='Percentage of total area')
plt.show()