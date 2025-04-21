def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
        
        
    visited.add(start)
    print(start)


    for next in graph[start]-visited:
        dfs(graph, next,visited)
    return visited

graph={
      'A':set(['B','C','D']),
      'B':set(['A','E','F']),
      'C':set(['A','G']),
      'D':set(['A','H']),
      'E':set(['B','F']),
      'F':set(['B']),
      'G':set(['C']),
      'H':set(['D'])
       }    

dfs(graph,'A')