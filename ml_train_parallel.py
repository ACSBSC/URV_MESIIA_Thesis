#training models AI
from random import randint
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib
from sklearn import metrics
import random as rnd
import pandas as pd
import pickle
from lithops import FunctionExecutor, Storage
import numpy as np
import itertools
import time

def train_RFC_map(id,namespace,storage,estimator, criteria):
    #train the model
    print("Splitting...")
    df = pd.read_csv('Sample_RanSap.csv', sep=",")
    features = list(df.columns)
    X = df[features[:len(features)-2]]
    Y = df[features[-1]] #to predict danger
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
    
    storage.put_object(namespace, 'X_test_RFC_{}'.format(id), pickle.dumps(X_test))
    storage.put_object(namespace, 'Y_test_RFC_{}'.format(id), pickle.dumps(y_test))
    
    model_RFC = RandomForestClassifier(n_estimators=estimator, criterion=criteria)
    
    model_RFC.fit(X_train, y_train)
    
    storage.put_object(namespace, 'Model_RFC_{}'.format(id), pickle.dumps(model_RFC))
  
def accuracy_reduce_RFC(id, namespace, storage, i):
    
    model = storage.get_object(namespace, 'Model_RFC_{}'.format(i))
    model = pickle.loads(model)
    
    X_test = storage.get_object(namespace, 'X_test_RFC_{}'.format(i))
    X_test = pickle.loads(X_test)
    
    y_test = storage.get_object(namespace, 'Y_test_RFC_{}'.format(i))
    y_test = pickle.loads(y_test)
    
    result = model.score(X_test, y_test)
    
    return result
    
def train_DTC_map(id,namespace,storage,criteria, splitter_):
    #train the model
    print("Splitting...")
    
    df = pd.read_csv('Sample_RanSap.csv', sep=",")
    features = list(df.columns)
    X = df[features[:len(features)-2]]
    Y = df[features[-1]] #to predict danger
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
    
    storage.put_object(namespace, 'X_test_DTC_{}'.format(id), pickle.dumps(X_test))
    storage.put_object(namespace, 'Y_test_DTC_{}'.format(id), pickle.dumps(y_test))
    
    model_DTC = DecisionTreeClassifier(criterion = criteria, splitter = splitter_)
    
    model_DTC.fit(X_train, y_train)
    
    storage.put_object(namespace, 'Model_DTC_{}'.format(id), pickle.dumps(model_DTC))
    
def accuracy_reduce_DTC(id, namespace, storage, i):
    
    model = storage.get_object(namespace, 'Model_DTC_{}'.format(i))
    model = pickle.loads(model)
    
    X_test = storage.get_object(namespace, 'X_test_DTC_{}'.format(i))
    X_test = pickle.loads(X_test)
    
    y_test = storage.get_object(namespace, 'Y_test_DTC_{}'.format(i))
    y_test = pickle.loads(y_test)
    
    result = model.score(X_test, y_test)
    
    return result    


def train_model():
    
    namespace = 'RanSap_Model_Training'
    storage = Storage()
    fexec = FunctionExecutor()
    
    #####################################################################################
    
    n_estimators=np.arange(5, 20, 5).tolist()
    criterion = ["gini", "entropy"]
    splitter_ = ["best", "random"]
    
    parameters_RFC = [[namespace],n_estimators, criterion]
    items_RFC = list(itertools.product(*parameters_RFC))
    
    parameters_DTC = [[namespace], criterion, splitter_]
    items_DTC = list(itertools.product(*parameters_DTC))
    
    '''print("DTC PARAM")
    print(items_DTC)
    print("RFC PARAM")
    print(items_RFC)'''
    
    #####################################################################################
    start_time_0 = time.time() 
    
    print()
    print("Creating and training RFC Model...")
    print()
    fexec.map(train_RFC_map, items_RFC)
    fexec.wait()
    
    print()
    print("Getting Accuracy results of RFC' models...")
    print()
    
    itera_RFC = [(namespace,i) for i in range(len(items_RFC))]
   
    fexec.map(accuracy_reduce_RFC, itera_RFC)
    
    result_RFC = fexec.get_result()
    fexec.wait()
    fexec.clean()
    
    finalexectime_0 = time.time() - start_time_0
    #######################################################################################
    start_time_1 = time.time()
    
    print()
    print("Creating and training DTC Model...")
    print()
    fexec.map(train_DTC_map, items_DTC)
    fexec.wait()
    
    print()
    print("Getting Accuracy results of DTC' models...")
    print()
    
    itera_DTC = [(namespace,j) for j in range(len(items_DTC))]
   
    fexec.map(accuracy_reduce_DTC, itera_DTC)
    
    result_DTC = fexec.get_result()
    
    fexec.clean()
    
    finalexectime_1 = time.time() - start_time_1
    ########################################################################################
    
    
    index_RFC = result_RFC.index(max(result_RFC))
    
    model_RFC = storage.get_object(namespace, 'Model_RFC_{}'.format(index_RFC))
    model_RFC = pickle.loads(model_RFC)
 
    joblib.dump(model_RFC, "RFC_model_parallel.joblib")
    
    
    
    index_DTC = result_DTC.index(max(result_DTC))
    
    model_DTC = storage.get_object(namespace, 'Model_DTC_{}'.format(index_DTC))
    model_DTC = pickle.loads(model_DTC)
 
    joblib.dump(model_DTC, "DTC_model_parallel.joblib")
    
    ###########################################################################################
    
    '''print()
    print("RFC accuracy results:")
    print(result_RFC)
    print()
    print("DTC accuracy results:")
    print(result_DTC)
    print()'''
    
    return result_RFC, result_DTC, finalexectime_0, finalexectime_1
    



def prediction():
    
    model_RFC = joblib.load("RFC_model_parallel.joblib")
    model_DTC = joblib.load("DTC_model_parallel.joblib")
    
    file = "./RanSAP/dataset/original/win7-120gb-hdd/Firefox/Firefox-20210610_23-43-40/ata_write.csv"
    X_test = pd.read_csv(file, sep=",", names=['Timestamp [s]', 'Timestamp [μs]','LBA','Size Block [byte]', 'Shannon Entropy 1','Shannon Entropy 2'])
    
    row = rnd.randint(0,len(X_test))
    X_new = pd.DataFrame(columns=X_test.columns)
    X_new = X_new.append(X_test.iloc[row])
    
    res_RFC = model_RFC.predict(X_new)
    res_DTC = model_DTC.predict(X_new)
    
    print("Prediction: ")
    print("RFC: ",res_RFC[0])
    print("DTC: ",res_DTC[0])
   
    print("Actual classification: ")
    print("Benign")