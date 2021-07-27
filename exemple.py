import json
def child(name,value):
    temp= {"name": name, "value": value}
    return temp

    data["children"].append(temp)

# fonction flat array
def getAllClusters(resultdbscan,dictlibrary):
    # reslutdbscan=[['f', -1], ['azde', -1], ['cmnukbgj', -1]]
    tempArrayofClusters=[]

    ArrayofClusters=[]
    for elem in resultdbscan:
        dataelem = dictlibrary.get(elem[0])
        if(isinstance(dataelem,list)):
            ArrayofClusters.append(dataelem)
        else:
            tempArrayofClusters.append(dataelem)
            ArrayofClusters.append(tempArrayofClusters)
            
    return ArrayofClusters
            
            



def souscluster(clusters):
    tempdataa =[]

    # clusters = ['c', 'm', 'n', 'u', ['k', 'b', ['g', 'j']]]
    for elem in clusters:
        if not (isinstance(elem,list)):
            tempdataa.append(elem)
            # return data

        else:
            # dataa.append(tempdataa)
            tempelem = elem
            # print(elem)
            souscluster(tempelem)
        # print(tempdataa)
        if(tempdataa not in dataa):
            dataa.append(tempdataa)
    # print (dataa)
    return dataa
def hiearchyCluster(childcluster):
    temp = 0
    for elem in childcluster:
        datacover = {"name": "Library", "children": []}
        # print(elem)
        if(temp ==0):
            temp = elem
            # print(temp)

        else:
            # print("yes")
            # print(elem["children"])
            # old mettre chaque sous cluster dans leur bul elem["children"].append(temp)
            elem["children"].append(datacover['children'].append(temp))
            temp = elem
            # print(temp)

    return temp

def superCluster(hiarchyCluster):
    data = {"name": "name", "children": []}
    data['children'].append(hiarchyCluster)
    return data

def subchildtwo(cluster):
    dataarray =[]
    # datacover = {"name": "Library", "children": []}

    for array in cluster:
        data = {"name": "name", "children": []}
        for elem in array:
            data['children'].append(child(elem, 4888))
        # datacover['children'].append(data)
        dataarray.append(data)
    # print(dataarray)
    # print(len(dataarray))
    return dataarray[::-1]

def geteachCluster(resultgetallclusters):

    for elem in resultgetallclusters:
        subdatajson.append(superCluster(hiearchyCluster(subchildtwo(souscluster(elem)))))
        print(dataa)
        dataa.clear()
    return subdatajson



def globaljsonvisualisation(subdatajson):
    data = {"name": "name", "children": []}
    for elem in subdatajson:
        data['children'].append(elem)
    return data







if __name__ == '__main__':

    resultgetallclusters =[['f'], ['a', 'z', 'd', 'e'], ['c', 'm', 'n', 'u', ['k', 'b', 'g', 'j']]]
    reslutdbscan=[['f', -1], ['azde', -1], ['cmnukbgj', -1]]
    dictlibrary = {'k': 'k', 'b': 'b', 'c': 'c', 'a': 'a', 'z': 'z', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'j': 'j', 'm': 'm', 'n': 'n', 'u': 'u', 'azde': ['a', 'z', 'd', 'e'], 'kbgj': ['k', 'b', 'g', 'j'], 'cmnukbgj': ['c', 'm', 'n', 'u', ['k', 'b', 'g', 'j']]}
    subdatajson=[]
    dataa = []
    bigdata =[]
    a= {'name': 'name', 'children': [{'name': 'c', 'value': 4888}, {'name': 'm', 'value': 4888}, {'name': 'n', 'value': 4888}, {'name': 'u', 'value': 4888}]}
    childcluster= [{'name': 'name', 'children': [{'name': 'c', 'value': 4888}, {'name': 'm', 'value': 4888}, {'name': 'n', 'value': 4888}, {'name': 'u', 'value': 4888}]}, {'name': 'name', 'children': [{'name': 'k', 'value': 4888}, {'name': 'b', 'value': 4888}]}, {'name': 'name', 'children': [{'name': 'g', 'value': 4888}, {'name': 'j', 'value': 4888}]}, {'name': 'name', 'children': [{'name': 'd', 'value': 4888}]}, {'name': 'name', 'children': [{'name': 'i', 'value': 4888}]}]

    dataforjson= [['c', 'm', 'n', 'u'], ['k', 'b'], ['g', 'j'], ['d'], ['i','z']]
    # clusters=['c', 'm', 'n', 'u', ['k', 'b', ['g', 'j',['d',['i']]],'O'],'Z','K']
    clusters = ['e', 'option', 'add', ['a', 'z', 'd', 'zoom'], ['k', 'b', 'g', 'org-ksoap2', 'call']]
    cluster1 = [['k', 2], ['b', 2], ['c', -1], ['a', 1], ['z', 1], ['d', 1], ['e', 1], ['f', -1], ['g', 2], ['j', 2], ['m', -1], ['n', -1], ['u', -1]]
    newclusters1 = [[4, 5, 6, 7], [1, 2, 9, 10]]
    cluster2 = [['c', 1], ['f', -1], ['m', 1], ['n', 1], ['u', 1], ['a&z&d&e&', -1], ['k&b&g&j&', 1]]
    newclusters2 = [[1, 3, 4, 5, 7]]
    var = 6703
    name ="mylib"
    data = {"name": "Lib8", "value": 6703}
    subdata={"name": name, "children": [{"name": "Lib8", "value": 6703}]}
    data2 = {}
    # data['name'] = 'alexandre'
    # data['value'] =var
    data2['name'] = 'data'
    # print(data2)
    # data2['children'] = [{"name": name, "value": var}]
    # print(data2)
    # data2['children'].append(data)
    # print(data2)
    # data2['children'].append(subdata)
    # print(data2)
    # data2['children'] =25
    # print(data2)
    # data2 = {"name": "Libraryw", "children": []}
    # print(data2)

    # print( souscluster(['c', 'm', 'n', 'u', ['k', 'b', ['g', 'j'], ['t','u']]] ))
    # print(subchildtwo([['c', 'm', 'n', 'u'], ['k', 'b'], ['g', 'j']]))
#     print(hiearchyCluster([{'name': 'name', 'children': [{'name': 'g', 'value': 4888}, {'name': 'j', 'value': 4888}]}, {'name': 'name', 'children': [{'name': 'k', 'value': 4888}, {'name': 'b', 'value': 4888}]}, {'name': 'name', 'children': [{'name': 'c', 'value': 4888}, {'name': 'm', 'value': 4888}, {'name': 'n', 'value': 4888}, {'name': 'u', 'value': 4888}]}]
# ))

    # json_data = json.dumps(data)
    # print(data2)

    # json_data = json.dumps(data2 ,indent= 4)
    # print(json_data)

    # print("element")
    #
    # with open('data.json', 'w') as fp:
    #     json.dump(subdata, fp, indent=4)

    # subchild()

    # file = "01s.json"
    # with open(file,"r") as json_file:
    #     data= json.load(json_file)
    #     print(data)
    # subchildrenone()
    # print(souscluster(clusters))
    # print(hiearchyCluster(childcluster))
    # print(globaljsonvisualisation(geteachCluster(getAllClusters(reslutdbscan,dictlibrary))))
