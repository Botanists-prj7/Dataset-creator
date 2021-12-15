import heatMapResults
import pandas as pd
import contextily as cx
import matplotlib.pyplot as plt
import geopandas as gpd
import csvTools

def plotPlantOccurencesFromDataWithLatLong(plant: str, using_mac: bool = True):
    if using_mac:
        plants = pd.read_csv('data\\data_with_lat_long.csv', error_bad_lines = False, engine='python')
    else:    
        plants = pd.read_csv('data/data_with_lat_long.csv', error_bad_lines = False, engine='python')
    plantsdub = plants[(plants['species']!=plant)].index
    plants.drop(plantsdub, inplace=True)

    #Make axis :O
    fig, ax = plt.subplots(1, figsize=(10,10))

    #plot map on axis
    countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    countries[countries["name"] == "Denmark"].plot(color="lightgrey", ax=ax, alpha=0)

    plants.plot(x="decimalLongitude", y="decimalLatitude", kind="scatter", colormap='PiYG', ax=ax)

    cx.add_basemap(ax,source=cx.providers.CartoDB.Positron,crs='EPSG:4326')

    plt.show()

def plotPlantOccurenceInGrid(plant: str, using_mac: bool = True):
    if using_mac:
        plants = csvTools.convert_csv_to_gdf('csv_files\\DK_Plant_10000.csv',True,'EPSG:3857')
    else:    
        plants = csvTools.convert_csv_to_gdf('csv_files/DK_Plant_10000.csv',True,'EPSG:3857')

    heatMapResults.print_map_of_occurences(plant,'EPSG:3857',geodataframe=plants)