#training models AI
from random import randint
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn import metrics

#import sklearn.external.joblib as extjoblib
import joblib

import pickle
import pandas as pd
import random as rnd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def train_model(df):
    print("Training model...")
    print()
    
    features = list(df.columns)
    
    X = df[features[:len(features)-2]]
    Y1 = df[features[-1]] #to predict danger
    #Y2 = df[features[-2]] #to predict type of malware / software
    
    print("Splitting...")
    X1_train, X1_test, y1_train, y1_test = train_test_split(X, Y1, test_size=0.3)
    #X2_train, X2_test, y2_train, y2_test = train_test_split(X, Y2, test_size=0.3)
    
    #Save X_test and Y_test
    X_test_path = "./trained_AI_models/X_test.joblib"
    Y_test_path = "./trained_AI_models/Y_test.joblib"
    joblib.dump(X1_test, X_test_path)
    joblib.dump(y1_test, Y_test_path)
    
    print("Creating models...")
    model1 = DecisionTreeClassifier()
    model2 = RandomForestClassifier(n_estimators=10)
    
    print("Training model DTC")
    model1.fit(X1_train, y1_train)
    filename1 = "./trained_AI_models/DTC_model.joblib"
    joblib.dump(model1, filename1)
    
    print("Training model RFC")
    model2.fit(X1_train, y1_train)
    filename2 = "./trained_AI_models/RFC_model.joblib"
    joblib.dump(model2, filename2)
    
    return filename1,filename2, X_test_path, Y_test_path

def predict(model_path_RFC, model_path_DTC, X_test_path, Y_test_path):
    print("Predicting results...")
    
    loaded_model_RFC = joblib.load(model_path_RFC)
    loaded_model_DTC = joblib.load(model_path_DTC)
    X_test = joblib.load(X_test_path)
    y_test = joblib.load(Y_test_path)
    
    result_RFC = loaded_model_RFC.score(X_test, y_test)
    result_DTC = loaded_model_DTC.score(X_test, y_test)
    print(result_RFC)
    print(result_DTC)
    
    file = "./RanSAP/dataset/original/win7-120gb-hdd/Firefox/Firefox-20210610_23-43-40/ata_write.csv"
    
    X_test_selection = pd.read_csv(file, sep=",", names=X_test.columns)
    
    row = rnd.randint(0,len(X_test_selection))
    X_new = pd.DataFrame(columns=X_test_selection.columns)
    X_new = X_new.append(X_test_selection.iloc[row])
    
    predict_RFC = loaded_model_RFC.predict(X_new)
    predict_DTC = loaded_model_DTC.predict(X_new)
    
    print("Predictions: ")
    print(predict_RFC[0])
    print(predict_DTC[0])
    
    print("Actual classification: ")
    #print(y_test.iloc[row])
    print("Benign")