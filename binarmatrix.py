import csv
def ligne(file, n, sep=","):
    f = open(file, "r")
    r = csv.reader(f, delimiter=sep)
    lignes = list(r)
    f.close()
    print(lignes)
    return lignes
def indexdict(arraysource,librsansdoublon,appname):
    for elem in arraysource:
        if (elem[0] == appname):
            app.append(librsansdoublon.index(elem[len(elem) - 1]))
        print()

    print(app)
    dictindice =dict()
    dictindice[appname] =app
    print(dictindice.get(appname))
    return dictindice


# Prepare data for CrossRec evaluation
def listOfProjectWriter(projects):
    with open('DataForCrossRec/'+'projects.txt', 'w',encoding='utf-8') as f:
        for projet in projects:
            f.write(projet+'\t'+'\n')

def dicthForPorjects(projects,datasource):
    print("")
    for project in projects:
        i =1
        j=2
        dependencies=[]
        for data in datasource:
            if(len(dependencies)==0):
                dependencies.append(project)
            if(data[0]==project):
                dependencies.append(data[1])
        print("dictproject",dependencies)
        with open('DataForCrossRec/'+'dicth_'+project, 'w', encoding='utf-8') as f, open('DataForCrossRec/'+'graph_'+project, 'w', encoding='utf-8') as g:
            for dependencie in dependencies:
                if(dependencie == project):
                    f.write(str(i) +'\t'+ dependencie+'\n')
                    i = i+1
                else:
                    f.write(str(i) + '\t' +'#DEP#'+ dependencie + '\n')
                    i = i + 1
                    g.write('1' + '#' + str(j) + '\n')
                    j = j + 1





if __name__ == "__main__":
   arraysource = ligne("echantillon.csv",5)
   print("datasource",arraysource)
   librs =[]
   apps = []
   arrayout = []
   dictindice = dict()
   for elem in arraysource:
       librs.append(elem[len(elem)-1])
       apps.append(elem[0])
# print(librs)
# print(apps)
librsansdoublon = (list(dict.fromkeys(librs)))
print("libsans doublon",librsansdoublon)
appsansdoublon = (list(dict.fromkeys(apps)))
print("app sans doublon",appsansdoublon)
app =[]

for elemt in appsansdoublon:
    app = []
    for elem in arraysource:
        if(elem[0] == elemt):
            app.append(librsansdoublon.index(elem[len(elem) - 1]))
    dictindice[elemt] = app
print(dictindice)

for elem in appsansdoublon:
    arrayelem =[]

    arrayelem.append(elem)
    for i in range(0,len(librsansdoublon)) :
        if(i in dictindice.get(elem)):
            arrayelem.append('1')
        else: arrayelem.append('0')
    arrayout.append(arrayelem)
print("resultat final",arrayout)

f = open('echantillonmatrix.csv', 'w')
librsansdoublon.insert(0,'Applicatons/libraries')
ligneEntete = ",".join(librsansdoublon) + "\n"
f.write(ligneEntete)
for valeur in arrayout:
     ligne = ",".join(valeur) + "\n"
     f.write(ligne)

f.close()

# listOfProjectWriter(appsansdoublon)
# dicthForPorjects(appsansdoublon,arraysource)

