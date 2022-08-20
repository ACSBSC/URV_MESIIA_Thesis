#Python Scripts
import get_files as gf
import get_DataFrame as gDF
import ml_train as mlT
import ml_train_parallel as mlT_parallel
import pandas as pd
import time

if __name__ == "__main__" :
    
    
    #uncomment the following path to create the 2 classification models and if the RanSap dataset is stored locally
    #get random file paths (2 per folder)
    win7_120_hdd = gf.get_files()
    
    #Open the selected paths and load it as dataframe
    gDF.get_DF(win7_120_hdd)


    start_time_0 = time.time() 
    RFC_np_acc, DTC_np_acc = mlT.train_model()
    finalexectime_0 = time.time() - start_time_0  
    
    mlT.predict()
    
    
    
    start_time_1 = time.time() 
    RFC_p_acc, DTC_p_acc = mlT_parallel.train_model()
    finalexectime_1 = time.time() - start_time_1
    
    mlT_parallel.prediction()
    
    
    print()
    print("Time taken for training model without parallel processes: \n", finalexectime_0)
    print()
    print("Time taken for training model with parallel processes: \n", finalexectime_1)
    
    ###############################################################################################################################
    '''run_ = 1
    RFC_np_acc.extend([run_,finalexectime_0, "non-parallel_method"])
    DTC_np_acc.extend([run_,finalexectime_0, "non-parallel_method"])
    RFC_p_acc.extend([run_,finalexectime_1, "parallel_method"])
    DTC_p_acc.extend([run_,finalexectime_1, "parallel_method"])
    
    list_RFC = ["Accuracy_Model_1", "Accuracy_Model_2", "Accuracy_Model_3", "Accuracy_Model_4", "Accuracy_Model_5", "Accuracy_Model_6", "Run", "Time_Run","Method"]
    
    df_RFC_ = pd.DataFrame([RFC_p_acc, RFC_np_acc], columns=list_RFC)
    
    list_DTC = ["Accuracy_Model_1", "Accuracy_Model_2", "Accuracy_Model_3", "Accuracy_Model_4", "Run", "Time_Run","Method"]
    
    df_DTC_ = pd.DataFrame([DTC_p_acc,DTC_np_acc], columns=list_DTC)
    
    df_RFC_.to_csv('Acc_Result_RFC.csv', mode='a', index = False, header=False)
    df_DTC_.to_csv('Acc_Result_DTC.csv', mode='a', index = False, header=False)'''

        