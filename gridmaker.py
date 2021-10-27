import geopandas as gpd
from geopandas import geodataframe
from matplotlib import pyplot as plt
import shapely
#from progress.bar import Bar
import os
from pathlib import Path
import numpy as np

#functions:
def save_gdf_to_csv_in_folder(foldername,filename,gdf):
    Path(foldername).mkdir(parents=True, exist_ok=True)
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, foldername, filename)
    gdf.to_csv(file_path, index=False)

def calculateCenter(xmin,xmax,ymin,ymax):
    xmean = (xmin+xmax)/2
    ymean = (ymin+ymax)/2
    return shapely.geomety.Point(xmean,ymean)

def convert_gdf_to_gdfgrid(gdf,distance_pr_cell_in_m):
    xmin, ymin, xmax, ymax = gdf.total_bounds
    grid_cells = []
    x = xmin
    while x < xmax:
        y = ymin
        while y < ymax:
            grid_cells.append(shapely.geometry.box(x, y, x+distance_pr_cell_in_m, y+distance_pr_cell_in_m))
            y += distance_pr_cell_in_m
        x += distance_pr_cell_in_m
    return gpd.GeoDataFrame(grid_cells, columns=['geometry'], crs=crs)    

def convert_shp_to_gdf_using_crs(shp,crs):
    geodataframe = gpd.read_file(shp)
    return geodataframe.to_crs(crs)

def first_row_of_gdf_containing_point(gdf,point):
    polygons_containing_point_list = gdf.contains(point)
    polygon_containing_point = np.where(polygons_containing_point_list)[0]
    if(polygon_containing_point.size > 0):
        return gdf.loc[polygon_containing_point[0]]
    else:
        return None

def add_center_to_gdf(gdf):
    gdf['center'] = gdf.centroid
    return gdf

#script:
crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

gridsizes = [10000] #100km grid size
update_csv_files = False #Set true if CSV files should be updated
plot_grid = True

for gridsize in gridsizes:

    soiltypeColumnName = 'soiltype'
    centerColumnName = 'center'

    dk_soiltype_geodataframe = convert_shp_to_gdf_using_crs('data/Jordart_200000_Shape/Jordart_200000.shp',crs)
    dk_geodataframe_grid = convert_gdf_to_gdfgrid(dk_soiltype_geodataframe,gridsize) 

    #Adding relevant data to our geodataframe
    dk_geodataframe_grid[soiltypeColumnName] = ''
    dk_geodataframe_grid[centerColumnName] = dk_geodataframe_grid.centroid
    
    #Going through all grids an finding the needed soiltype
    #bar = Bar('Finding soiltype of all gridcells', max=len(dk_geodataframe_grid.index))
    output_dk_grid = []
    for index, grid in dk_geodataframe_grid.iterrows():    
        row_containing_point = first_row_of_gdf_containing_point(dk_soiltype_geodataframe,grid[centerColumnName]) 
        if not (row_containing_point is None):
            foundSoilType = row_containing_point['TSYM']
            output_dk_grid.append([grid['geometry'], foundSoilType])        
        #bar.next()
    #bar.finish()    


    output_dk_gdf_grid = gpd.GeoDataFrame(output_dk_grid, columns=['geometry', soiltypeColumnName])
    if(plot_grid):
        output_dk_gdf_grid.plot(column = soiltypeColumnName) 
        plt.show()
        
    if(update_csv_files):
        save_gdf_to_csv_in_folder('csv_files',f'DK_Soiltypes_{gridsize}.csv',output_dk_gdf_grid)
        output_dk_gdf_grid.drop(soiltypeColumnName, inplace=True, axis=1)
        save_gdf_to_csv_in_folder('csv_files',f'DK_Grid_{gridsize}.csv',output_dk_gdf_grid)
