import csv
import os

import pandas as pdd
from _csv import writer, reader
from datetime import datetime


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

def ligne(file, sep=","):
    f = open(file, "r")
    r = csv.reader(f, delimiter=sep)
    lignes = list(r)
    f.close()
    # print(lignes)

    return lignes

def puc(pattern):
    # result = ['a', 'z', 'd', 'y']
    result = flatten(pattern)
    print(result)
    listofIndex = []
    NbrUseLibByApp = []
    NotnullAppUseLib = 0
    Sum = 0
    for elem in arraysource[0]:
        if (elem in result):
            index = arraysource[0].index(elem)
            listofIndex.append(index)

    for element in arraysource:
        if not(arraysource.index(element) == 0):
            NbrappUseLib = 0
            for indexlib in listofIndex:
                if(element[indexlib] =='1'):
                    NbrappUseLib =NbrappUseLib+1
            NbrUseLibByApp.append(NbrappUseLib)
            if not (NbrappUseLib ==0):
                NotnullAppUseLib = NotnullAppUseLib +1
        print(NbrUseLibByApp)
        print(NotnullAppUseLib)
    Sum = sum(NbrUseLibByApp)
    print(Sum)
    numerateur =Sum/len(result)
    PUC =numerateur/NotnullAppUseLib
    print('PUC==> ' + str(PUC))
    return PUC

def averagePuc(listofpattern):
    SumPuc=0
    for elem in listofpattern:
        SumPuc = SumPuc+puc(elem)

    AveragePuc =SumPuc/(len(listofpattern))
    print('AveragePuc==> ' + str(AveragePuc))
    return AveragePuc

def append_list_as_row(file_name, list_of_elem,header_csv=['maxepsilon','minpoint','nbrlibrary','nbrapplication','stepepsilon','nbrPattern','PUC','Datetime']):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        if os.stat(file_name).st_size == 0:
            csv_writer.writerow(header_csv)

        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

if __name__ == '__main__':

    patternTest1 =[['e', 'j', 'q', ['a', 'z', 'd', 'y'], ['k', 'b', 'g', 'p', 'i']]]
    patternTest2 = ['a', 'z', 'd', 'y']
    listpatternTest1 = [['e', 'j', 'q', ['a', 'z', 'd', 'y'], ['k', 'b', 'g', 'p', 'i']],['a', 'z', 'd', 'y']]
    input = 'samplesortie2test.csv'
    # irregular_list = [[666],[1, 2, 3, 4], [5, 6, 7], [8, 9,[888,[33]] , 10], 11]
    # print(flatten(irregular_list))


    arraysource = ligne(input)
    print(arraysource)
    puc(patternTest1)
    puc(patternTest2)
    averagePuc(listpatternTest1)
    append_list_as_row('pucreet.csv',[0.1,'e',datetime.now()])

    # open the file in the write mode
    # with open('pucrecord.csv', 'w', encoding='UTF8') as f:
    #     # create the csv writer
    #     writer = csv.writer(f)
    #
    #     # write a row to the csv file
    #     writer.writerow(['gghfg'])












