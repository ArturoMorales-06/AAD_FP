import networkx as nx 
import matplotlib.pyplot as plt 
import bfs  

# Create a tetrahedral graph and write it to a file  
# tet = nx.tetrahedral_graph()
# nx.write_adjlist(tet, "tet.txt")

# Read a graph from a file
# tet = nx.read_adjlist("road-road-ad-list.txt")
tet = nx.read_adjlist("tet.txt")
nx.freeze(tet)

# Show the nodes and edges in the graph 
# print("Nodes: " + str(tet.nodes))
# print("Edges: " + str(tet.edges))

# DEBUG ZONE 
bf = bfs.bfs(tet, '1', 10)
print(bf)

# print(list(nx.neighbors(tet, "1")))

# nx.draw(tet)
# plt.show()