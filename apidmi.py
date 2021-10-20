from os import write
import requests
import json
import csv


apisuffix = "www.opengis.net%2Fdef%2Fcrs%2FOGC%2F1.3%2FCRS84&api-key="
apikey = "17574c06-d89e-417d-a747-82f9bd5acac2"
mintemperaturedata = requests.get("https://dmigw.govcloud.dk/v2/climateData/collections/stationValue/items?datetime=..%2F2018-03-18T12%3A31%3A12Z&parameterId=min_temp&timeResolution=month&validity=true&bbox-crs=https%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FOGC%2F1.3%2FCRS84" + apisuffix + apikey)
maxtemperaturedata = requests.get("https://dmigw.govcloud.dk/v2/climateData/collections/stationValue/items?datetime=..%2F2018-03-18T12%3A31%3A12Z&parameterId=max_temp_w_date&timeResolution=month&validity=true&bbox-crs=https%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FOGC%2F1.3%2FCRS84" + apisuffix + apikey)
sunshinedata = requests.get("https://dmigw.govcloud.dk/v2/climateData/collections/stationValue/items?datetime=..%2F2018-03-18T12%3A31%3A12Z&parameterId=bright_sunshine&timeResolution=month&validity=true&bbox-crs=https%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FOGC%2F1.3%2FCRS84" + apisuffix + apikey)
raindata = requests.get("https://dmigw.govcloud.dk/v2/climateData/collections/stationValue/items?datetime=..%2F2018-03-18T12%3A31%3A12Z&parameterId=acc_precip&timeResolution=month&validity=true&bbox-crs=https%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FOGC%2F1.3%2FCRS84" + apisuffix + apikey)
windspeeddata = requests.get("https://dmigw.govcloud.dk/v2/climateData/collections/stationValue/items?datetime=..%2F2018-03-18T12%3A31%3A12Z&parameterId=mean_wind_speed&timeResolution=month&validity=true&bbox-crs=https%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FOGC%2F1.3%2FCRS84" + apisuffix + apikey)
snowdata = requests.get("https://dmigw.govcloud.dk/v2/climateData/collections/stationValue/items?datetime=..%2F2018-03-18T12%3A31%3A12Z&parameterId=snow_depth&timeResolution=month&validity=true&bbox-crs=https%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FOGC%2F1.3%2FCRS84" + apisuffix + apikey)


#response = requests.get("https://dmigw.govcloud.dk/v2/climateData/collections/stationValue/items?datetime=..%2F2018-03-18T12%3A31%3A12Z&parameterId=mean_temp&timeResolution=day&validity=true&bbox-crs=https%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FOGC%2F1.3%2FCRS84")
mintemperature = mintemperaturedata.json()
maxtemperature  = maxtemperaturedata.json()
sun = sunshinedata.json()
rain = raindata.json()
wind = windspeeddata.json()
snow = snowdata.json()

with open('mintempdatamonth.json', 'w') as jsonfile:
    json.dump(mintemperature, jsonfile)

with open('maxtempdatamonth.json', 'w') as jsonfile:
    json.dump(maxtemperature, jsonfile)

with open('sundatamonth.json', 'w') as jsonfile:
    json.dump(sun, jsonfile)

with open('raindatamonth.json', 'w') as jsonfile:
    json.dump(rain, jsonfile)

with open('winddatamonth.json', 'w') as jsonfile:
    json.dump(wind, jsonfile)

with open('snowdatamonth.json', 'w') as jsonfile:
    json.dump(snow, jsonfile)
