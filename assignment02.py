import math


# This defines a class named Node that represents a node in a search graph. It has attributes like the current state, parent node, possible actions, total cost, and heuristic cost.
class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic

# This is a function that finds the node with the minimum cost in the frontier. It iterates through the nodes in the frontier dictionary and keeps track of the node with the minimum cost.
def findMin(frontier):
    minNode = None
    minCost = float("inf")
    for node, (parent, cost) in frontier.items():
        if cost < minCost:
            minNode = node
            minCost = cost
    return minNode

# This function is used to find the sequence of actions from the initialState to the goalState. It iterates backward from the goal state to the initial state, following the parent nodes and recording the actions in the sequence.
def actionSequence(graph, initialState, goalState):
    sequence = []
    currentNode = goalState
    while currentNode != initialState:
        parent = graph[currentNode].parent
        for action, _ in graph[parent].actions:
            if action == currentNode:
                sequence.insert(0, action)
                break
        currentNode = parent
    sequence.insert(0, initialState)
    return sequence


# This function implements the A* search algorithm. It initializes data structures for the frontier, explored nodes, and cost so far. It uses a dictionary to keep track of the cost to reach each state from the initial state.
def ASteric(graph, initialState, goalState):
    frontier = dict()
    explored = dict()
    totalCost = {initialState: 0}


# Here, it calculates the heuristic cost for the initial state to the goal state based on the Euclidean distance between their heuristic values. This is a common heuristic used in A* search.
    heuristicCost = math.sqrt(
        (graph[goalState].heuristic - graph[initialState].heuristic) ** 2
    )

    # The initial state is added to the frontier with a parent of None and the heuristic cost as its estimated total cost.
    frontier[initialState] = (None, heuristicCost)

# This is the main loop of the A* algorithm. It iterates while there are nodes in the frontier. It selects the node with the minimum estimated cost using the findMin function and removes it from the frontier.
    while frontier:
        currentNode = findMin(frontier)
        currentCost = totalCost[currentNode]
        del frontier[currentNode]

# If the current node is the goal state, it means the solution has been found. It then calls the actionSequence function to find the action sequence and returns it along with the total cost.

        if currentNode == goalState:
            sequence = actionSequence(graph, initialState, goalState)
            return sequence, currentCost
        
# The current node is added to the explored set with its parent and current cost.
        explored[currentNode] = (graph[currentNode].parent, currentCost)

# The code iterates through the possible actions from the current node and calculates the cost to reach each child node from the current node.
        for child, actionCost in graph[currentNode].actions:
            childCost = currentCost + actionCost

# If the child node is already in the totalCost dictionary, it checks if the new cost to reach it is less than the previously recorded cost. If it's not, it continues to the next child.
            if child in totalCost:
                if totalCost[child] <= childCost:
                    continue

# If the new cost to reach the child is less than the previously recorded cost, it updates the cost in the totalCost dictionary.
            totalCost[child] = childCost

# This calculates the heuristic cost for the child node using the same Euclidean distance heuristic as before.
            heuristicCost = math.sqrt(
                (graph[goalState].heuristic - graph[child].heuristic) ** 2
            )
# It checks if the child is already explored. If so, it continues to the next child if the conditions are met.
            if child in explored:
                if (
                    graph[child].parent == currentNode
                    or child == initialState
                    or explored[child][1] <= childCost + heuristicCost
                ):
                    continue

# If the child is not in the frontier or if the new cost is less than the cost recorded in the frontier, it updates the child's parent and estimated total cost in the frontier.
            if child not in frontier or childCost + heuristicCost < frontier[child][1]:
                graph[child].parent = currentNode
                frontier[child] = (graph[child].parent, childCost + heuristicCost)

# If the loop completes without finding a solution, it returns None to indicate that no path exists.
    return None


graph = {
        "Arad": Node("Arad", None, [("Sibiu",140),("Timisoara", 118),( "Zerind", 75)], 0, 366),
        "Bucharest": Node("Bucharest", None, [("Fagaras", 211), ("Giurgiu", 90), ("Pitesti", 101),( "Urziceni", 85)], 0, 0),
        "Craiova": Node("Craiova", None, [("Dobreta",120), ("Pitesti",138), ("Rimnicu Vilcea",146)], 0, 160),
        "Dobreta": Node("Dobreta", None, [("Craiova",120), ("Mehadia",75)], 0, 242),
        "Eforie": Node("Eforie", None, [("Hirsova", 86)], 0, 161),
        "Fagaras": Node("Fagaras", None, [("Bucharest",211), ("Sibiu", 99)], 0, 176),
        "Giurgiu": Node("Giurgiu", None, [("Bucharest", 90)], 77, 77),
        "Hirsova": Node("Hirsova", None, [("Eforie", 86),("Urziceni", 98)], 0, 151),
        "Iasi": Node("Iasi", None, [("Neamt", 870), ("Vaslui",92)], 0, 226),
        "Lugoj": Node("Lugoj", None, [("Mehadia",70), ("Timisoara",111)], 0, 244),
        "Mehadia": Node("Mehadia", None, [("Dobreta",75), ("Lugoj", 70)], 0, 241),
        "Neamt": Node("Neamt", None, [("Iasi", 87)], 0, 234),
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

path, cost = ASteric(graph, initialState, goalState)

print(f"The path from {initialState} to {goalState} is: \n {path}")
print(f"The total Cost of reacing {goalState } from {initialState} is: {cost}")