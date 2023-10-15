from queue import PriorityQueue


def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    parent = {}
    cost_so_far = {start: 0}

    while not queue.empty():
        _, current = queue.get()

        if current == goal:
            break  # Goal node found, exit the loop

        if current not in visited:
            visited.add(current)

            for neighbor, edge_cost in graph[current].items():
                new_cost = cost_so_far[current] + edge_cost

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost
                    queue.put((priority, neighbor))
                    parent[neighbor] = current

    path = []
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()

    return path, cost_so_far[goal]

romania = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Pitesti": 138, "Rimnicu Vilcea": 146},
    "Rimnicu Vilcea": {"Craiova": 146, "Pitesti": 97, "Sibiu": 80},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Rimnicu Vilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}

start_node = "Arad"  
goal_node = "Bucharest" 

path, total_cost = uniform_cost_search(romania, start_node, goal_node)

print("Path:", path)
print("Total Cost:", total_cost)
