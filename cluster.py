class Cluster:
    def __init__(self,array,noise,nbcluster):
        self.array = array
        self.noise = noise
        self.nbcluster = nbcluster

    def getarray(self):
        return self.array
    def getnoise(self):
        return self.noise
    def getnbcluste(self):
        return self.nbcluster
