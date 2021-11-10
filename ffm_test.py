from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import csvTools


crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps


gdf = csvTools.convert_csv_to_gdf('csv_files\\DK_Plant_10000.csv',True,crs)
gdf_soil = csvTools.convert_csv_to_gdf('csv_files\\DK_SoilTypes_10000.csv',True,crs)
print(gdf)
#gdf['Target'] = ''
X_train, X_test, Y_train, Y_test = train_test_split(gdf,gdf['Salix caprea'],test_size=0.33)
features_except_geometry = list(gdf.columns)
features_except_geometry.remove('geometry')

model = RandomForestClassifier()
model.fit(X_train[features_except_geometry],Y_train)
print(model.score(X_test[features_except_geometry],Y_test))

print(X_test)
y_predicted = model.predict(X_test[features_except_geometry])

print(y_predicted)

cm = confusion_matrix(Y_test,y_predicted)
print(cm)


#gridmaker.save_gdf_to_csv_in_folder('csv_files','DK_Plant_10000_with_target')

"""
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
"""