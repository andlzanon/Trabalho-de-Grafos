import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def Prim(G, CopiaG, R):
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
    
    #Imprime a lista de predecessores    
    for key in Predecessor:
        print("predecessor de ", key, "é ", Predecessor[key])
    
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
    pos = nx.spring_layout(G2, k = 0.10, iterations=30) 
    nx.draw_networkx(G2, pos)
    plt.show()
    
        
# "Main" define um grafo e o chama a partir do data set
G = nx.Graph()
G =nx.read_weighted_edgelist('mulheres.txt')
nx.draw_networkx(G)
plt.show()
CopiaG = nx.Graph()
CopiaG = nx.read_weighted_edgelist('mulheres.txt')
nos = G.nodes()
R = nos[1]
print("raiz", R)
Prim(G, CopiaG, R)