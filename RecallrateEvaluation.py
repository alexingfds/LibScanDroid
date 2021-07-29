import os
from _csv import writer
from datetime import datetime


class RecallRateEvaluation:
    def __init__(self,fold,arraysource,maxepsilon,dictlibrary,resultofdbscan,minpoint,nbrlibrary,nbrapplication,stepepsilon):
        self.fold=fold
        self.arraysource = arraysource
        self.maxepsilon = maxepsilon
        self.dictlibrary = dictlibrary
        self.resultofdbscan =resultofdbscan
        self.minpoint =minpoint
        self.nbrlibrary = nbrlibrary
        self.nbrapplication = nbrapplication
        self.stepepsilon = stepepsilon



    def getPatternsForPCU(self):
        patternForPCU = []
        for pattern in self.resultofdbscan:
            thispattern = self.dictlibrary.get(pattern[0])

            if (isinstance(thispattern, list)):
                patternForPCU.append(thispattern)
                print(thispattern)
                print("not a pattern")
        return patternForPCU

    def puc(self,pattern):
        # result = ['a', 'z', 'd', 'y']
        result = flatten(pattern)
        print(result)
        listofIndex = []
        # list contenant le nombre de librairie utilisé par application
        NbrUseLibByApp = []
        NotnullAppUseLib = 0
        for elem in self.arraysource[0]:
            if (elem in result):
                index = self.arraysource[0].index(elem)
                listofIndex.append(index)

        for element in self.arraysource:
            if not (self.arraysource.index(element) == 0):
                NbrappUseLib = 0
                for indexlib in listofIndex:
                    if (element[indexlib] == '1'):
                        NbrappUseLib = NbrappUseLib + 1
                NbrUseLibByApp.append(NbrappUseLib)
                if not (NbrappUseLib == 0):
                    NotnullAppUseLib = NotnullAppUseLib + 1
            # print(NbrUseLibByApp)
            # print(NotnullAppUseLib)
        Sum = sum(NbrUseLibByApp)
        print(Sum)
        numerateur = Sum / len(result)
        PUC = numerateur / NotnullAppUseLib
        print('PUC==> ' + str(PUC))
        return PUC



    def averagePuc(self,listofpattern):
        AveragePuc = 0
        if (len(listofpattern) > 0):
            SumPuc = 0
            for elem in listofpattern:
                SumPuc = SumPuc + self.puc(elem)
            AveragePuc = SumPuc / (len(listofpattern))
            print('AveragePuc==> ' + str(AveragePuc))
            append_list_as_row('recallraterecordcrossvalidation.csv', [self.fold, self.maxepsilon, self.minpoint, self.nbrlibrary, self.nbrapplication,self.stepepsilon,len(listofpattern),str(AveragePuc),datetime.now()])
            log_result_dbscanc(self.resultofdbscan)
        return AveragePuc


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

def append_list_as_row(file_name, list_of_elem,header_csv=['foldname','maxepsilon','minpoint','nbrlibrary','nbrapplication','stepepsilon','nbrPattern','PUC','Datetime']):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        if os.stat(file_name).st_size == 0:
            csv_writer.writerow(header_csv)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def log_result_dbscanc(result):
    with open("logresultdbscanrecallrate.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(str(result))
        file_object.write("\n")
        file_object.write(str(datetime.now()))

        file_object.close()