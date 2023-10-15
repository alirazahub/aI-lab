import math


class Node:
    def __init__(self, state, parent, actions, totalcost=0, huristic=0,):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.huristic = huristic
        self.totalcost = totalcost


huristic = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
}


# Define the graph
romanian_map = {
    "Arad": Node("Arad", None, [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)]),
    "Zerind": Node("Zerind", None, [("Arad", 75), ("Oradea", 71)]),
    "Oradea": Node("Oradea", None, [("Zerind", 71), ("Sibiu", 151)]),
    "Sibiu": Node(
        "Sibiu",
        None,
        [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    ),
    "Timisoara": Node("Timisoara", None, [("Arad", 118), ("Lugoj", 111)]),
    "Lugoj": Node("Lugoj", None, [("Timisoara", 111), ("Mehadia", 70)]),
    "Mehadia": Node("Mehadia", None, [("Lugoj", 70), ("Dobreta", 75)]),
    "Dobreta": Node("Dobreta", None, [("Mehadia", 75), ("Craiova", 120)]),
    "Craiova": Node(
        "Craiova", None, [("Dobreta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)]
    ),
    "Rimnicu Vilcea": Node(
        "Rimnicu Vilcea", None, [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)]
    ),
    "Fagaras": Node("Fagaras", None, [("Sibiu", 99), ("Bucharest", 211)]),
    "Pitesti": Node(
        "Pitesti", None, [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)]
    ),
    "Giurgiu": Node("Giurgiu", None, [("Bucharest", 90)]),
    "Bucharest": Node(
        "Bucharest",
        None,
        [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    ),
    "Urziceni": Node(
        "Urziceni", None, [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)]
    ),
    "Hirsova": Node("Hirsova", None, [("Urziceni", 98), ("Eforie", 86)]),
    "Eforie": Node("Eforie", None, [("Hirsova", 86)]),
    "Vaslui": Node("Vaslui", None, [("Urziceni", 142), ("Iasi", 92)]),
    "Iasi": Node("Iasi", None, [("Vaslui", 92), ("Neamt", 87)]),
    "Neamt": Node("Neamt", None, [("Iasi", 87)]),
}

start = "Arad"
goal = "Bucharest"


# add heuristic values
def addHeuristic(graph, heuristic):
    for node in graph.values():
        node.huristic = heuristic[node.state]
    return graph


def findMin(frontier):
    minV = math.inf
    node = ""
    for i in frontier:
        if frontier[i][1] < minV:
            minV = frontier[i][1]
            node = i
    return node


def actionSequence(graph, start, goal):
    solution = [(graph[goal].state, graph[goal].totalcost)]
    totalCost = graph[goal].totalcost
    current = goal
    while current != start:
        currentParent = graph[current].parent
        solution.append((graph[currentParent].state, graph[currentParent].totalcost))
        current = currentParent
    solution.reverse()
    return solution, totalCost


def aStar(graph, start, goal):
    frontier = {start: (None, 0 + graph[start].huristic)}
    explored = dict()

    while frontier:
        currentNode = findMin(frontier)
        del frontier[currentNode]

        if graph[currentNode].state == goal:
            return actionSequence(graph, start, goal)

        currentCost = graph[currentNode].totalcost

        explored[currentNode] = (
            graph[currentNode].parent,
            currentCost + graph[currentNode].huristic,
        )

        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalcost

            if child[0] in explored:
                if (
                    graph[child[0]].parent == currentNode
                    or child[0] == start
                    or explored[child[0]][1] <= currentCost + graph[child[0]].huristic
                ):
                    continue

            if child[0] not in frontier:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalcost = currentCost
                frontier[child[0]] = (
                    graph[child[0]].parent,
                    currentCost + graph[child[0]].huristic,
                )
            else:
                if frontier[child[0]][1] > currentCost + graph[child[0]].huristic:
                    graph[child[0]].parent = currentNode
                    graph[child[0]].totalcost = currentCost
                    frontier[child[0]] = (
                        currentNode,
                        currentCost + graph[child[0]].huristic,
                    )


# Add heuristic values to the graph
addHeuristic(romanian_map, huristic)

# Call the A* search algorithm
solution, cost = aStar(romanian_map, start, goal)


print(f"The path from {start} to {goal} is: \n {solution}")
print(f"The total Cost of reacing {goal } from {start} is: {cost}")