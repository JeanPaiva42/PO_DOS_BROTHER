
class Grafo:
    nodeList = []
    def __init__(self):
        pass
    def getNode(self, id):
        for i in self.nodeList:
            if i['id'] == id:
                return i
        else:
            return None

    def getNodeList(self):
        return self.nodeList
    #add node to the graph
    def addNode(self, infoList):
        newNode = {}
        newNode['id'] = infoList[0]
        newNode['edges'] =[]
        edgeInfo = []
        edgeInfo.append(infoList[1])
        edgeInfo.append(infoList[2])
        edgeInfo.append(infoList[3])
        edgeInfo.append(infoList[4])
        newNode['edges'].append(edgeInfo)
        self.nodeList.append(newNode)

    #add info to a node, such as new edges, costs and all
    def addInfo(self,node,infoList):
        edgeInfo = []
        edgeInfo.append(infoList[1])
        edgeInfo.append(infoList[2])
        edgeInfo.append(infoList[3])
        edgeInfo.append(infoList[4])
        node['edges'].append(edgeInfo)

    def printGrafo(self):

        for i in self.nodeList:
            print(i)
