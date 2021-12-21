# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:35:21 2021

@author: lasse
"""
import pandas as pd 
import matplotlib.pyplot as plt

sundatapryear = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateSun.csv')
raindatapryear = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateRain.csv')
winddatapryear = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateWind.csv')
mintempdatapryear = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateMinTemp.csv')
maxtempdatapryear = pd.read_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateMaxTemp.csv')



def averagePlotter(weatherData, title, weatherType, xlabel, isWind):
    if isWind == False:
        meansData = weatherData[['{weatherType}January'.format(weatherType = weatherType),
                               '{weatherType}February'.format(weatherType = weatherType),
                               '{weatherType}March'.format(weatherType = weatherType),
                               '{weatherType}April'.format(weatherType = weatherType),
                               '{weatherType}May'.format(weatherType = weatherType),
                               '{weatherType}June'.format(weatherType = weatherType),
                               '{weatherType}July'.format(weatherType = weatherType),
                               '{weatherType}August'.format(weatherType = weatherType),
                               '{weatherType}September'.format(weatherType = weatherType),
                               '{weatherType}October'.format(weatherType = weatherType),
                               '{weatherType}November'.format(weatherType = weatherType),
                               '{weatherType}December'.format(weatherType = weatherType)]].mean(axis = 1)
        weatherData['number of stations'] = meansData
        plotableData = weatherData[['number of stations']]
        
        plt.hist(plotableData)
        plt.title(title, fontsize=25)
        plt.ylabel('Number of stations', fontsize=20)
        plt.xlabel(xlabel, fontsize=20)
    else:
        meansData = weatherData[['{weatherType}January'.format(weatherType = weatherType),
                               '{weatherType}February'.format(weatherType = weatherType),
                               '{weatherType}March'.format(weatherType = weatherType),
                               '{weatherType}July'.format(weatherType = weatherType),
                               '{weatherType}August'.format(weatherType = weatherType),
                               '{weatherType}September'.format(weatherType = weatherType),
                               '{weatherType}October'.format(weatherType = weatherType),
                               '{weatherType}November'.format(weatherType = weatherType),
                               '{weatherType}December'.format(weatherType = weatherType)]].mean(axis = 1)
        weatherData['number of stations'] = meansData
        plotableData = weatherData[['number of stations']]
      
        plt.hist(plotableData)
        plt.title(title, fontsize=25)
        plt.ylabel('Number of stations', fontsize=20)
        plt.xlabel(xlabel, fontsize=20)
    plt.show()
    return meansData


val = input("Enter weather type: ")

if val == 'sun':
    averagePlotter(sundatapryear, 'Mean of monthly sun', 'sun', 'Sunlight in hours', False)
elif val == 'rain':
    averagePlotter(raindatapryear, 'Mean of monthly rainfall','rain','Rain in mm', False)
elif val == 'wind':
    averagePlotter(winddatapryear, 'Mean of monthly windspeed', 'wind','Windspeed in m/s', True)
elif val == 'min':
    averagePlotter(mintempdatapryear, 'Mean of monthly minimum temperature', 'minTemp','Minimum temperature in Celcius', False)
elif val == 'max':
    averagePlotter(maxtempdatapryear, 'Mean of monthly maximum temperature', 'maxTemp','Maximum temperature in Celcius', False)
else:
    print('not a valid weather type: try: sun, rain, wind, min or max')


#test = sundatapryear[['sunJanuary','sunFebruary','sunMarch','sunApril','sunMarch','sunJune','sunJuly','sunAugust','sunSeptember','sunOctober','sunNovember','sunDecember']].mean(axis = 1)
#sundatapryear['mean value'] = test
#sundata = sundatapryear[['meanVal']]
#sundata.plot.hist(title = 'average daily sun pr. year', legend = True, xlabel ='hello')

#sundatapryear.plot.hist(by = sundatapryear['meanVal'], title = 'average daily sun pr. year', legend = True, xlabel ='hello')
#raindatapryear[['rainJanuary','rainFebruary','rainMarch','rainApril','rainMarch','rainJune','rainJuly','rainAugust','rainSeptember','rainOctober','rainNovember','rainDecember']].mean(axis = 1).sort_values().plot(kind='hist', title = 'Rain data pr year',xlabel='Weatherstaiton ID', ylabel='Rainfall per day in millimiter')
#winddatapryear[['windJanuary','windFebruary','windMarch','windJuly','windAugust','windSeptember','windOctober','windNovember','windDecember']].mean(axis = 1).sort_values().plot(kind='bar', xlabel='Weatherstaiton ID', ylabel='Wind Strength')
#mintempdatapryear[['minTempJanuary','minTempFebruary','minTempMarch','minTempApril','minTempMarch','minTempJune','minTempJuly','minTempAugust','minTempSeptember','minTempOctober','minTempNovember','minTempDecember']].mean(axis = 1).sort_values().plot(kind='bar', xlabel='Weatherstaiton ID', ylabel='Minimum Temperature')
#maxtempdatapryear[['maxTempJanuary','maxTempFebruary','maxTempMarch','maxTempApril','maxTempMarch','maxTempJune','maxTempJuly','maxTempAugust','maxTempSeptember','maxTempOctober','maxTempNovember','maxTempDecember']].mean(axis = 1).sort_values().plot(kind='bar', xlabel='Weatherstaiton ID', ylabel='Maximum Temperature')


'''
sundatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateSunyearly.csv')
raindatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateRainyearly.csv')
winddatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateWindyearly.csv')
mintempdatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateMinTempyearly.csv')
maxtempdatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateMaxTempyearly.csv')
'''