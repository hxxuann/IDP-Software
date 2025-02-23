from collections import deque, defaultdict


node_D2 = (0, 0) # Depot 2
node_D1 = (4, 0) # Depot 1
node_A = (1, 0)
node_B = (3, 2)
node_C = (2, 3)
node_D = (3, 4)
node_O = (2, 0) # Origin/Starting point

# Define the allowed movements on the grid
routes = {
    'y=0': [(0, 0), (1, 0), (2, 0), (4, 0)],
    'y=2': [(0, 2), (2, 2), (3, 2), (4, 2)],
    'y=4': [(0, 4), (2, 4), (3, 4), (4, 4)],
    'x=0': [(0, 0), (0, 2), (0, 4)],
    'x=4': [(4, 0), (4, 2), (4, 4)],
    '(2,2)_to_(2,4)': [(2, 2), (2, 3), (2, 4)]
}

# Build graph
def build_graph():
    graph = defaultdict(list)
    for line in routes.values():
        for i in range(len(line) - 1):
            node1, node2 = line[i], line[i + 1]
            graph[node1].append(node2)
            graph[node2].append(node1)
    return graph

# Breath first search to find the shortest path
def bfs_path(graph, start, end):

    # Queue stores (current_node, path)
    queue = deque([(start, [start])])  
    # Set of visited nodes
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path  # Return the path if the end node is reached
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None  # If no path is found

# Find the shortest route
def shortest_route(A, B):
    graph = build_graph()
    if A not in graph or B not in graph:
        return "Invalid start or end node."
    return bfs_path(graph, A, B)


print("Shortest path from", node_D2, "to", node_D, ":", shortest_route(node_D2, node_D))