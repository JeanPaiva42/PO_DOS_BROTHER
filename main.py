from grafo import Grafo
grafo = Grafo()
with open('PO_DOS_BROTHER/c33.txt', 'r') as f:
    for line in f:
        lineData = line.split()[0:4]
        oi = grafo.getNode(lineData[0])
        if oi:
            grafo.addInfo(oi, lineData)
        else:
            grafo.addNode(lineData)


grafo.printGrafo()


