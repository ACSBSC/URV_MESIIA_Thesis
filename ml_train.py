#training models AI
from random import randint
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn import metrics

#import sklearn.external.joblib as extjoblib
import joblib

import pandas as pd
import numpy as np
import random as rnd
import time


def train_model():
    
    df = pd.read_csv('Sample_RanSap.csv', sep=",")
    features = list(df.columns)
    X = df[features[:len(features)-2]]
    Y = df[features[-1]] #to predict dange
    
    n_estimators=np.arange(5, 20, 5).tolist()
    criterion = ["gini", "entropy"]
    splitters = ["best", "random"]
    
    model_RFC = RandomForestClassifier()
    model_DTC = DecisionTreeClassifier()
    
    #temporal variable to check some results
    accuracy_list_RFC = []
    accuracy_list_DTC = []
    accuracy = 0.0
    
    print("Creating and training RFC Model...")
    print()
    
    start_time_0 = time.time() 
    
    for estimator in n_estimators:
        for criteria in criterion:
            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
            new_model = RandomForestClassifier(n_estimators=estimator, criterion=criteria)
            new_model.fit(X_train, y_train)
            
            accuracy_temp = new_model.score(X_test, y_test)
            accuracy_list_RFC.append(accuracy_temp)
            
            if accuracy_temp>accuracy:
                accuracy=accuracy_temp
                model_RFC = new_model

            #print("({}, {})".format(estimator, criteria))
    finalexectime_0 = time.time() - start_time_0        
    print("Creating and training DTC Model...")
    print()
    
    accuracy = 0.0
    start_time_1 = time.time() 
    for criteria in criterion:
        for splitter_ in splitters:
            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
            new_model = DecisionTreeClassifier(criterion=criteria, splitter=splitter_)
            new_model.fit(X_train, y_train)
            
            accuracy_temp = new_model.score(X_test, y_test)
            accuracy_list_DTC.append(accuracy_temp)
            
            if accuracy_temp>accuracy:
                accuracy=accuracy_temp
                model_DTC = new_model
                
            #print("({}, {})".format(criteria, splitter_))
    finalexectime_1 = time.time() - start_time_1
            
    joblib.dump(model_RFC, "RFC_model.joblib")
    joblib.dump(model_DTC, "DTC_model.joblib")
    
    '''print()
    print("RFC accuracy results:")
    print(accuracy_list_RFC)
    print()
    print("DTC accuracy results:")
    print(accuracy_list_DTC)
    print()'''
    
    return accuracy_list_RFC, accuracy_list_DTC, finalexectime_0, finalexectime_1
    
    

def predict():
    print("Predicting results...")
    
    model_RFC = joblib.load("RFC_model.joblib")
    model_DTC = joblib.load("DTC_model.joblib")
 
    #Predict and classify the given data
    
    file = "./RanSAP/dataset/original/win7-120gb-hdd/Firefox/Firefox-20210610_23-43-40/ata_write.csv"
    X_test = pd.read_csv(file, sep=",", names= ['Timestamp [s]', 'Timestamp [μs]','LBA','Size Block [byte]', 'Shannon Entropy 1','Shannon Entropy 2'])
    
    row = rnd.randint(0,len(X_test))
    X_new = pd.DataFrame(columns=X_test.columns)
    X_new = X_new.append(X_test.iloc[row])
    
    predict_RFC = model_RFC.predict(X_new)
    predict_DTC = model_DTC.predict(X_new)
    
    print("Predictions: ")
    print("RFC: ",predict_RFC[0])
    print("DTC: ",predict_DTC[0])
    
    print("Actual classification: ")
    print("Benign")
    