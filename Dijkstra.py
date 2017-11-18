import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def Dijkstra(G, CopiaG, R1, R2, R3):
    
    for i in G.nodes():
        G.node[i]['peso'] = np.inf
        
    G.node[R1]['peso'] = 0
    #G.node[R2]['peso'] = 0
    #G.node[R3]['peso'] = 0
    Predecessor = {}
    for i in G.nodes():
        Predecessor[i] = None
    
    while G.number_of_nodes() > 0:
        pesoMinimo = np.inf
        
        for i in G.nodes():
            if G.node[i]['peso'] <= pesoMinimo:
                verticePesoMinimo = i
                pesoMinimo = G.node[i]['peso']
                
        for i in G.neighbors(verticePesoMinimo):
            if G.node[i]['peso']>G.get_edge_data(verticePesoMinimo, i)['weight']+G.node[verticePesoMinimo]['peso']:
                G.node[i]['peso'] =G.get_edge_data(verticePesoMinimo, i)['weight']+G.node[verticePesoMinimo]['peso']
                Predecessor[i] = verticePesoMinimo
                
        G.remove_node(verticePesoMinimo)
        
    for key in Predecessor:
        print("predecessor de ", key, "e = ", Predecessor[key])
    
    vertice = []
    arestas = []
    for key in Predecessor:
        vertice.append(key)
        
    for key in Predecessor:
        arestas.append((key, Predecessor[key]))
    
    G2 = nx.Graph()
    G2.add_nodes_from(vertice)
    G2.add_edges_from(arestas)
    pos = nx.spring_layout(G2, k = 0.10, iterations=30) 
    nx.draw_networkx(G2, pos)
    plt.show()
    
        

G = nx.Graph()
L = [('s','c', {'weight': 15}), ('s','a', {'weight': 18}), ('c','a', {'weight': 2}), ('a','b', {'weight': 9}), ('c','b', {'weight': 14}),
    ('c','d', {'weight': 7}), ('b','d', {'weight': 10}), ('d','t', {'weight': 36}), ('b','t', {'weight': 28})]

G.add_edges_from(L)
pos = nx.spring_layout(G, k = 1, iterations=30) 
nx.draw_networkx(G, pos)
plt.show()
CopiaG = nx.Graph()
CopiaG = G
nos = G.nodes();
R1 = nos[0]
R2 = nos[1]
R3 = nos[2]
Dijkstra(G, CopiaG, R1, R2, R3)

#G =nx.read_weighted_edgelist('mulheres.txt')
#CopiaG = nx.Graph()
#CopiaG = nx.read_weighted_edgelist('mulheres.txt')
#nos = G.nodes()
#R1 = nos[0]
#R2 = nos[1]
#R3 = nos[2]
#print("raiz 1", R1)
#print("raiz 2", R2)
#print("raiz 3", R3)
#Dijkstra(G, CopiaG, R1, R2, R3)