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




sundatapryear['yearlyAverage'] = round(sundatapryear[['sunJanuary','sunFebruary','sunMarch','sunApril','sunMarch','sunJune','sunJuly','sunAugust','sunSeptember','sunOctober','sunNovember','sunDecember']].mean(axis = 1))
raindatapryear['yearlyAverage'] = round(raindatapryear[['rainJanuary','rainFebruary','rainMarch','rainApril','rainMarch','rainJune','rainJuly','rainAugust','rainSeptember','rainOctober','rainNovember','rainDecember']].mean(axis = 1))
winddatapryear['yearlyAverage'] = round(winddatapryear[['windJanuary','windFebruary','windMarch','windMarch','windJuly','windAugust','windSeptember','windOctober','windNovember','windDecember']].mean(axis = 1))
mintempdatapryear['yearlyAverage'] = round(mintempdatapryear[['minTempJanuary','minTempFebruary','minTempMarch','minTempApril','minTempMarch','minTempJune','minTempJuly','minTempAugust','minTempSeptember','minTempOctober','minTempNovember','minTempDecember']].mean(axis = 1))
maxtempdatapryear['yearlyAverage'] = round(maxtempdatapryear[['maxTempJanuary','maxTempFebruary','maxTempMarch','maxTempApril','maxTempMarch','maxTempJune','maxTempJuly','maxTempAugust','maxTempSeptember','maxTempOctober','maxTempNovember','maxTempDecember']].mean(axis = 1))

sundatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateSunyearly.csv')
raindatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateRainyearly.csv')
winddatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateWindyearly.csv')
mintempdatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateMinTempyearly.csv')
maxtempdatapryear.to_csv('C:/Users/lasse/OneDrive/Dokumenter/GitHub/Dataset-creator/csv_files/DK_ClimateMaxTempyearly.csv')