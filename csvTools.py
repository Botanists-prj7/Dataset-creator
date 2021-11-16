import pandas as pd
import geopandas as gpd
from shapely import wkt
import os
from pathlib import Path

def convert_csv_to_gdf(csv_file_path: str, has_geometry_column:bool, crs:str):
    df = pd.read_csv(csv_file_path)
    if has_geometry_column:
        df['geometry'] = df['geometry'].apply(wkt.loads)
        return gpd.GeoDataFrame(df, crs=crs).set_geometry('geometry')
    else :
        return gpd.GeoDataFrame(df, crs=crs)

def save_gdf_to_csv_in_folder(foldername: str,filename: str, gdf: gpd.GeoDataFrame):
    Path(foldername).mkdir(parents=True, exist_ok=True)
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, foldername, filename)
    gdf.to_csv(file_path, index=False)