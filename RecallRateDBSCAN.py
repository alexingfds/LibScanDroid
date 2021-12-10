import csv
import json
import os
from _csv import writer
from datetime import datetime

import numpy
import numpy as np

from RecallrateEvaluation import RecallRateEvaluation
from cluster import Cluster
topkName=['top1.csv','top3.csv','top5.csv','top7.csv','top10.csv']
topnumber=[1,3,5,7,10]
namesfoldValidANDnamesfoldTraining =['fold_1valid.csv', 'fold_2valid.csv', 'fold_3valid.csv', 'fold_4valid.csv', 'fold_5valid.csv', 'fold_6valid.csv', 'fold_7valid.csv', 'fold_8valid.csv', 'fold_9valid.csv', 'fold_10valid.csv']


def getindex(arraytestsortie, nbcluster):
    listclustered = []
    if (nbcluster > 0):
        for i in range(1, nbcluster + 1):
            elemandindex = []
            # print(i)
            for elem in arraytestsortie:

                # i = 1
                if (elem[1] == i):
                    elemandindex.append(arraytestsortie.index(elem) + 1)
            listclustered.append(elemandindex)
        # print(listclustered)
    return (listclustered)


def updateDB(arraysource, index):
    summ = ''
    updict = {}
    tempdict = []
    clusterbyPatern = []

    indextodelete = []
    for cluster in index:
        patternCluster = []
        for point in cluster:
            indextodelete.append(point)
    indextodelete.sort()

    for elem in arraysource:
        ajustindex = 0
        for cluster in index:
            for elemindex in cluster:
                a = elemindex - ajustindex
                # print(ajustindex)
                if (elem[a] != '0' and elem[a] != '1'):
                    summ = summ + elem[a]
                    tempdict.append(dictlibrary.get(elem[a]))
                    # tempdict.insert(0,(dictlibrary.get(elem[a])))
                else:
                    if (elem[a] == '1' and summ != '1'):
                        summ = '1'
                    else:
                        if (summ == ''):
                            summ = '0'

            if (summ != '0' and summ != '1'):
                print(tempdict)
                dictlibrary[summ] = tempdict
                clusterbyPatern.append(tempdict)

                print(dictlibrary)
            elem.append(summ)

            summ = ''
            tempdict = []

        for item in indextodelete:
            thisindex = item - ajustindex
            elem.pop(thisindex)
            ajustindex = ajustindex + 1

    # print(arraysource)
    # print(indextodelete)
    # if not (clusterbyPatern == []):
    #     globalClusterPatern.append(clusterbyPatern)
    return arraysource


def ligne(file, sep=","):
    f = open(file, "r")
    r = csv.reader(f, delimiter=sep)
    lignes = list(r)
    f.close()
    # print(lignes)
    return lignes


def similarity(lib1, lib2, arraysource):
    # arraysource = ligne(input)
    index1 = 0
    index2 = 0
    countapplib1 = 0
    countapplib2 = 0
    similarity = 0

    for elem in arraysource[0]:
        if (elem == lib1):
            index1 = arraysource[0].index(elem)
            # print(index1)
        if (elem == lib2):
            index2 = arraysource[0].index(elem)

    for elem in arraysource:
        if (elem[index1] == elem[index2] and (elem[index1] == '1')):
            similarity = similarity + 1

        if (elem[index1] == '1'):
            countapplib1 = countapplib1 + 1

        if (elem[index2] == '1'):
            countapplib2 = countapplib2 + 1

    if(countapplib2 !=0 and countapplib1 != 0):
        lib1similarity = similarity / countapplib1
        lib2similarity = similarity / countapplib2
        usim = similarity / (countapplib2 + countapplib1 - similarity)
        average_similarity = (lib2similarity + lib1similarity) / 2
    else:
        usim=0
    return usim

# Return the library that have the max RecSocre ArraySource repesent data Source
def recScore(library, arraysource,LibGroundTruth):
    dataScore = arraysource
    score = []
    maxSimilarity = 0
    maxSimilaritylib = ''

    for elem in arraysource[0]:
        if ((elem != library) and (arraysource[0].index(elem) != 0) and elem in LibGroundTruth):
            tempMaxSimilarity = similarity(library, elem, dataScore)
            if (tempMaxSimilarity > maxSimilarity):
                maxSimilarity = tempMaxSimilarity
                maxSimilaritylib = elem
    # print(maxSimilaritylib)
    score.append(maxSimilarity)
    score.append(maxSimilaritylib)

    return score


def setlabel(point, data, label):
    for elem in data:
        if (elem[0] == point):
            elem[1] = label


def getlabel(point, data):
    for elem in data:
        if (elem[0] == point):
            return elem[1]


