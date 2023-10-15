# graph2 = {
#     'A': ['C'],
#     'B': ['A'],
#     'C': [],
#     'D': ['B', 'C', 'E'],
#     'E': ['T', 'R'],
#     'F': ['G'],
#     'G': [],
#     'Q': [],
#     'R': ['F'],
#     'S': ['D','P', 'E'],
#     'T': ['Q'],
# }
# graph1 = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B', 'E'],
#     'E': ['B', 'D'],
#     'F': ['C'],
#     'G': ['C']
# }
# MAX = 5
# F = -1
# R = -1
# Q = [0] * MAX

# def EnQueue(value):
#     global F, R
#     if ((F == 0 and R == MAX-1) or (F == R + 1)):
#         print("\n--OverFlow--\n")
#     elif (F == -1 and R == -1):
#         F = 0
#         R = 0
#         Q[R] = value
#         print("\n--", value, "Inserted--\n")
#     elif (F != 0 and R == MAX-1):
#         R = 0
#         Q[R] = value
#         print("\n--", value, "Inserted--\n")
#     else:
#         R += 1
#         Q[R] = value
#         print("\n--", value, "Inserted--\n")

# def DeQueue():
#     global F, R
#     if (F == -1 and R == -1):
#         print("\n--UnderFlow--\n")
#         return -1
#     value = Q[F]
#     if (F == R):
#         F = -1
#         R = -1
#     elif (F == MAX-1):
#         F = 0
#     else:
#         F += 1
#     return value

# def PrintQueue():
#     global F, R
#     if (F == -1 and R == -1):
#         print("\n--Queue is Empty--\n")
#     elif (F <= R):
#         print("\nFollowing are the Elements Present in the Queue!")
#         for i in range(F, R+1):
#             print(Q[i])
#     else:
#         print("\nFollowing are the Elements Present in the Queue!")
#         for i in range(F, MAX):
#             print(Q[i])
#         for i in range(0, R+1):
#             print(Q[i])


# def bfs(graph, start):
#     visited = []
#     EnQueue(start)
#     visited.append(start)
#     while (F != -1 and R != -1):
#         current = DeQueue()
#         print(current, end=" ")
#         for neighbour in graph[current]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 EnQueue(neighbour)
#     print(visited)
    

# bfs(graph2, 'A')