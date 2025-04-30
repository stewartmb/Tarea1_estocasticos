import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Definir los nodos (etiquetas de las columnas)
nodos = ["BF", "BM", "BL", "Es", "SL", "SM", "SF"]

# Definir la matriz de adyacencia (valores numéricos)
matriz = np.array([
    [0.000, 0.250, 0.050, 0.200, 0.250, 0.150, 0.100],
    [0.018, 0.146, 0.181, 0.205, 0.269, 0.158, 0.023],
    [0.012, 0.098, 0.210, 0.306, 0.283, 0.077, 0.014],
    [0.005, 0.053, 0.223, 0.334, 0.285, 0.092, 0.008],
    [0.007, 0.067, 0.211, 0.342, 0.283, 0.085, 0.005],
    [0.021, 0.119, 0.233, 0.269, 0.233, 0.119, 0.005],
    [0.048, 0.238, 0.286, 0.095, 0.190, 0.143, 0.000]
])

# Crear un grafo dirigido (pues la matriz no es simétrica)
G = nx.DiGraph()

# Añadir nodos
G.add_nodes_from(nodos)

# Añadir aristas con pesos (solo si el peso > 0)
for i in range(len(nodos)):
    for j in range(len(nodos)):
        peso = matriz[i, j]
        if peso > 0:
            G.add_edge(nodos[i], nodos[j], weight=peso)

# Dibujar el grafo
pos = nx.spring_layout(G, seed=42)  # Diseño para evitar superposiciones
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1000, 
        edge_color="gray", font_size=10, arrows=True)

# Añadir etiquetas a las aristas (pesos)
edge_labels = {(u, v): f"{d['weight']:.3f}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Grafo de la matriz de adyacencia")
plt.show()
