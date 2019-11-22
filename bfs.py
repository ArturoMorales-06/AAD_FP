# Module that applies Breadth First Search 
# on a node "u" in a tree "G"
import networkx as nx 
import sys 

def bfs(G, u, k):
    try:
        Discovered = [u]
        Layer = [[u]]
        for i in range(k-1):
            temp_layer = []
            for node in Layer[i]:
                for neighbor in list(nx.neighbors(G,node)):
                    if (Discovered.count(neighbor) == 0):
                        Discovered.append(neighbor)
                        temp_layer.append(neighbor)
                    else:
                        continue
            if(len(temp_layer) == 0):
                sys.exit("There is no path with the provided length with " + u + " as one of its endpoints")
            else:
                Layer.append(temp_layer)
        return Layer  

    except:
        sys.exit("Invalid Input - BFS")
