import pandas as pd
import geopandas as gpd
from shapely import wkt

def convert_csv_to_gdf(csv_file_path: str, has_geometry_column:bool, crs:str):
    df = pd.read_csv(csv_file_path)
    if has_geometry_column:
        df['geometry'] = df['geometry'].apply(wkt.loads)
        return gpd.GeoDataFrame(df, crs=crs).set_geometry('geometry')
    else :
        return gpd.GeoDataFrame(df, crs=crs)
