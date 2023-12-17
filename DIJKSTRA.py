import networkx as nx
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        
        if current_distance > distances[current_node]:
            continue
        
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


G = nx.DiGraph()


edges_with_weights = [
    ('A', 'B', 4), ('B', 'D', 2), ('A', 'C', 2),
    ('C', 'B', 1), ('B', 'C', 3), ('C', 'E', 5), ('E', 'D', 1),
    ('C', 'D', 4), ('B', 'E', 4)
]

G.add_weighted_edges_from(edges_with_weights)


start_node = 'A'
shortest_distances = dijkstra(G, start_node)


for node, distance in shortest_distances.items():
    print(f'Odległość od {start_node} do {node}: {distance}')
