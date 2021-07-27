import csv
import random

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
        






if __name__ == '__main__':
    print("recall")
    arraysource = ligne('samplesortie2.csv')
    print(getClientSystem(arraysource))
    testlist=['a','b','c','d','e','f','g']

    testlist = shuffleList(getClientSystem(arraysource))
    folds = split(testlist, 10)
    print(folds)
    print(len(folds))
    print(arraysource[0])
    print(tenFold(folds))