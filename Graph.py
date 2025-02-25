from collections import deque, defaultdict

node_D2 = (-105, 0) # Depot 2
node_D1 = (105, 0) # Depot 1
node_A = (-30, 60)
node_B = (35, 90)
node_C = (-45, 150)
node_D = (40, 155)
collections_points = [node_A, node_B, node_C, node_D]
node_O = (0, 0) # Origin/Starting point

# Define the allowed movements on the grid
routes = {
    'y=30': [(-105, 30), (-30, 30), (0, 30), (105, 30)],
    'y=115': [(-105, 115), (0, 115), (35, 115), (105, 115)],
    'y=190': [(-105, 190), (0, 190), (40, 190), (105, 190)],
    'x=-105': [(-105, 0), (-105, 30), (-105, 115), (-105, 190)],
    'x=105': [(105, 0), (105, 30), (105, 115), (105, 190)],
    '(0,0)_to_(0,30)': [(0, 0), (0, 30)],
    '(-30,30)_to_(-30,60)': [(-30, 30), (-30, 60)],
    '(0,115)_to_(0,190)': [(0, 115), (0, 150), (0, 190)],
    '(35,90)_to_(35,115)': [(35, 90), (35, 115)],
    '(-45,150)_to_(0,150)': [(-45, 150), (0, 150)],
    '(40,190)_to_(40,155)': [(40, 190), (40, 155)]
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

def line_tracking():
    pass

def node_to_node(start, end, next):
    # distance = ((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5
    line_tracking()
    #reaches next node
    if (junction_left.value() == 1 or junction_right.value() == 1):
        if start[0]==next[0] or start[1]==next[1]:
            return
        if start[0] == end[0]:
            if start[1] < end[1]:
                if end[0] < next[0]:
                    turn_right()
                else:
                    turn_left()
            else:
                if end[0] > next[0]:
                    turn_right()
                else:
                    turn_left()
        else:
            if start[0] < end[0]:
                if end[1] > next[1]:
                    turn_right()
                else:
                    turn_left()
            else:
                if end[1] < next[1]:
                    turn_right()
                else:
                    turn_left()
    return 1
    

def collect(num):
    path = shortest_route(location, collections_points[num])
    for i in path:
        


print("Shortest path from", node_D2, "to", node_D, ":", shortest_route(node_D2, node_D))