import json
from typing import List, Tuple
from attr import dataclass
import geopy.distance
from shapely.geometry import geo
from pyproj import Proj
import geopandas as gpd
from pprint import pprint
import pandas as pd


list_of_coordinates_stations = []
list_of_stationids = []
list_of_ids = []
listofdistances = []
coords_plant = (52.2296756, 21.0122287)
coords = []
theid = []
coordinatesofneareststation = []

with open('/Users/cecilieronmogensen/Desktop/VSC/winddatamonth.json') as wdm:
    data = json.load(wdm)
  
def joinids(aList):
    for list in aList:
        list_of_ids = ''.join(list)      
    return list_of_ids  

def get_id_and_coords_for_each_station(): 
    for key, i in data.items():
        if key != 'features':
            continue
        for j in i:
            list_of_stationids.append(list(j["properties"]["stationId"]))
            joinids(list_of_stationids)
            list_of_coordinates_stations.append((tuple(j["geometry"]["coordinates"])[::-1]))
    return list_of_stationids, list_of_coordinates_stations



def get_id_of_nearest_station(coords_plant): 
    for coords_station in list_of_coordinates_stations:
        distance = (geopy.distance.distance(coords_plant, coords_station).km)
        listofdistances.append(distance)
        listofdistances.sort()
        if (geopy.distance.distance(coords_plant, coords_station).km) == listofdistances[0]: 
            coordinatesofneareststation = coords_station

    print("Distance to the nearest station: ")
    print(listofdistances[0])
    print("Coordinates of the nearest station: ")
    print(coordinatesofneareststation)


    for key, i in data.items():
        if key != 'features':
            continue
        for j in i:
            theid.append(list(j["properties"]["stationId"]))
            coords.append(tuple(j["geometry"]["coordinates"])[::-1])
            if (tuple(j["geometry"]["coordinates"])[::-1]) == coordinatesofneareststation: 
                thestationid = joinids(theid)
    print("The id of the nearest station: ")
    print(thestationid)  

    return thestationid

get_id_and_coords_for_each_station()
get_id_of_nearest_station(coords_plant=(52.2296756, 21.0122287))



