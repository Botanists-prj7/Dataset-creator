from logging import error
from os import sep
import geopandas as gpd
from matplotlib import pyplot as plt
from pandas.io import pytables
import shapely
import numpy as np
import pandas as pd
import codecs


def calculateCenter(xmin,xmax,ymin,ymax):
    xmean = (xmin+xmax)/2
    ymean = (ymin+ymax)/2
    return shapely.geomety.Point(xmean,ymean)

crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps
print('loading data...')
dk_gdf = gpd.read_file('geopandas/jordart_200000.shp')
dk_gdf = dk_gdf.to_crs(crs)



#dk_gdf.to_file('C:\AAU\henning.shp')

print(dk_gdf.head())
xmin, ymin, xmax, ymax = dk_gdf.total_bounds

#n_cells=200
distance_pr_cell = 10000 #10km cell size
#cell_size = (xmax-xmin)/n_cells

gridCells2 = []
x = xmin
while x < xmax:
    y = ymin
    while y < ymax:
        gridCells2.append(shapely.geometry.box(x, y, x+distance_pr_cell, y+distance_pr_cell))
        y += distance_pr_cell
    x += distance_pr_cell

#Adding all cells to a GeoDataFrame
cells = gpd.GeoDataFrame(gridCells2, columns=['geometry'], crs=crs)
cells['soiltype'] = ''
print(cells)
#Gettting the centerpoints of all cells.
centroids = cells.centroid

#Going through all centerpoints
counter = 0
foundcentroids = []
for centroid in centroids:
    #Finding what polygon in dk_gdf matches the centerpoint
    polygons_containing_centroid = dk_gdf.contains(centroid)
    polygon_containing_centroid = [i for i, val in enumerate(polygons_containing_centroid) if val]
    #If a match was found, we get the soiltype of that centerpoint
    if(polygon_containing_centroid != []):
        foundSoilType = dk_gdf.loc[polygon_containing_centroid[0],'TSYM']
        cells.loc[counter,'soiltype'] = foundSoilType
    #foundcentroids.append(res)
    print(counter)
    counter+=1


#ax = dk_gdf.plot(column = 'TSYM')
plt.autoscale(False)
cells.plot(column = 'soiltype')
#ax.axis("off")

plt.show()
