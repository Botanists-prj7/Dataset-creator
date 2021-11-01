import geopandas as gpd
import pandas as pd
from shapely.geometry import  Point
from shapely.geometry import box
from shapely import wkt

crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

plantsPd =  pd.read_csv('data\\data_with_lat_long.csv')
plantsPd['geometry'] = Point(plantsPd['decimalLongitude'], plantsPd['decimalLatitude'])
plantsGdf = gpd.GeoDataFrame(plantsPd, crs=crs_earth).set_geometry('geometry')
plantsGdf.to_crs(crs)


dkGrid = pd.read_csv('csv_files\\DK_Grid_10000.csv')
dkGrid['geometry'] = dkGrid['geometry'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(dkGrid, crs=crs).set_geometry('geometry')
gdf.to_crs(crs)


points_within = gpd.sjoin(plantsGdf, gdf, op='within')
print(points_within)