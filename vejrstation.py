# loading library 
#from sklearn.neighbors import KNeighborsClassifier 
 
# instantiate learning model (k = 3) 
#knn = KNeighborsClassifier(n_neighbors=3) 
 
# fitting the model 
#knn.fit(X_train, y_train)

#knn.

import json
#import geopy.distance
from shapely.geometry import geo
from pyproj import Transformer
import pyproj

with open('winddatamonth.json') as wdm:
    data = json.load(wdm)

list_of_coordinates = [
[-53.965, 67.7842], 
[-21.9511, 70.4844],
[-43.1653, 60.0553],
[-48.4544, 60.7636],
[-20.2169, 74.3075],
[-51.7308, 64.1833],
[-13.7119, 80.6494],
[-52.8517, 68.7081],
[-45.44, 61.1575], 
[-50.4058, 62.5789],
[-57.7231, 74.0606],
[-37.6367, 65.6111], 
[-40.3017, 64.7819], 
[-18.6681, 76.7694], 
[-42.0678, 61.9364], 
[-16.6633, 81.6033], 
[-73.1208, 76.7333], 
[-52.5286, 65.0131], 
[-54.6, 70.6561], 
[-45.1461, 59.9911], 
[8.5599, 55.1904], 
[8.1413, 56.0072], 
[11.6035, 55.7358], 
[9.7872, 55.868], 
[8.215, 56.7068], 
[10.8694, 55.7435],
[11.2787, 56.0083],
[8.0828, 55.5575], 
[9.5067, 56.7558], 
[15.0953, 55.0557], 
[11.1348, 55.1593], 
[10.1272, 56.3027], 
[12.149, 55.3955], 
[11.9435, 54.5687],
[9.8882, 55.2444], 
[10.5135, 56.0955],
[12.562, 55.716], 
[12.5263, 55.7664],
[10.5693, 55.0144],
[10.9939, 54.8205], 
[9.1811, 56.0939], 
[8.6551, 55.2908], 
[12.1841, 54.879], 
[10.4398, 55.3088],
[14.7718, 55.2979],
[8.6705, 56.383], 
[9.988, 54.8528],
[11.3879, 55.3224], 
[10.6316, 57.7364], 
[10.0929, 56.5604], 
[10.1353, 56.0803], 
[8.6242, 55.9591], 
[11.8605, 55.2075], 
[8.6412, 56.93], 
[9.9527, 57.1852],  
[11.3292, 54.8275],
[10.3349, 57.3828], 
[12.4121, 55.8764], 
[11.5098, 56.7169], 
[9.1229, 54.8986], 
[11.3285, 55.2465],
[12.3424, 56.1193], 
[-51.7308, 64.1833], 
[-54.6, 70.6561], 
[-42.0678, 61.9364], 
[-45.1461, 59.9911], 
[-33.3739, 83.6561], 
[-52.8517, 68.7081], 
[-21.9511, 70.4844], 
[-53.965, 67.7842], 
[-48.4544, 60.7636], 
[-18.6681, 76.7694], 
[-37.6367, 65.6111], 
[-57.7231, 74.0606], 
[-16.6633, 81.6033], 
[-40.3017, 64.7819], 
[-43.1653, 60.0553], 
[-13.7119, 80.6494], 
[-20.2169, 74.3075], 
[-73.1208, 76.7333], 
[-52.5286, 65.0131], 
[-45.44, 61.1575], 
[-50.4058, 62.5789], 
[12.1841, 54.879], 
[9.1229, 54.8986], 
[12.4121, 55.8764], 
[12.5263, 55.7664], 
[10.5135, 56.0955], 
[8.0828, 55.5575], 
[11.3285, 55.2465], 
[11.3879, 55.3224], 
[10.9939, 54.8205], 
[11.6035, 55.7358], 
[11.2787, 56.0083], 
[12.562, 55.716], 
[8.6242, 55.9591], 
[15.0953, 55.0557], 
[11.5098, 56.7169], 
[8.6412, 56.93], 
[9.9527, 57.1852]
]

list_of_coordinates.sort()

res = []
for i in list_of_coordinates:
    if i not in list_of_coordinates:
        res.append(i)

x=[a[0] for a in list_of_coordinates]
y=[a[1] for a in list_of_coordinates]    

transformer = Transformer.from_crs(4326, 3857)
transformed = transformer.transform(x, y)

print(transformed)


#print(list_of_coordinates)
     

#print(res)
#print(len(list_of_coordinates))

#inProj = Proj(init = 'epsg:4326')
#outProj = Proj(init = 'epsg:3857')
#x,y = transform(inProj,outProj,x,y)

#list1 = [[x],[y]]
#print(list1)

"""
lon = 8.6412, 56.93 
lat = 9.9527, 57.1852

proj1 = pyproj.Proj(init="epsg:4326")
proj2 = pyproj.Proj(init="epsg:3857")
x, y = pyproj.transform(proj1, proj2, lon, lat)
print(x, y)
"""




"""
inProj = Proj(init='epsg:3857')
outProj = Proj(init='epsg:4326')
x1,y1 = -11705274.6374,4826473.6922
x2,y2 = transform(inProj,outProj,x1,y1)
print(x2,y2)
"""

#printer id for alle vejrstationer
ids = []
for dictionary in data['features']:
    if "properties" in dictionary:
        ids.append(dictionary["properties"])
        if "stationId" in dictionary: 
            ids.append(dictionary["stationId"])

#print(ids)



#printer geometry som indeholder coordinates og type
geometry = []
for dictionary in data['features']:
    if "geometry" in dictionary:
        geometry.append(dictionary["geometry"])


"""
#printer 10 koordinater
for i in range(0, 100):
    print(geometry[i])
"""

"""
for element in data['features']:
    for ele in element['id']:
        print(['id'])


for element in data['features']:
    for ele in element['geometry']:
        print('coordinates')    
    print(element['geometry'])'
"""

"""
listofdistances = []
for d in list_of_coordinates():
    listofdistances.append(d)
    listofdistances.sort()

for i in listofdistances(len(listofdistances)):    
    print(listofdistances[i])

coords_plant = (52.2296756, 21.0122287)
for list in list_of_coordinates:
    distance = (geopy.distance.distance(coords_plant, list_of_coordinates).km)
    print(distance)


#beregner afstand mellem plantekoordinater og vejrstationskoordinater
def hej():

    coords_plant = (52.2296756, 21.0122287)
    for list in list_of_coordinates:
        distance = (geopy.distance.distance(coords_plant, list_of_coordinates).km)
        print(distance)
"""
"""
def hejigen(coords_station):
    coords_plant = (52.2296756, 21.0122287)
    distance = (geopy.distance.distance(coords_plant, list_of_coordinates).km)
    distances = [coords_station]
    print(distance)

output = hejigen(hej())
print(output)
"""

#coords_list = [[52.406374, 16.9251681],[52.406374, 16.9251681],[52.406374, 16.9251681]]
coords_plant = (52.2296756, 21.0122287)
coords_station = (52.406374, 16.9251681)
    
#for list in coords_list:
   # for coords_station in list:

"""
list_of_distances = []
for setofcoordinates in list_of_coordinates:
    distance = (geopy.distance.distance(coords_plant, setofcoordinates).km)
    list_of_distances.append(distance)

list_of_distances.sort()
print(list_of_distances[0])
"""
