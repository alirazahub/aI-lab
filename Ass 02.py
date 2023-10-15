import math


class Node:
    def __init__(self, state, parent, actions, heuristic, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.heuristic = heuristic
        self.totalCost = totalCost


def findMin(frontier):
    minNode = None
    minCost = float("inf")
    for node, (parent, cost) in frontier.items():
        if cost < minCost:
            minNode = node
            minCost = cost
    return minNode


def actionSequence(graph, initialState, goalState):
    sequence = []
    currentNode = goalState
    # sequence.insert(0, initialState)
    while currentNode != initialState:
        parent = graph[currentNode].parent
        # sequence.insert(0, initialState)
        for action, _ in graph[parent].actions:
            if action == currentNode:
                sequence.insert(0, action)
                break
        currentNode = parent
    sequence.insert(0, initialState)
    return sequence


def solutionAstar(graph, initialState, goalState):
    frontier = {}
    explored = {}

    heuristicCost = math.sqrt(
        (graph[goalState].heuristic - graph[initialState].heuristic) ** 2
        # + (graph[goalState].heuristic[1] - graph[initialState].heuristic[1]) ** 2
    )

    frontier[initialState] = (None, heuristicCost)

    while frontier:
        currentNode = findMin(frontier)
        currentCost = frontier[currentNode][1]
        del frontier[currentNode]

        if currentNode == goalState:
            return actionSequence(graph, initialState, goalState)

        explored[currentNode] = (graph[currentNode].parent, currentCost)

        for child, actionCost in graph[currentNode].actions:
            childCost = currentCost + actionCost
            heuristicCost = math.sqrt(
                (graph[goalState].heuristic - graph[child].heuristic) ** 2
                # + (graph[goalState].heuristic[1] - graph[child].heuristic[1]) ** 2
            )

            if child in explored:
                if (
                    graph[child].parent == currentNode
                    or child == initialState
                    or explored[child][1] <= childCost + heuristicCost
                ):
                    continue

            if child not in frontier or childCost < frontier[child][1]:
                graph[child].parent = currentNode
                frontier[child] = (graph[child].parent, childCost + heuristicCost)

    return None  # No solution found


graph = {
        "Arad": Node("Arad", None, [("Sibiu",140),("Timisoara", 118),( "Zerind", 75)], 0, 366),
        "Bucharest": Node("Bucharest", None, [("Fagaras", 211), ("Giurgiu", 90), ("Pitesti", 101),( "Urziceni", 85)], 0, 0),
        "Craiova": Node("Craiova", None, [("Dobreta",120), ("Pitesti",138), ("Rimnicu Vilcea",146)], 0, 160),
        "Dobreta": Node("Dobreta", None, [("Craiova",120), ("Mehadia",75)], 0, 242),
        "Eforie": Node("Eforie", None, [("Hirsova", 86)], 0, 161),
        "Fagaras": Node("Fagaras", None, [("Bucharest",211), ("Sibiu", 99)], 0, 176),
        "Giurgiu": Node("Giurgiu", None, [("Bucharest", 90)], 0, 77),
        "Hirsova": Node("Hirsova", None, [("Eforie", 86),("Urziceni", 98)], 0, 151),
        "Iasi": Node("Iasi", None, [("Neamt", 870), ("Vaslui",92)], 0, 226),
        "Lugoj": Node("Lugoj", None, [("Mehadia",70), ("Timisoara",111)], 0, 244),
        "Mehadia": Node("Mehadia", None, [("Dobreta",75), ("Lugoj", 70)], 0, 241),
        "Neamt": Node("Neamt", None, [("Iasi", 87)], 234, 234),
        "Oradea": Node("Oradea", None, [("Sibiu", 151),("Zerind", 71)], 0, 380),
        "Pitesti": Node("Pitesti", None, [("Bucharest", 101), ("Craiova", 138), ("Rimnicu Vilcea", 97)], 0, 100),
        "Rimnicu Vilcea": Node("Rimnicu Vilcea", None, [("Craiova", 146),( "Pitesti", 97), ("Sibiu", 80)], 0, 193),
        "Sibiu": Node("Sibiu", None, [("Arad", 140), ("Fagaras",99),( "Oradea",151),("Rimnicu Vilcea", 80)], 0, 253),
        "Timisoara": Node("Timisoara", None, [("Arad", 118), ("Lugoj", 111)], 0, 329),
        "Urziceni": Node("Urziceni", None, [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)], 0, 80),
        "Vaslui": Node("Vaslui", None, [("Iasi",92), ("Urziceni",142)], 0, 199),
        "Zerind": Node("Zerind", None, [("Arad",75), ("Oradea",71)], 0, 374),
    }
initialState = "Arad"
goalState = "Bucharest"

solution = solutionAstar(graph, initialState, goalState)
print(solution)