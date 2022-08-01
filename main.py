#Python Scripts
import get_files as gf
import get_DataFrame as gDF
import ml_train as mlT

#parallel computing
import lithops as lh
from lithops import FunctionExecutor, Storage
import pickle

import time

if __name__ == "__main__" :
    
    #uncomment the following path to create the 2 classification models and if the RanSap dataset is stored locally
    '''#get random file paths (2 per folder)
    win7_120_hdd = gf.get_files()
    
    #Open the selected paths and load it as dataframe
    df=gDF.get_DF(win7_120_hdd)
    
    print(df.sample(n=10))
    print(len(df))

    #send the df to train
    model_path1, model_path2, X_test, Y_test = mlT.train_model(df)'''
    
    #Following part used once the models are trained and stored
    
    #see score metric (accuracy)
    model_path_RFC = "./trained_AI_models/RFC_model.joblib"
    model_path_DTC = "./trained_AI_models/DTC_model.joblib"
    X_test = "./trained_AI_models/X_test.joblib"
    Y_test = "./trained_AI_models/Y_test.joblib"
    mlT.predict(model_path_RFC, model_path_DTC, X_test, Y_test)
    
    
