from collections import deque

def bfs_path(graph,start,goal):
    queue=deque([[start]])
    
    visited=set([start])
    
    while queue:
        path=queue.popleft()
        node=path[-1]
        
        if node==goal:
            return path
        
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path=list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None

graph={
       '0':['4'],
       '1':['4'],
       '2':['5'],
       '3':['5'],
       '4':['0','1','6'],
       '5':['2','3','6'],
       '6':['4','5','7'],
       '7':['6','8'],
       '8':['9','10'],
       '9':['8','11','12'],
       '10':['8','13','14'],
       '11':['9'],
       '12':['9'],
       '13':['10'],
       '14':['10'],
       }      

start_node='0'
goal_node='14'

path=bfs_path(graph, start_node, goal_node)

if path:
   print(f"Path From {start_node} to {goal_node}:{path}")
else:
    print(f" No Path Found from {start_node} to {goal_node}")      