import pandas as pd




"""
csv = pd.read_csv('csv_files/weatherstationandplants.csv')
rain_february_mean = csv['rainFebruary'].mean()
rain_march_mean = csv['rainMarch'].mean()
rain_july_mean = csv['rainJuly'].mean()
rain_august_mean = csv['rainAugust'].mean()
rain_september_mean = csv['rainSeptember'].mean()
rain_october_mean = csv['rainOctober'].mean()
rain_november_mean = csv['rainNovember'].mean()
rain_december_mean = csv['rainDecember'].mean()

csv['rainFebruary'].fillna(rain_february_mean, inplace=True)
csv['rainMarch'].fillna(rain_march_mean, inplace=True)
csv['rainJuly'].fillna(rain_july_mean, inplace=True)
csv['rainAugust'].fillna(rain_august_mean, inplace=True)
csv['rainSeptember'].fillna(rain_september_mean, inplace=True)
csv['rainOctober'].fillna(rain_october_mean, inplace=True)
csv['rainNovember'].fillna(rain_november_mean, inplace=True)
csv['rainDecember'].fillna(rain_december_mean, inplace=True)

csv.pd

newcsv = csv.fillna(csv.mean())
newcsv.to_csv('csv_files/weatherstations_and_plants_notnull.csv')
print(csv.isnull().values.sum()) """


occurences = pd.read_csv('csv_files/new_dataset_with_occurences.csv')
occurences.drop(columns=['Unnamed: 0','geometry','index_right_x_x','Unnamed: 0_x_x','stationId_x_x','x_x_x','y_x_x','index_right_y_x','Unnamed: 0_y_x','stationId_y_x','x_y_x','y_y_x','index_right_x_y','Unnamed: 0_x_y','stationId_x_y','x_x_y','y_x_y','index_right_y_y','Unnamed: 0_y_y','stationId_y_y','x_y_y','y_y_y','Unnamed: 0.1','stationId','x','y'],inplace=True)
occurences.to_csv('csv_files/new_dataset_with_occurences_final.csv')



