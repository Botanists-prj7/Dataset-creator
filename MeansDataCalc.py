# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:18:09 2021

@author: lasse
"""

import geopandas as gpd

tempData = gpd.read_file('C:/Users/lasse/OneDrive/Dokumenter/ProjektCSIT7/Tempdata/maxtempdatamonth.json')      
stationID = tempData.drop_duplicates(subset='stationId')

stationArray = meanCalculator = meanCalculated = dateArray = dkCoord = tempData[tempData['stationId']==0]
stIdLoc = stationID.columns.get_loc('stationId')
fromLoc = stationID.columns.get_loc('from')
geometryLoc = stationID.columns.get_loc('geometry')

x = []
y = []
for i in range(len(tempData)):
    point = tempData.iloc[i,geometryLoc] 
    if point.x > 0:
        dkCoord = dkCoord.append(tempData.iloc[[i]])
        x.append(point.x)
        y.append(point.y)
dkCoord.reset_index(drop = True, inplace=True)
dkCoord['x'] = x
dkCoord['y'] = y
tempData = dkCoord

#lav koordinater om til nye kolonner
for i in range(len(stationID)):
    for j in range(len(tempData)):
        if stationID.iloc[i,stIdLoc]==(tempData.iloc[j,stIdLoc]):
            NewRow = tempData.loc[[j]]
            stationArray = stationArray.append(NewRow)
            
    for k in range(len(stationArray)):
        for l in range(len(stationArray)):
            if stationArray.iloc[k,fromLoc][5:7] ==(stationArray.iloc[l,fromLoc][5:7]):
                NewTempRow = stationArray.iloc[[l]]
                dateArray = dateArray.append(NewTempRow)
                
        dateArray['value'] = dateArray['value'].mean()
        meanCalculator = meanCalculator.append(dateArray.drop_duplicates(subset ='stationId'))
        dateArray = tempData[tempData['stationId']==0]
        
    meanCalculated = meanCalculated.append(meanCalculator.drop_duplicates(subset = 'from'))
    meanCalculated.reset_index(drop=True,inplace=True)
    meanCalculator = stationArray = tempData[tempData['stationId']==0]

meanCalculated.plot()