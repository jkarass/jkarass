import networkx as nx

def bellman_ford(graph, start):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    
    
    for _ in range(len(graph.nodes()) - 1):
        for u, v, weight in graph.edges(data=True):
            if distances[u] + weight['weight'] < distances[v]:
                distances[v] = distances[u] + weight['weight']
    
    
    for u, v, weight in graph.edges(data=True):
        if distances[u] + weight['weight'] < distances[v]:
            raise ValueError("Graf zawiera ujemny cykl")
    return distances


G = nx.DiGraph()

edges_with_weights = [
    ('A', 'B', 10), ('A', 'F', 8), ('F', 'E', 1),
    ('E', 'B', -4), ('E', 'D', -1), ('D', 'C', -2)
]

G.add_weighted_edges_from(edges_with_weights)

start_node = 'A'
shortest_distances = bellman_ford(G, start_node)

for node, distance in shortest_distances.items():
    print(f'Odległość od {start_node} do {node}: {distance}')
