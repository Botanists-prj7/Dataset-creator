import csvTools
import randomForestClassifierHelper

#Setup
crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

test_plants = ['Urtica dioica','Crambe maritima','Rosa spinosissima','Impatiens parviflora','Rumex sanguineus']

#Load data
data = csvTools.convert_csv_to_gdf('csv_files/DK_Full_Dataset_10000.csv',True,crs=crs)
data = data.drop(columns=['geometry'])
plant_gdf_grid = csvTools.convert_csv_to_gdf('csv_files/DK_Plant_10000.csv',True,crs=crs)
plant_gdf_grid = plant_gdf_grid.drop(columns=['geometry'])

#Calculate features and target
#feature_values = data.drop(columns=[plant_gdf_grid.columns])
for plant in test_plants:  
    feature_values = data.drop(columns=[plant])
    target_values = data[plant]
    print(plant)
    #Build model
    rfcWrapper = randomForestClassifierHelper.RandomForestClassiferWrapper(feature_values,target_values)
    #Print scorecard
    randomForestClassifierHelper.printRandomForestScoreMap(rfcWrapper)
    print('Top 5 most important features:')
    randomForestClassifierHelper.printFeatureList(rfcWrapper.model,5)
    print()
    print()