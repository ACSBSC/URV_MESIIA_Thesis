import pandas as pd


def get_DF(fileList):
    
    print("Creating Dataframe...")
    print()
    #Initiate an empty dataframe to later add the necessary data
    df = pd.DataFrame(columns=['Timestamp [s]', 'Timestamp [μs]','LBA','Size Block [byte]', 'Shannon Entropy 1','Shannon Entropy 2', 'Software', 'Type'])
    
    #Specify the benign Software for later classifiaction
    benignSoft = ['AESCrypt', 'Excel', 'Firefox', 'SDelete', 'Zip']
    
    #for each path given, open the csv and store it in a temporal dataframe and later add it to df
    for elem in fileList:
        #create an empty temporal dataframe with the columns that exist in the csv
        dfTemp = pd.read_csv(elem, sep=",", names=['Timestamp [s]', 'Timestamp [μs]','LBA','Size Block [byte]', 'Shannon Entropy 1','Shannon Entropy 2'])
        arr = elem.split("\\")
        
        #add two columns to the temporal dataframe that specifies the software name and the type (good or bad software)
        if "-" in arr[2]:
            #if there is a - in the name, just get the first type and save it under software
            #this is becuase is the same type of software but coming from a different file size
            a = arr[2]
            b = a.split("-")
            dfTemp["Software"]= b[0]
            
            if b[0] in benignSoft:
                dfTemp["Type"] = "Benign"
            else:
                dfTemp["Type"] = "Malignant"
            
        else:
            dfTemp["Software"]= arr[2]
            
            if arr[2] in benignSoft:
                dfTemp["Type"] = "Benign"
            else:
                dfTemp["Type"] = "Malignant"

        #after the temporal dataframe is filled, save it to the final dataframe
        df = df.append(dfTemp)

    #return the final dataframe    
    return df

