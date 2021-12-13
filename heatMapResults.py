import geopandas as gpd
import csvTools
from matplotlib import pyplot as plt
import contextily as cx

def print_heatmap_of_predictions(column:str, crs: str, geodataframe_csv_location:str = None, geodataframe:gpd.GeoDataFrame = None):
    if geodataframe is not None:
        geodataframe_results = geodataframe
    elif geodataframe_csv_location is not None:
        geodataframe_results = csvTools.convert_csv_to_gdf(geodataframe_csv_location,True, crs)
    else :
        print("Couldn't print heatmap of predictions as neither a csv file or a geodataframe was supplied")
        return None

    ax = geodataframe_results.plot(column = column, legend=True, cmap='RdYlGn', scheme='User_Defined',classification_kwds=dict(bins=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]))
    cx.add_basemap(ax,source=cx.providers.CartoDB.Positron)
    plt.show()

def print_map_of_dataset(crs: str, geodataframe_csv_location:str = None, geodataframe:gpd.GeoDataFrame = None):
    if geodataframe is not None:
        geodataframe_results = geodataframe
    elif geodataframe_csv_location is not None:
        geodataframe_results = csvTools.convert_csv_to_gdf(geodataframe_csv_location,True, crs)
    else :
        print("Couldn't printpredictions as neither a csv file or a geodataframe was supplied")
        return None

    ax = geodataframe_results.plot()
    cx.add_basemap(ax,source=cx.providers.CartoDB.Positron)
    plt.show()