import networkx as nx 
import matplotlib.pyplot as plt 
import bfs, sys

def khop_neighborhood(G, u, k):
    try:
        bfs_result = bfs.bfs(G, u, k)
        neighborhood_list = []
        for i in range(len(bfs_result)):
            neighborhood_list += bfs_result[i]
        khop_neighborhood_graph = nx.subgraph(G, neighborhood_list)
        nx.draw(khop_neighborhood_graph)
        plt.show()
    except:
        sys.exit("Invalid Input - KHopN")

def k_length_path(G, u, k):
    try:
        bfs_result = bfs.bfs(G, u, k)
        current_node = bfs_result[k-1][0]
        k_path = nx.null_graph()
        k_path.add_node(current_node)
        for i in range(k-2, -1, -1):
            current_neighbors = list(nx.neighbors(G, current_node))
            for node in bfs_result[i]:
                if(current_neighbors.count(node) == 1):
                    k_path.add_node(node)
                    k_path.add_edge(current_node, node)
                    current_node = node 
                    break
                else:
                    continue
        nx.draw(k_path)
        plt.show()
    except:
        sys.exit("Invalid Input - KLP")
        

# Create a tetrahedral graph and write it to a file  
# tet = nx.tetrahedral_graph()
# nx.write_adjlist(tet, "tet.txt")

# Read a graph from a file
tet = nx.read_adjlist("road-road-ad-list.txt")
# tet = nx.read_adjlist("tet.txt")
nx.freeze(tet)

# Show the nodes and edges in the graph 
# print("Nodes: " + str(tet.nodes))
# print("Edges: " + str(tet.edges))

# DEBUG ZONE 

# k_length_path(tet, '1', 4)

# khop_neighborhood(tet, '1', 2)

# bf = bfs.bfs(tet, '1', 2)
# print(bf)

# print(list(nx.neighbors(tet, "1")))

# nx.draw(tet)
# plt.show()