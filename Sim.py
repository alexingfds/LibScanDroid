import csv

import numpy
import numpy as np
def ligne(file, sep=","):
    f = open(file, "r")
    r = csv.reader(f, delimiter=sep)
    lignes = list(r)
    f.close()
    # print(lignes)

    return lignes



def similarity(lib1,lib2,input):
    arraysource = ligne(input)
    index1 = 0
    index2 = 0
    countapplib1 = 0
    countapplib2 = 0
    similarity = 0

    for elem in arraysource[0]:
        if (elem == lib1):
            index1 = arraysource[0].index(elem)
        if(elem == lib2):
            index2 = arraysource[0].index(elem)

            # print(index1)
        # else:
        #     if (elem == lib2):
        #         index2 = arraysource[0].index(elem)
                # print(index2)

    for elem in arraysource:
        if (elem[index1] == elem[index2] and (elem[index1] == '1')):
            similarity = similarity + 1

        if (elem[index1] == '1'):
            countapplib1 = countapplib1 + 1

        if (elem[index2] == '1'):
            countapplib2 = countapplib2 + 1
    print('appuselib1==> '+ lib1+':' + str(countapplib1))
    print('appuselib2==> '+lib2+':' + str(countapplib2))
    lib1similarity = similarity / countapplib1
    lib2similarity = similarity / countapplib2
    usim = similarity / (countapplib2 + countapplib1 - similarity)
    average_similarity = (lib2similarity + lib1similarity) / 2

    print('appuselib1==> '+ lib1+':' + str(countapplib1))
    print('appuselib2==> '+lib2+':' + str(countapplib2))
    print('similarity apps between lib1 & lib2:' + str(similarity))
    print('amountApp: ' + str(len(arraysource) - 1))
    print('%Usimilarity:' + str(usim))
    print('%average similarity' + str(average_similarity))
    print('Average between Usimilarity and average_similarity: ' + str((usim + average_similarity) / 2))




if __name__ == "__main__":
    print('trans')
    newcluster = []
    dict={}
    tempdict=[]
    dictlibrary={}

    index=[[1,2,3],[12,13],[4,5,6]]
    # [[1, 2, 9, 10], [3, 11, 12, 13], [4, 5, 6, 7]]

    listclustered=[]
    summ=''
    indextodelete=[]
    arraytestsortie =[['k', 1], ['b', 1], ['c', 2], ['a', 3], ['z', 3], ['d', 3], ['e', 3], ['f', -1], ['g', 1], ['j', 1], ['m', 2], ['n', 2], ['u', 2]]
    arraysource = ligne('samplesortie2.csv')

    for elem in arraysource[0]:
        if(arraysource[0].index(elem)!=0):
            dictlibrary[str(elem)] = elem
    print(dictlibrary)
    print('z' in dictlibrary)
    print(dictlibrary.get('z'))




    # transpose = np.transpose(arraysource)
    # # arraysource.pop(1)
    # numpyArraysource = numpy.array(arraysource)
    # print(arraysource)
    # print(len(numpyArraysource))
    # print(numpyArraysource)
    # # print(transpose)

# =====
    for cluster in index:
        for point in cluster:
            indextodelete.append(point)
    indextodelete.sort()
    print(arraysource)

    for elem in arraysource:
        ajustindex = 0
        for cluster in index:
            for elemindex in cluster:
                a=elemindex -ajustindex
                # print(ajustindex)
                if(elem[a]!='0' and elem[a]!='1'):
                    summ = summ + elem[a]
                    tempdict.append(elem[a])
                    # print(tempdict)
                    
                else:
                    if(elem[a] == '1' and summ !='1'):
                        summ = '1'
                    else:
                        if(summ==''):
                            summ ='0'

            if(summ !='0' and summ !='1'):
                dict[summ] =tempdict
                print(dict)
            elem.append(summ)
            # print(arraysource)
            # print(summ)
            # newcluster.append(summ)
            # print(newcluster)
            # newcluster=[]
            summ=''
            tempdict=[]
        for item in indextodelete:
            thisindex = item -ajustindex
            elem.pop(thisindex)
            ajustindex = ajustindex +1


    print(arraysource)
    print(indextodelete)
    # ============
    # for i in range(1, 4):
    #     elemandindex = []
    #     # print(i)
    #     for elem in arraytestsortie:
    #
    #         # i = 1
    #         if (elem[1] == i):
    #             elemandindex.append(arraytestsortie.index(elem) + 1)
    #     listclustered.append(elemandindex)
    # print(listclustered)
    #









    # similarity('c','k','samplesortie.csv')





