import utime
from machine import Pin
from MOTOR import Motor
from colour_detector import pickup, dropoff, liftup
from config import line_left,line_right,junction_left,junction_right, led
location = (0, 0)

# line_left = Pin(13, Pin.IN)
# line_right = Pin(11, Pin.IN)
# junction_left = Pin(12, Pin.IN)
# junction_right = Pin(10, Pin.IN)

motor=Motor()
last_junction_time = utime.ticks_ms()

node_D2 = (-105, 0) # Depot 2
node_D1 = (105, 0) # Depot 1
node_A = (-30, 60)
node_B = (35, 90)
node_C = (-45, 150)
node_D = (40, 155)
collection_points = [node_A, node_B, node_C, node_D]
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
    graph = {}
    for line in routes.values():
        for i in range(len(line) - 1):
            node1, node2 = line[i], line[i + 1]
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)
    return graph

# Breath first search to find the shortest path
def bfs_path(graph, start, end):
    # Queue stores (current_node, path)
    queue = [(start, [start])]  
    # Set of visited nodes
    visited = set()

    while queue:
        # Pop the first element from the queue 
        current, path = queue.pop(0)
        if current == end:
            return path  # Return the path if the end node is reached
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    # Append the neighbor and the updated path to the queue
                    queue.append((neighbor, path + [neighbor]))
    return None  # If no path is found

# Find the shortest route
def shortest_route(A, B):
    graph = build_graph()
    if A not in graph or B not in graph:
        return "Invalid start or end node."
    return bfs_path(graph, A, B)

def line_tracking():
    # Movement control along a straight line
    global last_junction_time
    debounce_time = 200  # milliseconds
    while True:
        if line_left.value() == 1:
            motor.forward(0)
        elif line_right.value() == 1:
            motor.forward(1)
        else:
            motor.forward()
        
        if junction_left.value() == 1 or junction_right.value() == 1:
            current_time = utime.ticks_ms()
            if utime.ticks_diff(current_time, last_junction_time) >= debounce_time:
                last_junction_time = current_time
                return

def turn(diff):
    # Controls direction of turning
    if diff == 1:
        # Right Turn
        motor.right()
        utime.sleep(1.3)
        while line_left.value()==0:
            pass
        # Left pivot
        motor.left(0)
        utime.sleep(0.3)
        motor.off()
        return

    elif diff == 3:
        # Left Turn
        motor.left()
        utime.sleep(1.3)
        while line_right.value()==0:
            pass
        # Right pivot
        motor.right(0)
        utime.sleep(0.3)
        motor.off()
        return
    
    elif diff == 4:
        # Pivot 180 degrees right
        motor.pivot()
        utime.sleep(1.3)
        while line_left.value()==0:
            pass
        motor.off()
        return  
    elif diff == 5:
        # Pivot 180 degrees left
        motor.pivot(1)
        utime.sleep(1.3)
        while line_left.value()==0:
            pass
        motor.off()
        return  
        

    
def follow_path(path):

    def get_direction(p1, p2):
        # Helper function to get unit direction from p1 to p2
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx != 0:
            return (dx // abs(dx), 0)
        else:
            return (0, dy // abs(dy))

    # Assign index to direction: 
    direction_order = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_map = {d: idx for idx, d in enumerate(direction_order)}
    
    # Move to path[1] initially
    prev_dir = get_direction(path[0], path[1])
    line_tracking()
    global location
    location = path[1] 
    led.value(1)

    # Iterate over all points except the first one
    for i in range(1, len(path)):
        if i == len(path) - 2:
            # Last node
            current_dir = get_direction(path[i], path[i+1])
            
            prev_idx = direction_map[prev_dir]
            current_idx = direction_map[current_dir]
            diff = (current_idx - prev_idx) % 4
            
            turn(diff, last=True)
            motor.off()
            utime.sleep(0.2)
            location = path[-1]
            return

        # Movement for all nodes but last
        current_dir = get_direction(path[i], path[i+1])
        
        prev_idx = direction_map[prev_dir]
        current_idx = direction_map[current_dir]
        diff = (current_idx - prev_idx) % 4
        print(diff)
        turn(diff)
        
        line_tracking()
        location = path[i]
        prev_dir = current_dir

# Moves from current location to input location, picks up box and pivots 180 degrees
def collect(num):
    path = shortest_route(location, collection_points[num])
    print(path)
    follow_path(path)
    motor.reverse()
    utime.sleep(1)
    motor.off()
    # Picks up block
    color = pickup()

    # Pivot 180 degrees
    if collection_points[num] not in [node_B, node_D]:
        motor.reverse()
        utime.sleep(0.5)
    motor.off()
    turn(4)
    motor.reverse()
    utime.sleep(0.5)
    motor.off()
    
    return color

def deposit(color):
    # Determine destination and hence path
    if color in ['blue', 'green']:
        path = shortest_route(location, node_D1)
        dir=4
    elif color in ['yellow', 'red']:
        path = shortest_route(location, node_D2)
        dir=5
    else:
        print("Invalid color")
        return
    
    print(path)
    follow_path(path)
    motor.forward()
    utime.sleep(0.5)
    line_tracking()

    # Drop off block
    dropoff()

    # Turn 180 degrees
    motor.reverse()
    utime.sleep(0.5)
    turn(dir)
    liftup()

def return_home():
    # Move from current location to home
    path = shortest_route(location, node_O)
    follow_path(path)
    motor.forward()
    utime.sleep(1.3)
    motor.off()
    led.value(0)
