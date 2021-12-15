import csvTools
from geopandas import GeoDataFrame as gdf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def printRandomForestScoreMap(feature_values: gdf,target_values):

    x_train, x_test, y_train, y_test = train_test_split(feature_values, target_values, test_size = 0.25, random_state = 42)

    model = RandomForestClassifier()
    model.fit(x_train,y_train)
    print(model.score(x_test,y_test))


