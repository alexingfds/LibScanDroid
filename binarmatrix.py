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

if __name__ == "__main__":
   arraysource = ligne("GroundTruth.csv",5)
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
print(librsansdoublon)
appsansdoublon = (list(dict.fromkeys(apps)))
print(appsansdoublon)
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
print(arrayout)

f = open('samplesortie1.csv', 'w')
librsansdoublon.insert(0,'Applicatons/libraries')
ligneEntete = ",".join(librsansdoublon) + "\n"
f.write(ligneEntete)
for valeur in arrayout:
     ligne = ",".join(valeur) + "\n"
     f.write(ligne)

f.close()