def neigbors(point, data, eps, arraysource):
    neighbors = []
    for elem in data:
        if (elem[0] != point):
            distance = 1 - (similarity(point, elem[0], arraysource))

            if (distance < eps):
                # print(elem[0])
                # elem[1]=1
                neighbors.append(elem[0])
            # print(distance)
    # print(arraypoint)
    # print(neighbors)
    return neighbors


def dbscan(arraysource, minpoint, epsilon):
    arraypoint = []
    C = 0
    # print(arraysource)
    for elem in arraysource[0]:
        if (arraysource[0].index(elem) != 0):
            arraypoint.append([elem, 0])

    # print(arraypoint)
    # print(len(arraypoint))
    for elem in arraypoint:

        # print(elem[0]+' est visite ================================================')
        if (elem[1] == 0):
            npoints = neigbors(elem[0], arraypoint, epsilon, arraysource)
            # print(elem[0] + ' est visite ***************'+ str(npoints)+'==='+ str(len(npoints))+ ' de voisin')

            if (len(npoints) < minpoint):
                elem[1] = -1

            else:
                C += 1
                i = 0
                elem[1] = C
                # fix code for elem
                while i < len(npoints):
                    pn = npoints[i]
                    thislabelph = getlabel(pn, arraypoint)
                    if (thislabelph == -1):
                        setlabel(pn, arraypoint, C)

                    elif (thislabelph == 0):
                        setlabel(pn, arraypoint, C)
                        # print(arraypoint)

                        pnneighborpts = neigbors(pn, arraypoint, epsilon, arraysource)
                        if (len(pnneighborpts) >= minpoint):
                            npoints = npoints + pnneighborpts
                    i += 1
    print(arraypoint)
    output = Cluster(arraypoint, C, C)
    return output


def relaxdbscan(arraysource, epsilon, minpoint, maxEpsilon):
    history = []
    pas = 0.1
    while (epsilon <= maxEpsilon):
        resultdbscan = dbscan(arraysource, minpoint, epsilon)
        history.append(resultdbscan.getarray())
        indextoremove = getindex(resultdbscan.getarray(), resultdbscan.getnbcluste())
        # print('cluster' + str(resultdbscan.getnbcluste()))
        print('element to remove' + str(indextoremove))
        arraysource = updateDB(arraysource, indextoremove)
        # print(arraysource)
        epsilon = epsilon + pas
        print('epsilon = ' + str(epsilon))
    # print(history)
    return resultdbscan.getarray()

    # while (epsilonn <1):
    #     relaxdbscan(arraysource,epsilonn,minpoint)


###### visualisationn#############


def child(name, value):
    temp = {"name": name, "value": value}
    return temp

    data["children"].append(temp)


# fonction flat array
def getAllClusters(resultdbscan, dictlibrary):
    # resultdbscan=[['f', -1], ['azde', -1], ['cmnukbgj', -1]]
    tempArrayofClusters = []

    ArrayofClusters = []
    for elem in resultdbscan:
        dataelem = dictlibrary.get(elem[0])
        if (isinstance(dataelem, list)):
            if (dataelem not in ArrayofClusters):
                ArrayofClusters.append(dataelem)
        else:
            tempArrayofClusters.append(dataelem)
        ### elenver les element qui ne sont pas clustered
        # ArrayofClusters.append(tempArrayofClusters)
        tempArrayofClusters = []
    # print("arrayofclusters")
    # print(ArrayofClusters)
    return ArrayofClusters


def souscluster(clusters):
    tempdataa = []

    # clusters = ['c', 'm', 'n', 'u', ['k', 'b', ['g', 'j']]]
    for elem in clusters:
        if not (isinstance(elem, list)):
            tempdataa.append(elem)
            # return data

        else:
            # dataa.append(tempdataa)
            tempelem = elem
            # print(elem)
            souscluster(tempelem)
        # print(tempdataa)
        if (tempdataa not in dataa):
            dataa.append(tempdataa)
    return dataa


#     # CREATION DES SOUS CLUSTER PERE FILS



def hiearchyCluster(childcluster):
    temp = 0
    for elem in childcluster:
        print('element for datcover')
        print(elem)
        datacover = {"name": "", "children": []}

        # print(elem)
        if (temp == 0):
            # print("temp egale a zero")
            # print(temp)
            temp = elem

        else:
            # print("yes")
            # print(elem["children"])
            # elem["children"].append(temp)
            datacover["children"].append(temp)
            # print('data cover')
            # print(datacover)
            # elem["children"].append(datacover)
            datacover["children"].append(elem)

            # temp = elem
            temp = datacover
            # print(temp)

    return temp


def superCluster(hiarchyCluster):
    # ENCERCLER  EACH CLUStER( ELEMENT IN CLUSETER)
    data = {"name": "", "children": []}
    data['children'].append(hiarchyCluster)
    return data


