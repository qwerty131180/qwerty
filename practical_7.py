# Experiment 7: BFS and DFS Traversal of a Graph
vertex=["A","B","C","D","E"]

matrix=[
    [0,1,1,0,0],
    [1,0,0,1,1],
    [1,0,0,1,0],
    [0,1,1,0,1],
    [0,1,0,1,0]    
]

visited=[False]*len(vertex)

def dfs(v):
    print(vertex[v],end=" ")
    visited[v]=True

    for i in range(len(vertex)):
        if matrix[v][i]==1 and visited[i]==False:
            dfs(i)

print("DFS Traversal:")
dfs(0)

graph={
      "A":["B","C"],
      "B":["A","D","E"],
      "C":["A","D"],
      "D":["B","C","E"],
      "E":["B","D"]  
}

visited=[]
queue=[]

def bfs(start):
    visited.append(start)
    queue.append(start)

    while queue:
        vertex=queue.pop(0)
        print(vertex,end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("\nBFS Traversal:")
bfs("A")
