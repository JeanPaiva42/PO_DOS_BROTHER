from gurobipy import *

from grafo import Grafo
grafo = None
#oi

#Leitura das instâncias
with open('INST3.txt', 'r') as f:
    
    grafo = Grafo(int(f.readline().split()[0]))
    for line in f:
        #Transformando os dados lidos em tuplas de float, criando as arestas e setando as demandas
        oi = line.split()
        oi= map(float,oi)
        if (len(oi) ==5):
            grafo.addEdge(oi)
        else:
            if(len(oi)==1):
                grafo.setDemandas(oi[0])
    grafo.setDemandas2()


'''As funções a seguir retornam índices das tuplas, significam respectivamente: nó de saída,
nó de chegada, capacidade, custo fixo e custo'''
def t(e):
    return e[0]
def h(e):
    return e[1]
def u(e):
    return e[2]
def c(e):
    return e[3]
def f(e):
    return e[4]

mod = Model('netflow')
'''Seta os dados de demanda e arestas'''
d, E = grafo.getDemanda(), grafo.getEdges()

m = len(E)
n= len(d)
e = grafo.getEdges()

'''Criação da variável y
Declarada como binária'''
y=[]

for j in range(0,m):
    y.append(mod.addVar(vtype=GRB.BINARY,name="y"))
'''Declaração da variável x'''
x=[]

for i in range(m):
    x.append(mod.addVar(name="x"))
'''Função objetivo. 
Sum dos y e dos custos das arestas do grafo mais o somatório dos custos fixo multiplicado pelo x'''

mod.setObjective(sum(c(e)*y[j] + f(e)*x[j] for j,e in enumerate(E)), GRB.MINIMIZE)

'''Restrição 1: Conservação de fluxo'''
for v in range(n):
    mod.addConstr(sum(x[j] for j,e in enumerate(E) if  h(e)==v)-sum(x[j] for j,e in enumerate(E) if  t(e)==v) == d[v])
'''Restrição 2: A quantidade do que pssa por x deve ser menor ou igual a capacidade da aresta'''
for j,e in enumerate(E):
    mod.addConstr(x[j] <= u(e)*y[j])

'''As seguintes linhas são: atualizar o modelo, depois otimizar'''
mod.update()
mod.optimize()


#Prints dos resultados
listaX=[]
listaY=[]

for v in mod.getVars():
    if(v.varName=='y'):
        listaY.append(v.x)
    else:
        listaX.append(v.x)

print('Obj: %g' % mod.objVal)

listaResult=[]
for i in range(0, len(listaY)):
    listaResult.append("Resultado: y"+str(listaY[i])+" x: "+str(listaX[i]))
print(listaResult)
