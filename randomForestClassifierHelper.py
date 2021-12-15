from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import top_k_accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from tabulate import tabulate

class RandomForestClassiferWrapper(): 
    Model = None
    x_train = None
    y_train = None
    x_test = None 
    y_test = None
    train_predictions = None
    test_predictions = None
    test_probabilities = None

    def __init__(self, feature_values, target_values):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(feature_values, target_values, test_size = 0.25, random_state = 42)
        self.model = buildClassifier(self.x_train,self.y_train)
        self.train_predictions = self.model.predict(self.x_train)
        self.test_predictions = self.model.predict(self.x_test)
        self.test_probabilities = self.model.predict_proba(self.x_test)
   

def buildClassifier(x_train,y_train):
    model = RandomForestClassifier()
    model.fit(x_train,y_train)
    return model

def printRandomForestScoreMap(rfcWrapper: RandomForestClassiferWrapper):
    cm = get_confusion_matrix(rfcWrapper.y_test,rfcWrapper.test_predictions)
    
    print(
        tabulate([['accuracy_score_training', 'accuracy_score_test','True_positive','False_positive','True_negative','False_negative', 'precision_score', 'recall_score','f1_score'],[
            accuracy_score(rfcWrapper.y_train, rfcWrapper.train_predictions), 
            accuracy_score(rfcWrapper.y_test, rfcWrapper.test_predictions),
            cm[0][0],
            cm[1][0],
            cm[1][1],
            cm[0][1],
            precision_score(rfcWrapper.y_test,rfcWrapper.test_predictions),
            recall_score(rfcWrapper.y_test,rfcWrapper.test_predictions),
            f1_score(rfcWrapper.y_test,rfcWrapper.test_predictions)]]))
    
def printFeatureList(classifier: RandomForestClassifier, k: int = 200):
    feature_list = list(classifier.feature_names_in_)
    importances = list(classifier.feature_importances_)
    feature_importances = [(feature, round(importance, 4)) for feature, importance in zip(feature_list, importances)]
    feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
    counter = 0
    for pair in feature_importances:
        if counter == k:
            break
        print('Variable: {:20} Importance: {}'.format(*pair))
        counter+=1

def print_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred,labels=[1,0])
    print(cm)
    print('True positive = ', cm[0][0])
    print('False positive = ', cm[1][0])
    print('True negative = ', cm[1][1])
    print('False negative = ', cm[0][1])
    
def get_confusion_matrix(y_true, y_pred):
    return  confusion_matrix(y_true, y_pred,labels=[1,0])
    
    