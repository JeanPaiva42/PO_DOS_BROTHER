'''A estrutura do grafo se baseia em um dicionário com dois campos:
um chamado 'demanda' que guarda uma lista de valores de demandas para os nós
e um outro que é o 'edges' '''
class Grafo:
    grafo = {}
    grafo['demanda'] = []
    grafo['edges'] = []
    nodeNum=0
    def __init__(self, numNodes):
        self.nodeNum = numNodes
        pass

    #Retorna grafo
    def getgrafo(self):
        return self.grafo

    #Adiciona arestas no grafo
    def addEdge(self, infoList):
        newtuple = (infoList[0], infoList[1],infoList[2],infoList[3],infoList[4])
        self.grafo['edges'].append(newtuple)

    #Adiciona as demandas
    def setDemandas(self, v):
        self.grafo['demanda'].append(v)

    #Seta as demandas de nós que não foram especificadas na instancia para 0
    def setDemandas2(self):
        tam=len(self.grafo['demanda'])
        for i in range(tam,self.nodeNum):
            self.grafo['demanda'].append(0)

    #Retorna arestas
    def getEdges(self):
        return self.grafo['edges']

    #Retorna a lista com as demandas dos nós
    def getDemanda(self):
        return self.grafo['demanda']

    #Printa grafo
    def printGrafo(self):
        print self.grafo['demanda']
        for i in self.grafo['edges']:
            print(str(i)+''+str(type(i)))
        for j in self.grafo['demanda']:
            print(str(j)+''+str(type(j)))


