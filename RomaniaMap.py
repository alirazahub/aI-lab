import math
class Node:
    def __init__(self, state, parent, actions, totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost


romania_Map = {
    "Arad": Node("Arad", None, [("Zerind",75), ("Sibiu",118), ("Timisoara",140)], 333),
    "Zerind": Node("Zerind", None, [("Arad",75), ("Oradea",71)], 146),
    "Oradea": Node("Oradea", None, [("Zerind",71), ("Sibiu",151)], 222),
    "Timisoara": Node("Timisoara", None, [("Arad",118), ("Lugoj",111)], 229),
    "Lugoj": Node("Lugoj", None, [("Timisoara",111), ("Mehadia",70)], 181),
    "Mehadia": Node("Mehadia", None, [("Lugoj",70), ("Drobeta",75)], 145),
    "Drobeta": Node("Drobeta", None, [("Mehadia",75), ("Craiova",120)], 195),
    "Craiova": Node("Craiova", None, [("Drobeta",120), ("Rimnicu Vilcea",146), ("Pitesti",138)], 404),
    "Rimnicu Vilcea": Node("Rimnicu Vilcea", None, [("Craiova",146), ("Pitesti",97), ("Sibiu",80)], 323),
    "Sibiu": Node("Sibiu", None, [("Arad",140), ("Oradea",151), ("Rimnicu Vilcea",80), ("Fagaras",99)], 470),
    "Fagaras": Node("Fagaras", None, [("Sibiu",99), ("Bucharest",211)], 310),
    "Pitesti": Node("Pitesti", None, [("Rimnicu Vilcea",97), ("Craiova",138), ("Bucharest",101)], 336),
    "Bucharest": Node("Bucharest", None, [("Fagaras",211), ("Pitesti",101), ("Giurgiu",90), ("Urziceni",85)], 487),
    "Giurgiu": Node("Giurgiu", None, [("Bucharest",90)], 90),
    "Urziceni": Node("Urziceni", None, [("Bucharest",85), ("Hirsova",98), ("Vaslui",142)], 325),
    "Hirsova": Node("Hirsova", None, [("Urziceni",98), ("Eforie",86)], 184),
    "Eforie": Node("Eforie", None, [("Hirsova",86)], 86),
    "Vaslui": Node("Vaslui", None, [("Urziceni",142), ("Iasi",92)], 234),
    "Iasi": Node("Iasi", None, [("Vaslui",92), ("Neamt",87)], 179),
    "Neamt": Node("Neamt", None, [("Iasi",87)], 87)
}





def actionSequence(graph, start, goal):
    solution = [goal]
    current = goal
    while current != start:
        currentParent = graph[current].parent
        solution.append(currentParent)
        current = currentParent
    solution.reverse()
    return solution



def BFS(graph, start, goal):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)

    while queue:
        current = queue.pop(0)
        if current == goal:
            return actionSequence(graph, start, goal)
        for neighbor in graph[current].actions:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                graph[neighbor].parent = current    

def DFS(graph, start, goal):
    stack = []
    visited = []
    stack.append(start)
    visited.append(start)

    while stack:
        current = stack.pop()
        if current == goal:
            return actionSequence(graph, start, goal)
        for neighbor in graph[current].actions:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.append(neighbor)
                graph[neighbor].parent = current


print(BFS(romania_Map, "Arad", "Bucharest"))
print(DFS(romania_Map, "Arad", "Bucharest"))


