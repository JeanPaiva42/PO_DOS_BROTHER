
class Grafo:
    nodeList = []
    def __init__(self):
        pass
    def getNode(self, id):
        for i in self.nodeList:
            if i['edges'][0] == id:
                return i
        else:
            return None

    def getNodeList(self):
        return self.nodeList
    #add node to the graph
    def addNode(self, infoList):
        newNode = {}
        newNode['edges'] =[]
        edgeInfo = (infoList[0], infoList[1],infoList[2],infoList[3],infoList[4])
        newNode['edges'].append(edgeInfo)
        self.nodeList.append(newNode)

    #add info to a node, such as new edges, costs and all
    def addInfo(self,node,infoList):
        edgeInfo = (infoList[0], infoList[1], infoList[2], infoList[3], infoList[4])
        node['edges'].append(edgeInfo)

    def printGrafo(self):

        for i in self.nodeList:
            print(i)

    def inflow(self):
        mycts = m.addConstrs((quicksum(x[i, f, p] * y[i, f, p, t]
                                       for i in I for p in P[i, f]) <= z[f, t]
                              for f in F for t in T), "myconstraint")