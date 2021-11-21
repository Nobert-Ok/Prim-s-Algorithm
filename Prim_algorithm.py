# Prim's Algorithm in Python

# number of vertices in graph
v = 7

# adjacency matrix representing edges and vertices of the graph
graph = [[0,28,0,0,0,10,0],
    [28,0,16,0,0,0,14],
    [0,16,0,12,0,0,0],
    [0,0,12,0,22,0,18],
    [0,0,0,22,0,25,24],
    [10,0,0,0,25,0,0],
    [0,14,0,18,24,0,0]]
    

# create to check visited edges vertex
visited = [0, 0, 0, 0, 0, 0 ,0]

# initializing the number of edge
no_edge = 0

# setting the 0th index to True
visited[0] = True

while (no_edge < v - 1):
    # initializing the variables
    minimum = float("inf")
    x = 0
    y = 0
    # looping through every vertex in the graph
    for i in range(v):
        if visited[i]:
            # looping through all the adjacent vertices connected to
            # the selected vertex above
            for j in range(v):
                if ((not visited[j]) and graph[i][j]):  
                    # not in selected and there is an edge
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j
    print(str(x+1) + "-->" + str(y+1) + ":" + str(graph[x][y]))
    # setting the visited vertex to true
    visited[y] = True
    # incrementing the number of edges
    no_edge += 1
    
    
