from ctypes import sizeof
from logging import error
from os import sep
import geopandas as gpd
import pandas as pd
from matplotlib import pyplot as plt

#Read files hehehehehe
plants = pd.read_csv('outfiles/data_with_lat_long.csv', error_bad_lines = False, engine='python')

#Make axis :O
fig, ax = plt.subplots(1, figsize=(10,10))

#plot map on axis
countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
countries[countries["name"] == "Denmark"].plot(color="lightgrey", ax=ax)

plants.plot(x="decimalLongitude", y="decimalLatitude", kind="scatter", colormap='PiYG', ax=ax)

#add grid XD
ax.grid(which = "major", b=True, alpha=0.6)
plt.minorticks_on()
ax.grid(which = "minor", b=True, alpha=0.6)

plt.show()











