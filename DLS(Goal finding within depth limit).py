def dls(graph,start,goal,dl):
    if dl<0:
        return None
    if start ==goal:
        return start
    
    for n in graph.get(start,[]):
        result=dls(graph, n, goal, dl -1)
        if result:
            return result
        
    return None

graph={
       'A':set(['B','C']),
       'B':set(['A','D','E']),
       'C':set(['A','F']),
       'D':set(['B']),
       'E':set(['B']),
       'F':set(['C'])
       }    

result=dls(graph,'A', 'F', 2)
if result:
    print("Goal Found",result)
else:
    print("Goal not Found Within Depth limit")
    