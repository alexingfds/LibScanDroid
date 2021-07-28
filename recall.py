import csv
import os
import random
from _csv import writer

import numpy as np

namesfoldValid =['foldvalid_1valid.csv','fold_2valid.csv','fold_3valid.csv','fold_4valid.csv','fold_5valid.csv','fold_6valid.csv','fold_7valid.csv','fold_8valid.csv','fold_9valid.csv','fold_10valid.csv']
namesfoldTraining = ['fold_1Training.csv','fold_2Training.csv','fold_3Training.csv','fold_4Training.csv','fold_5Training.csv','fold_6Training.csv','fold_7Training.csv','fold_8Training.csv','fold_9Training.csv','fold_10Training.csv']

def ligne(file, sep=","):
    f = open(file, "r")
    r = csv.reader(f, delimiter=sep)
    lignes = list(r)
    f.close()
    # print(lignes)
    return lignes
def split(a, n):
    k, m = divmod(len(a), n)
    return list((a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)))

def shuffleList(array):
    random.shuffle(array)
    return array

def getClientSystem(array):
    listClientSystem=[]
    for elem in array:
        if not(array.index(elem) == 0):
            listClientSystem.append(elem)
    return listClientSystem

def tenFold(array):
    for elem in array:
        elem.insert(0,arraysource[0])
    return array
        

def writeFold(fold,nameFold):
    # a = np.array([[1, 4, 2], [7, 9, 4], [0, 6, 2]])
    for data in fold:
        with open('Foldscsv/'+nameFold, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(data)

def writeFoldTraining(folds,validIndex,header_csv):
    pathFile ='Foldscsv/' + namesfoldTraining[validIndex]
    with open(pathFile, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        if os.stat(pathFile).st_size == 0:
            csv_writer.writerow(header_csv)
        for fold in folds:
            if(folds.index(fold) != validIndex):
                    # Add contents of list as last row in the csv file
                    for data in fold:
                        if (data != header_csv):
                            csv_writer.writerow(data)







if __name__ == '__main__':
    print("recall")
    arraysource = ligne('samplesortie1.csv')
    print(getClientSystem(arraysource))
    # testlist=['a','b','c','d','e','f','g']

    testlist = shuffleList(getClientSystem(arraysource))
    folds = split(testlist, 10)
    print("print fold")
    print(len(folds))
    print(folds[0])

    # print(arraysource[0])
    tenfoldObj = tenFold(folds)


    print(tenfoldObj)
    for elem in tenfoldObj:
        for data in elem:
            print(len (data))
            indexOfthisdata =tenfoldObj.index(elem)
        writeFold(elem, namesfoldValid[indexOfthisdata])
        writeFoldTraining(folds,indexOfthisdata,arraysource[0])


