class Node:
    def __init__(self, state, parent, actions, cost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.cost = cost
def actionSquence(graph,initialState,globalState):
    solution = [globalState]
    currentParent = graph[globalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

def BFS():
    initialState = 'D'
    globalState = 'F'
    frontier = []
    explored = []
    graph = {
        'A': Node('A',None, ['B','C'],None),
        'B': Node('B',None, ['D', 'E'],None),
        'C': Node('C',None, ['A', 'F', 'G'],None),
        'D': Node('D',None, ['B', 'E'],None),
        'E': Node('E',None, ['B', 'D'],None),
        'F': Node('F',None, ['C'],None),
        'G': Node('G',None, ['C'],None),
    }

    frontier = [initialState]
    explored = []
    while len(frontier) != 0:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in explored and child not in frontier:
                graph[child].parent = currentNode
                if graph[child].state == globalState:
                    return actionSquence(graph,initialState,globalState)
                frontier.append(child)


BFS()