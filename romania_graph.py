class node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.visited = False

graph = {

    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
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

class queue:

    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0
        self.visited = []

    def enqueue(self, item):
        self.queue.append(item)
        self.rear += 1

    def dequeue(self):
        self.front += 1
        return self.queue[self.front - 1]

    def isEmpty(self):
        return self.front == self.rear

    def printQueue(self):
        print(self.queue)


def bfs(graph, start, end):
    q = queue()
    q.enqueue(start)
    q.visited.append(start)
    while not q.isEmpty():
        node = q.dequeue()
        print(node, end=" ")
        if node == end:
            return True
        for adjacent in graph[node]:
            if adjacent not in q.visited:
                q.enqueue(adjacent)
                q.visited.append(adjacent)



print (bfs(graph, 'Arad', 'Bucharest'))

def dfs(graph, start, end):
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        print(node, end=" ")
        if node == end:
            return True
        for adjacent in graph[node]:
            stack.append(adjacent)

print (dfs(graph, 'Arad', 'Bucharest'))