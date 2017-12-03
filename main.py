from grafo import Grafo
grafo = None
#oi
with open('PO_DOS_BROTHER/c33.txt', 'r') as f:
    grafo = Grafo(int(f.readline().split()[0]))
    for line in f:
        oi = line.split()
        if len(oi) > 3:
            grafo.addEdge(oi)
        else:
            grafo.setDemandas(oi)



grafo.printGrafo()


