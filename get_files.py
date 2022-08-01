import os
import random

def get_files():
    
    #Get the files from the locally stored RanSap database
    dirName = './RanSAP/dataset/original'
    print()
    print("Getting Files...")
    print()
    
    #Create a list where all the csv file paths will be stored
    listOfFiles = list()
    
    #Get the paths
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    
    #Create another list where only the ata_write.csv files will be stored.    
    fileList1 = list()  

    #Create a set where the folder's software names will be stored
    category_set = set()
    
    #from the list with all the file paths, get the ata_write.csv files from the first sub-folder 'win7-120gb-hdd'
    for elem in listOfFiles:
        arr = elem.split("\\")
        if arr[4] == "ata_write.csv" and arr[1]=='win7-120gb-hdd':
            fileList1.append(elem)
            category_set.add(arr[2])
    
    #create a list where 2 randmom samples from each software type will be stored
    win7_120_hdd = list()
    
    #For loops for selecting the random paths for the dataframes
    for type in category_set:
        temp_list = list()
        for link in fileList1:
            splitted = link.split("\\")
            
            if splitted[2]==type:
                temp_list.append(link)
            
            elif len(temp_list)>10: #there are only 10 files per folder
                break
            else:
                continue
        
        win7_120_hdd.extend(random.sample(temp_list, 2))

                
    #return list of selected paths
    return win7_120_hdd  