def subchildtwo(cluster):
    dataarray = []
    for array in cluster:
        data = {"name": "", "children": []}
        for elem in array:
            data['children'].append(child(elem, 555888 * Scoredictlibrary.get(elem)))
        dataarray.append(data)
    # print(dataarray)
    # print(len(dataarray))
    # reverse array
    return dataarray[::-1]


def geteachCluster(resultgetallclusters):
    for elem in resultgetallclusters:
        subdatajson.append(superCluster(hiearchyCluster(subchildtwo(souscluster(elem)))))
        # print("etat de data")
        # print(dataa)
        dataa.clear()
    return subdatajson


def globaljsonvisualisation(subdatajson):
    data = {"name": "", "children": []}
    for elem in subdatajson:
        data['children'].append(elem)
    return data


# def scoreLibrary():
#     TransposeArraysourceforscorelibrary = np.transpose(arraysourceforscorelibrary)
#     # print(TransposeArraysourceforscorelibrary)
#     TransposeArraysourceforscorelibrary = TransposeArraysourceforscorelibrary.tolist()
#     for lib in TransposeArraysourceforscorelibrary:
#         # print(TransposeArraysourceforscorelibrary.index(lib))
#         nbapp = 0
#         if not (TransposeArraysourceforscorelibrary.index(lib) == 0):
#
#             # print(lib)
#             for i in range(1, len(lib) - 1):
#                 if (lib[i] == '1'):
#                     nbapp = nbapp + 1
#             Scoredictlibrary[str(lib[0])] = nbapp / len(lib)
#     return Scoredictlibrary
# # fat the array of cluster for evaluation recall rate

def getlistofApp(arrayfold):
    TransposeArraysourceforscorelibrary = np.transpose(arrayfold)
    # print(TransposeArraysourceforscorelibrary)
    listapp = TransposeArraysourceforscorelibrary.tolist()
    return listapp[0]




def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
def listoflibbyApp(database,namelib,nameapp):

    for app in database:
        listlib=[]
        # indexofapp = database.index(app)
        if app[0] !='Applicatons/librairies':
            listallApp.append(app[0])
            for n in range(1,len(app)):
                if app[n] == '1':
                    listlib.append(namelib[n])
        dictlibraryinapp[app[0]] = listlib
    # print(dictlibraryinapp)


def slideGroundtruth(l):
    groundtruth = [l[i] for i in range(len(l)) if i % 2 == 1]

    # print(groundtruth)  # ['7072631', '7072687', '7072759', '7072783']
    return groundtruth


def slideValidation(l):
    validation = [l[i] for i in range(len(l)) if i % 2 == 0]
    # print(validation)  # ['7072624', '7072672', '7072752', '7072768']
    return validation
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False

def getUsefullPatterns(patterns,groundtruth):
    usefulPattern =[]
    for pattern in patterns:
        if(common_member(pattern,groundtruth)):
            usefulPattern.append(pattern)
    return usefulPattern

def listofPatterns(nestedcluster):
    listofPatterns=[]
    for elem in nestedcluster:
        if isinstance(elem, list):
            listofPatterns.append(flatten(elem))
    return listofPatterns

def lislibraryinusefulpatter(lispattern,groundtruth):
    removeGroundtruthUsefulLib = []
    flatlib = flatten(lispattern)
    for elem in  flatlib:
        # if not elem in  groundtruth:
            removeGroundtruthUsefulLib.append(elem)
    return removeGroundtruthUsefulLib

# Set Score for libarary in usefull pattern
def setdicRecScore(listlibuseful,data,groundtruth,):
    for libtoevaluate in listlibuseful:
        score = recScore(libtoevaluate,data,groundtruth)
        dictRecScore[libtoevaluate] =score[0]
    return dictRecScore


def getrecall(dicRecScore,topk):
    sort_orders = sorted(dicRecScore.items(), key=lambda x: x[1], reverse=True)
    # print(sort_orders)
    ranking =[]
    for rank in range(topk):
        if not(rank +1 > len(sort_orders)):
            ranking.append(sort_orders[rank][0])
        # print(sort_orders[rank][0])
    # print('top k element',ranking)
    return ranking
def getrecallrank(dicRecScore, validlist):
    sort_orders = sorted(dicRecScore.items(), key=lambda x: x[1], reverse=True)
    # print(sort_orders)
    ranking =[]
    for rank in range(len(sort_orders)):
        if(sort_orders[rank][0] in validlist):
            return (1/(rank+1))




def append_list_as_row(file_name, list_of_elem,header_csv=['file','app','iscorrect','topk','firstrankIscorrect']):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        if os.stat(file_name).st_size == 0:
            csv_writer.writerow(header_csv)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def testurn(listelem,list2):
    for elem in listelem:
        if(elem in list2):
            return elem



