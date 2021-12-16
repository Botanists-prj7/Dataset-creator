from matplotlib import style
from matplotlib.pyplot import colormaps
import gridmaker
import csvTools
import geopandas

crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

soiltypeColumnName = 'soiltype'
centerColumnName = 'center'

DK_Soiltypes_Grid = csvTools.convert_csv_to_gdf('csv_files\\DK_Soiltypes_10000.csv',True,crs)
DK_Soiltypes_SHP = gridmaker.convert_shp_to_gdf_using_crs('data\\Jordart_200000_Shape\\jordart_200000.shp',crs)
        
#merged = geopandas.overlay(DK_Soiltypes_Grid, DK_Soiltypes_SHP, how='intersection')
#print(merged)
#merged.plot(column='TSYM')

fig, axes = gridmaker.plt.subplots(nrows=1, ncols=2)
DK_Soiltypes_Grid.sort_values('soiltype', ascending=True, inplace=True, kind='heapsort')
DK_Soiltypes_Grid.plot(column = soiltypeColumnName, legend=True, ax=axes[0],cmap="tab20") 

DK_Soiltypes_Grid.drop_duplicates(subset='soiltype',inplace=True)
print(DK_Soiltypes_Grid.head)
DK_Soiltypes_SHP = gridmaker.sortingFunction(DK_Soiltypes_SHP, DK_Soiltypes_Grid, 'TSYM', 'soiltype', 'TSYM')
DK_Soiltypes_SHP.plot(column = 'TSYM', legend=True, ax=axes[1], cmap="tab20") 

gridmaker.plt.show()