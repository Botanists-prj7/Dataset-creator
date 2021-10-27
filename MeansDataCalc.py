# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:18:09 2021

@author: lasse
"""

import geopandas as gpd

tempData = gpd.read_file('C:/Users/lasse/OneDrive/Dokumenter/ProjektCSIT7/Tempdata/maxtempdatamonth.json')      
stationID = tempData.drop_duplicates(subset='stationId')
tempData['January'],tempData['February'],tempData['March'],tempData['April'],tempData['May'],tempData['June'],tempData['July'],tempData['August'],tempData['September'],tempData['October'],tempData['November'],tempData['December'] = ['','','','','','','','','','','','']



GeodataframeOutput = stationArray = meanCalculator = meanCalculated = dateArray = dkCoord = tempData[tempData['stationId']==0]
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
            if stationArray.iloc[k,fromLoc][5:7] == (stationArray.iloc[l,fromLoc][5:7]):
                NewTempRow = stationArray.iloc[[l]]
                dateArray = dateArray.append(NewTempRow)

        dateArray['value'] = dateArray['value'].mean()
        meanCalculator = meanCalculator.append(dateArray.drop_duplicates(subset ='stationId'))
        dateArray = tempData[tempData['stationId']==0]
        
    for w in range(len(meanCalculator)):
        i=w-1
        if meanCalculator.iloc[i,fromLoc][5:7] == '01':
            meanCalculator['January'] = meanCalculator.iloc[i]['value']
        
        if meanCalculator.iloc[i,fromLoc][5:7] == '02':
            meanCalculator['February'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '03':
            meanCalculator['March'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '04':
            meanCalculator['April'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '05':
            meanCalculator['May'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '06':
            meanCalculator['June'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '07':
            meanCalculator['July'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '08':
            meanCalculator['August'] = meanCalculator.iloc[i]['value']
        
        if meanCalculator.iloc[i,fromLoc][5:7] == '09':
            meanCalculator['September'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '10':
            meanCalculator['October'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '11':
            meanCalculator['November'] = meanCalculator.iloc[i]['value']
            
        if meanCalculator.iloc[i,fromLoc][5:7] == '12':
            meanCalculator['December'] = meanCalculator.iloc[i]['value']


    meanCalculated = meanCalculated.append(meanCalculator.drop_duplicates(subset='from'))
    meanCalculated = meanCalculated.drop_duplicates(subset='stationId')
    meanCalculated.reset_index(drop=True,inplace=True)
    meanCalculator = stationArray = tempData[tempData['stationId']==0]

