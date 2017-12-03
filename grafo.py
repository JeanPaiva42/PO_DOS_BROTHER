
class Grafo:
    grafo = {}
    grafo['demanda'] = []
    grafo['edges'] = []
    def __init__(self, numNodes):
        nodeNum = numNodes
        for i in range(0, numNodes):
            self.grafo['demanda'].append(0)
        pass

    def getNode(self, id):
        for i in self.grafo:
            if i['edges'][0] == id:
                return i
        else:
            return None

    def getgrafo(self):
        return self.grafo
    #add node to the graph

    def addEdge(self, infoList):
        newtuple = (infoList[0], infoList[1],infoList[2],infoList[3],infoList[4])
        self.grafo['edges'].append(newtuple)

    def setDemandas(self, v):
        newV = v[1:]
        if self.grafo['demanda'][int(newV[0])] == 0:
            self.grafo['demanda'][int(newV[0])] = int(newV[1])






    def printGrafo(self):
        print(len(self.grafo['demanda']))
        print(len(self.grafo['demanda']))
        for i in self.grafo['edges']:
            print(i)
















