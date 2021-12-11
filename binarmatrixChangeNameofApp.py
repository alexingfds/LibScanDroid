import csv
def ligne(file, n, sep=","):
    f = open(file, "r")
    r = csv.reader(f, delimiter=sep)
    lignes = list(r)
    f.close()
    # print(lignes)
    return lignes
def indexdict(arraysource,librsansdoublon,appname):
    for elem in arraysource:
        if (elem[0] == appname):
            app.append(librsansdoublon.index(elem[len(elem) - 1]))
        print()

    # print(app)
    dictindice =dict()
    dictindice[appname] =app
    # print(dictindice.get(appname))
    return dictindice


# Prepare data for CrossRec evaluation
def listOfProjectWriter(projects):
    with open('DataForCrossRec/'+'projects.txt', 'w',encoding='utf-8') as f:
        i=1
        for projet in projects:
            f.write('project'+str(i)+'\n')
            i=i+1

def dicthForPorjects(projects,datasource):
    print("")
    numproj=1
    for project in projects:

        i =1
        j=2
        dependencies=[]
        for data in datasource:
            if(len(dependencies)==0):
                dependencies.append('project'+str(numproj))
            if(data[0]==project):
                if(data[len(data)-1]==""):
                    dependencies.append(data[len(data)-2])
                else:
                    dependencies.append(data[len(data) - 1])
        # print("dictproject",dependencies)
        with open('DataForCrossRec/'+'dicth_'+'project'+str(numproj), 'w', encoding='utf-8') as f,open('DataForCrossRec/'+'graph_'+'project'+str(numproj), 'w', encoding='utf-8') as g:
            for dependencie in dependencies:
                if(dependencie == 'project'+str(numproj)):
                    f.write(str(i) +'\t'+ dependencie+'\n')
                    i = i+1
                else:
                    f.write(str(i) + '\t' +'#DEP#'+ dependencie + '\n')
                    i = i + 1
                    g.write('1' + '#' + str(j) + '\n')
                    j = j + 1
        numproj = numproj +1





if __name__ == "__main__":
   arraysource = ligne("Resources/GroundTruth.csv",5)
   # print("datasource",arraysource)
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
# print(dictindice)

for elem in appsansdoublon:
    arrayelem =[]

    arrayelem.append(elem)
    for i in range(0,len(librsansdoublon)) :
        if(i in dictindice.get(elem)):
            arrayelem.append('1')
        else: arrayelem.append('0')
    arrayout.append(arrayelem)
# print("resultat final",arrayout)

f = open('Resources/samplesortichangename.csv', 'w')
librsansdoublon.insert(0,'Applicatons/libraries')
ligneEntete = ",".join(librsansdoublon) + "\n"
f.write(ligneEntete)
projectNewName =1;
for valeur in arrayout:
     valeur[0]="project"+str(projectNewName)
     ligne = ",".join(valeur) + "\n"
     f.write(ligne)
     projectNewName= projectNewName +1

f.close()

# listOfProjectWriter(appsansdoublon)
# dicthForPorjects(appsansdoublon,arraysource)

