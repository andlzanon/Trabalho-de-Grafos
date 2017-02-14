import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt

def Prim(G):
    #raiz
    nos = G.nodes()
    R = nos[1]
    #init começa aqui
    #coloca peso de todas as arestas como infito
    for i in G.nodes():
        G.node[i]['peso'] = np.inf
    
    #exceto o no raiz que é setado como 0    
    G.node[R]['peso'] = 0
    #O Dicionário é a tabela de predecessores e é composto com (x:y) 
    #em que x é o vertice e y seu predecessor
    Predecessor = {}
    #seta predecessores de todos os vertices como 0 inicialmente
    for i in G.nodes():
        Predecessor[i] = None
    #init termina aqui
    
    #enquanto o numero de nos for maior que zero e utilizado pois toda a vez que
    #visitamos um vertice iremos removê-lo para exluir a necessidade de uma fila 
    #de visitados
    while G.number_of_nodes() > 0:
        #seta peso como infinito para achar o peso Mínimo, que inicialmente será R
        pesoMinimo = np.inf
        
        #Esse for é resposável por extrair o no de peso minimo
        for i in G.nodes():
            if G.node[i]['peso'] <= pesoMinimo:
                verticePesoMinimo = i
                pesoMinimo = G.node[i]['peso']
        
        #para todos os visinhos do no de peso minimo        
        for i in G.neighbors(verticePesoMinimo):
            #se o peso do no na fila de prioridades e maior do que o peso da aresta
            if G.node[i]['peso'] > G.get_edge_data(verticePesoMinimo, i)['weight']:
                #peso na fila de prioridade passa a ser o peso da aresta
                G.node[i]['peso'] = G.get_edge_data(verticePesoMinimo, i)['weight']
                #precessor desse vizinho é o vertice de peso minimo
                Predecessor[i] = verticePesoMinimo
        #remove, ou seja, já passou por ele na fila de visitados       
        G.remove_node(verticePesoMinimo)
    
    
    #vertice e aresta responsável pela construção da MST
    vertice = []
    arestas = []
    #vertices da MST sao todos os vertices de G, ou seja, todos os vertices da tabela 
    # de predecessores
    for key in Predecessor:
        vertice.append(key)
    
    #as arestas são as proprias atribuições do dicionario da tabela de predecessores     
    for key in Predecessor:
        arestas.append((key, Predecessor[key]))
    
    #desenha MST que e G2
    G2 = nx.Graph()
    G2.add_nodes_from(vertice)
    G2.add_edges_from(arestas)
    return G2

def twice_around(G, Copy):
    mst = Prim(G)
    digrafo = mst.to_directed()
    
    pos = nx.spring_layout(digrafo, k = 0.10, iterations=30) 
    nx.draw_networkx(digrafo, pos)
    plt.show()
    
    euler = nx.eulerian_circuit(digrafo,random.randint(0, 29))
    arestas = list(euler)

    peso = 0
    for i in arestas:
        if i[0] is not None and i[1] is not None: 
            peso += Copy.edge[i[0]][i[1]]['weight']


    caminho = []
    for i in list(arestas):
        if i[0] not in caminho:
            caminho.append(i[0])
        if i[1] not in caminho:
            caminho.append(i[1])
    return peso, caminho

f = open('circuito.txt','w')
for i in range(10):
    A = np.loadtxt('matriz.txt')
    G = nx.from_numpy_matrix(A)
    arestas = G.edges(data=True)
    
    pos = nx.spring_layout(G, k = 0.10, iterations=30) 
    nx.draw_networkx(G, pos)
    plt.show()
    
    Copy = nx.from_numpy_matrix(A)
    arestas = Copy.edges(data=True)
    
    peso, caminho = twice_around(G, Copy)
    print(peso)
    
    f.write("Caminho (" + str(i) + ") " + str(caminho) + "\nPeso: " + str(peso) + "\n")
f.close()