if __name__ == "__main__":

    for topfile in range(len(topnumber)):
        thistopk = topnumber[topfile]
        topkfilename = topkName[topfile]
        for listfilefold in range(len(namesfoldValidANDnamesfoldTraining)):
            fold = namesfoldValidANDnamesfoldTraining[listfilefold]
            # C = 0
            # index = [1, 2, 3]
            # fold ='samplesortie2.csv'
            # thistopk =1
            # topkfilename = "toptest3.csv"
            dataa = []
            subdatajson = []
            namelib =[]
            nameapp =[]
            # minpt = 5
            minpt = 5
            eps = 0
            maxEpsilon = 0.7
            # maxEpsilon = maxepsilonvariable/10
            epsilonStep = 0.1
            print('EDBSCAN')
            print('maxEpsilon : ' + str(maxEpsilon))
            print('epsilonStep :' + str(epsilonStep))
            print('minimum points :' + str(minpt))
            dictlibraryinapp ={}
            dictlibrary = {}
            Scoredictlibrary = {}

            file = 'ValidationFold/'+fold

            arraysource = ligne(file)
            arraysourc = ligne(file)
            arraysourceforrecscorelibrary = arraysource
            # data for evaluation recall rate
            listallApp = []
            listallLib = arraysourceforrecscorelibrary[0]

            # scoreLibrary()

            for elem in arraysourc[0]:
                if (arraysourc[0].index(elem) != 0):
                    dictlibrary[str(elem)] = elem

            nbrlibrary = len(arraysourc[0])
            nbrapplication = len(arraysourc)
            print('nombre de librairies: ' + str(nbrlibrary))
            print('nombre dapplications :' + str(nbrapplication))
            stringdataname = 'DatamaxEpsilon' + str(maxEpsilon) + 'epsilonStep' + str(epsilonStep) + 'minpoint' + str(
                minpt) + 'strnblibrairie' + str(nbrlibrary) + 'Date' + str(datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))
            print(stringdataname)
            resultdbscan = relaxdbscan(arraysourc, eps, minpt, maxEpsilon)

            print(resultdbscan)
            print( "list of all cluster")
            listofallclusters= getAllClusters(resultdbscan, dictlibrary)
            print(listofallclusters)



            # print('finished:' + stringdataname)



            listoflibbyApp(arraysourceforrecscorelibrary, listallLib, getlistofApp(arraysourceforrecscorelibrary))
            # for application  in listallApp:
            for application in  listallApp:
                dictRecScore = {}
                thisapp = application

                thisgroundTruthLib = slideGroundtruth(dictlibraryinapp.get(thisapp))
                # thisValidation = slideValidation(dictlibraryinapp.get(thisapp))
                thislistofflatCusters = listofPatterns(listofallclusters)
                thisusefulPattern = getUsefullPatterns(thislistofflatCusters,thisgroundTruthLib)
                thisflattenusefulPattern = flatten(thisusefulPattern)
                thislistlibusefulpattern = lislibraryinusefulpatter(thisflattenusefulPattern,thisgroundTruthLib)
                # test1= ['a','b','c']
                # tests = [['a','r'], ['e','k']]
                # print(thisusefulPattern)
                # print(thisflattenusefulPattern)
                # print(len(thisflattenusefulPattern))
                # print(thisgroundTruthLib)
                # print(len(thisgroundTruthLib))
                # print("list of useful",thislistlibusefulpattern)
                # print(len(thislistlibusefulpattern))
                setdicRecScore(thislistlibusefulpattern,arraysource,thisgroundTruthLib)
                # print(len(dictRecScore))


                list_topkLib = getrecall(dictRecScore,thistopk)

                if(common_member(thisgroundTruthLib,list_topkLib)):
                    thisrank =getrecallrank(dictRecScore, thisgroundTruthLib)
                    if(thisrank == None):
                        thisrank = 0
                    append_list_as_row(topkfilename,[fold,thisapp,1,thistopk,thisrank])
                else:
                    thisrank = getrecallrank(dictRecScore, thisgroundTruthLib)
                    if (thisrank == None):
                        thisrank = 0
                    append_list_as_row(topkfilename, [fold, thisapp, 0, thistopk,thisrank])
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===')
                print(thisapp)
                print('liste all ordoner de recommandation',
                      sorted(dictRecScore.items(), key=lambda x: x[1], reverse=True))
                print('$$list of top k ', list_topkLib)
                print('list pour groundthruth', thisgroundTruthLib)

                print("le rang trouve", thisrank)
                print(thisapp,common_member(thisgroundTruthLib, list_topkLib))
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===')


    # list1 =[8,0,9,7,4,8]
    # list2 = [1,2,3]
    # if(testurn(list1,list2) == None):
    #     print("oups")
    # else:
    #     (print(testurn(list1,list2)))









