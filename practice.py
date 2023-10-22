import math
class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

def findMinCost(graph, frontier):
    minCost = math.inf
    minNode = None
    for node in frontier:
        if graph[node].totalCost < minCost:
            minCost = graph[node].totalCost
            minNode = node
    return minNode

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution
    
def bfs(graph, initialState, goalState):
    frontier = [initialState]
    explored = []
    while len(frontier) != 0:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in explored and child not in frontier:
                graph[child].parent = currentNode
                if graph[child].state == goalState:
                    return actionSequence(graph, initialState, goalState)
                frontier.append(child)


def dfs(graph, initialState, goalState):
    frontier = [initialState]
    explored = []
    while len(frontier) != 0:
        currentNode = frontier.pop()
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in explored and child not in frontier:
                graph[child].parent = currentNode
                if graph[child].state == goalState:
                    return actionSequence(graph, initialState, goalState)
                frontier.append(child)

def ucs(graph, initialState, goalState):
    frontier = dict()
    explored = []
    frontier[initialState] = (None, 0)
    while len(frontier) != 0:
        currentNode = findMinCost(graph, frontier)
        del frontier[currentNode]
        if currentNode == goalState:
            return actionSequence(graph, initialState, goalState)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            currentCost = graph[currentNode].totalCost + child[1]
            if child[0] not in explored and child[0] not in frontier:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
            elif child[0] in frontier:
                if frontier[child[0]][1] < currentCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]
                    frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
                else:
                    frontier[child[0]] = (currentNode, currentCost)
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]


graph1 = {
        "A": Node("A", None, ["B", "C","E"], None),
        "B": Node("B", None, ["A","D", "E"], None),
        "C": Node("C", None, ["A","F","G"], None),
        "D": Node("D", None, ["B","E"], None),
        "E": Node("E", None, ["A","B","D"], None),
        "F": Node("F", None, ["C"], None),
        "G": Node("G", None, ["C"], None)
    }
graph2 = {
    "Arad": Node("Arad", None, ["Zerind", "Timisoara","Sibiu"], None),
    "Zerind": Node("Zerind", None, ["Arad","Oradea"], None),
    "Timisoara": Node("Timisoara", None, ["Arad","Lugoj"], None),
    "Sibiu": Node("Sibiu", None, ["Arad","Oradea","Fagaras","Rimnicu Vilcea"], None),
    "Oradea": Node("Oradea", None, ["Zerind","Sibiu"], None),
    "Lugoj": Node("Lugoj", None, ["Timisoara","Mehadia"], None),
    "Fagaras": Node("Fagaras", None, ["Sibiu","Bucharest"], None),
    "Rimnicu Vilcea": Node("Rimnicu Vilcea", None, ["Sibiu","Pitesti","Craiova"], None),
    "Mehadia": Node("Mehadia", None, ["Lugoj","Dobreta"], None),
    "Bucharest": Node("Bucharest", None, ["Fagaras","Pitesti","Giurgiu","Urziceni"], None),
    "Pitesti": Node("Pitesti", None, ["Rimnicu Vilcea","Bucharest","Craiova"], None),
    "Craiova": Node("Craiova", None, ["Rimnicu Vilcea","Pitesti","Dobreta"], None),
    "Dobreta": Node("Dobreta", None, ["Mehadia","Craiova"], None),
    "Giurgiu": Node("Giurgiu", None, ["Bucharest"], None),
    "Urziceni": Node("Urziceni", None, ["Bucharest","Hirsova","Vaslui"], None),
    "Hirsova": Node("Hirsova", None, ["Urziceni","Eforie"], None),
    "Vaslui": Node("Vaslui", None, ["Urziceni","Iasi"], None),
    "Eforie": Node("Eforie", None, ["Hirsova"], None),
    "Iasi": Node("Iasi", None, ["Vaslui","Neamt"], None),
    "Neamt": Node("Neamt", None, ["Iasi"], None)
}
graph3 = {
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

print(bfs(graph2, "Arad", "Bucharest"))
print(dfs(graph2, "Arad", "Bucharest"))
print(ucs(graph3, "Arad", "Bucharest"))