# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:18:09 2021

@author: lasse
"""

import geopandas as gpd

maxTemp = gpd.read_file('C:/Users/lasse/OneDrive/Dokumenter/ProjektCSIT7/Tempdata/maxtempdatamonth.json')     
minTemp = gpd.read_file('C:/Users/lasse/OneDrive/Dokumenter/ProjektCSIT7/Tempdata/mintempdatamonth.json')
wind = gpd.read_file('C:/Users/lasse/OneDrive/Dokumenter/ProjektCSIT7/Tempdata/winddatamonth.json')
sun = gpd.read_file('C:/Users/lasse/OneDrive/Dokumenter/ProjektCSIT7/Tempdata/sundatamonth.json')
rain = gpd.read_file('C:/Users/lasse/OneDrive/Dokumenter/ProjektCSIT7/Tempdata/raindatamonth.json')

def columnDropper(oldData):
    return oldData[['from','stationId','value','geometry']]
    
def coordCreator(oldData):
    x = []
    y = []
    geometryLoc = oldData.columns.get_loc('geometry')
    newData = oldData[oldData['stationId']==0]
    for i in range(len(oldData)):
        point = oldData.iloc[i,geometryLoc] 
        if point.x >= 0:
            newData = newData.append(oldData.iloc[[i]])
            x.append(point.x)
            y.append(point.y)
    newData.reset_index(drop = True, inplace=True)
    newData['x'] = x
    newData['y'] = y
    oldData = newData
    return oldData

def tableRemaster(oldData, rename):
    stationArray = meanCalculator = meanCalculated = dateArray = oldData[oldData['stationId']==0]
    oldData['{newName}January'.format(newName = rename)],oldData['{newName}February'.format(newName = rename)],oldData['{newName}March'.format(newName = rename)],oldData['{newName}April'.format(newName = rename)],oldData['{newName}May'.format(newName = rename)],oldData['{newName}June'.format(newName = rename)],oldData['{newName}July'.format(newName = rename)],oldData['{newName}August'.format(newName = rename)],oldData['{newName}September'.format(newName = rename)],oldData['{newName}October'.format(newName = rename)],oldData['{newName}November'.format(newName = rename)],oldData['{newName}December'.format(newName = rename)] = ['','','','','','','','','','','','']
    stationID = oldData.drop_duplicates(subset='stationId')
    stIdLoc = stationID.columns.get_loc('stationId')
    fromLoc = stationID.columns.get_loc('from')
    
    for i in range(len(stationID)):
        for j in range(len(oldData)):
            if stationID.iloc[i,stIdLoc]==(oldData.iloc[j,stIdLoc]):
                NewRow = oldData.loc[[j]]
                stationArray = stationArray.append(NewRow)
                
        for k in range(len(stationArray)):
            for l in range(len(stationArray)):
                if stationArray.iloc[k,fromLoc][5:7] == (stationArray.iloc[l,fromLoc][5:7]):
                    NewTempRow = stationArray.iloc[[l]]
                    dateArray = dateArray.append(NewTempRow)
    
            dateArray['value'] = dateArray['value'].mean()
            meanCalculator = meanCalculator.append(dateArray.drop_duplicates(subset ='stationId'))
            dateArray = oldData[oldData['stationId']==0]
        
        for w in range(len(meanCalculator)):
            i=w-1
            if meanCalculator.iloc[i,fromLoc][5:7] == '01':
                meanCalculator['{newName}January'.format(newName = rename)] = meanCalculator.iloc[i]['value']

            if meanCalculator.iloc[i,fromLoc][5:7] == '02':
                meanCalculator['{newName}February'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '03':
                meanCalculator['{newName}March'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '04':
                meanCalculator['{newName}April'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '05':
                meanCalculator['{newName}May'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '06':
                meanCalculator['{newName}June'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '07':
                meanCalculator['{newName}July'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '08':
                meanCalculator['{newName}August'.format(newName = rename)] = meanCalculator.iloc[i]['value']
            
            if meanCalculator.iloc[i,fromLoc][5:7] == '09':
                meanCalculator['{newName}September'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '10':
                meanCalculator['{newName}October'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '11':
                meanCalculator['{newName}November'.format(newName = rename)] = meanCalculator.iloc[i]['value']
                
            if meanCalculator.iloc[i,fromLoc][5:7] == '12':
                meanCalculator['{newName}December'.format(newName = rename)] = meanCalculator.iloc[i]['value']
    
        meanCalculated = meanCalculated.append(meanCalculator.drop_duplicates(subset='from'))
        meanCalculated = meanCalculated.drop_duplicates(subset='stationId')
        meanCalculated.reset_index(drop=True,inplace=True)
        meanCalculator = stationArray = oldData[oldData['stationId']==0]
        meanCalculated.drop(['from','value'], axis = 1, inplace = True)

    return meanCalculated

maxTempSmall = columnDropper(maxTemp)
maxTempCoord = coordCreator(maxTempSmall)
maxTempCalculated = tableRemaster(maxTempCoord, 'maxTemp')
maxTempCalculated.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateMaxTemp.csv')

minTempSmall = columnDropper(minTemp)
minTempCoord = coordCreator(minTempSmall)
minTempCalculated = tableRemaster(minTempCoord, 'minTemp')
minTempCalculated.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateMinTemp.csv')

windSmall = columnDropper(wind)
windCoord = coordCreator(windSmall)
windCalculated = tableRemaster(windCoord, 'wind')
windCalculated.drop(['windApril','windMay','windJune'], axis=1, inplace=True)
windCalculated.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateWind.csv')

sunSmall = columnDropper(sun)
sunCoord = coordCreator(sunSmall)
sunCalculated = tableRemaster(sunCoord, 'sun')
sunCalculated.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateSun.csv')

rainSmall = columnDropper(rain)
rainCoord = coordCreator(rainSmall)
rainCalculated = tableRemaster(rainCoord,'rain')
rainCalculated.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateRain.csv')

