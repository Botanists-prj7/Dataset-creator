import geopandas as gpd
from geopandas import geodataframe
import pandas 
from matplotlib import pyplot as plt
import shapely
from progress.bar import Bar
import os
from pathlib import Path
import numpy as np
from shapely import geometry
import random
import time

from shapely.geometry.polygon import Polygon

#functions:
def save_gdf_to_csv_in_folder(foldername: str,filename: str, gdf: gpd.GeoDataFrame):
    Path(foldername).mkdir(parents=True, exist_ok=True)
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, foldername, filename)
    gdf.to_csv(file_path, index=False)

def convert_gdf_to_gdfgrid(gdf: gpd.GeoDataFrame,distance_pr_cell_in_m: int, crs: str):
    xmin, ymin, xmax, ymax = gdf.total_bounds
    grid_cells = []
    x = xmin
    while x < xmax:
        y = ymin
        while y < ymax:
            grid_cells.append(geometry.box(x, y, x+distance_pr_cell_in_m, y+distance_pr_cell_in_m))
            y += distance_pr_cell_in_m
        x += distance_pr_cell_in_m
    return gpd.GeoDataFrame(grid_cells, columns=['geometry'], crs=crs)    

def convert_shp_to_gdf_using_crs(shp: str, crs: str):
    geodataframe = gpd.read_file(shp)
    return geodataframe.to_crs(crs)

def first_row_of_gdf_containing_point(gdf: gpd.GeoDataFrame, point: geometry.Point):
    polygons_containing_point_list = gdf.contains(point)
    polygon_containing_point = np.where(polygons_containing_point_list)[0]
    if(polygon_containing_point.size > 0):
        return gdf.loc[polygon_containing_point[0]]
    else:
        return None

def get_column_of_gdf_row(row: pandas.core.series, column_name: str):
    return row[column_name]

def get_soiltype_of_point(gdf: gpd.GeoDataFrame,point: geometry.point.Point):
    soiltypeColumnName = 'TSYM'
    row_containing_point = first_row_of_gdf_containing_point(gdf,point)
    if not (row_containing_point is None):
        return get_column_of_gdf_row(row_containing_point,soiltypeColumnName)
    else : 
        return None

def find_soiltype_of_cornerpoints(gdf: gpd.GeoDataFrame, polygon: gpd.GeoSeries):
    minx,miny,maxx,maxy = polygon.bounds
    cornerpoints = []
    cornerpoints.extend([geometry.Point(minx,miny),geometry.Point(minx,maxy),geometry.Point(maxx,miny),geometry.Point(maxx,maxx)])
    
    foundSoilTypes = []
    for point in cornerpoints:
        soiltype = get_soiltype_of_point(gdf,point)
        if not (soiltype is None):
            foundSoilTypes.append(soiltype)
    
    if foundSoilTypes != []:
        return random.choice(foundSoilTypes)
    else:      
        return  None


def add_center_to_gdf(gdf: gpd.GeoDataFrame):
    gdf['center'] = gdf.centroid
    return gdf
#script:
crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

gridsizes = [10000] #100km grid size
update_csv_files = False #Set true if CSV files should be updated
plot_grid = True
using_mac = False

for gridsize in gridsizes:
    soiltypeColumnName = 'soiltype'
    centerColumnName = 'center'
    if using_mac: 
        dk_soiltype_geodataframe = convert_shp_to_gdf_using_crs('data\\Jordart_200000_Shape\\jordart_200000.shp',crs)
        dk_geodataframe_grid = convert_gdf_to_gdfgrid(dk_soiltype_geodataframe,gridsize,crs) 
    else:
        dk_soiltype_geodataframe = convert_shp_to_gdf_using_crs('data/Jordart_200000_Shape/Jordart_200000.shp',crs)
        dk_geodataframe_grid = convert_gdf_to_gdfgrid(dk_soiltype_geodataframe,gridsize) 

    #Adding relevant data to our geodataframe
    dk_geodataframe_grid[soiltypeColumnName] = ''
    dk_geodataframe_grid[centerColumnName] = dk_geodataframe_grid.centroid

    #Going through all grids an finding the needed soiltype
    bar = Bar('Finding soiltype of all gridcells', max=len(dk_geodataframe_grid.index))
    output_dk_grid = []
    for index, grid in dk_geodataframe_grid.iterrows():    
        found_soiltype = get_soiltype_of_point(dk_soiltype_geodataframe,grid[centerColumnName]) 
        if not (found_soiltype is None):
            output_dk_grid.append([grid['geometry'], found_soiltype])        
        else :
            corner_soiltype = find_soiltype_of_cornerpoints(dk_soiltype_geodataframe,grid['geometry'])
            if not (corner_soiltype is None):
                output_dk_grid.append([grid['geometry'], corner_soiltype])        
        bar.next()
    bar.finish()    

    output_dk_gdf_grid = gpd.GeoDataFrame(output_dk_grid, columns=['geometry', soiltypeColumnName])
    if(plot_grid):
        output_dk_gdf_grid.plot(column = soiltypeColumnName) 
        plt.show()

    if(update_csv_files):
        save_gdf_to_csv_in_folder('csv_files',f'DK_Soiltypes_{gridsize}.csv',output_dk_gdf_grid)
        output_dk_gdf_grid.drop(soiltypeColumnName, inplace=True, axis=1)
        save_gdf_to_csv_in_folder('csv_files',f'DK_Grid_{gridsize}.csv',output_dk_gdf_grid)
