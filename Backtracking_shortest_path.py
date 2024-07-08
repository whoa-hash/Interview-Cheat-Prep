# copyright Shira Reiss 2024

# Example grid
graph = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8],
        ]

# Valid to visit (prevents cycles)
def isValid(x, y):
   
    if x < 0 or y < 0 or x >= boundary or y >= boundary:
        return False
    
    if graph[x][y] in visited:
        return False
    
    return True

def backtrack(x, y, path=None):
    
    # starts off as None so we need to set it to add to it later on
    if path is None:
        path = [graph[x][y]]
        
    if graph[x][y] == end:
        # each path, not necessarily the shortest
        return path
    
    # no cycles
    visited.add(graph[x][y])
    
    # if you cannot reach the end, the shortest_path will return -1 (you can modify for other question definitions)
    shortest_path = -1
    # for each valid direction
    for j in range(4):
        new_x = delta_x[j] + x
        new_y = delta_y[j] + y

        # only use coordinates that are within the grid (can modify for other question definitions)
        if isValid(new_x, new_y):
            
            # add the new value to the path
            last_path = backtrack(x+delta_x[j],y+delta_y[j], path + [graph[new_x][new_y]])
            if shortest_path < 0:
                shortest_path = last_path
                
            # get shortest path
            elif last_path and len(last_path) < len(shortest_path):
                shortest_path = last_path
          
    # backtrack
    visited.remove(graph[x][y])

    # the value we want is the shortest path
    return shortest_path 

    
            
            



def main():
    global delta_x, delta_y, boundary, visited, end, graph # so we don't have to pass as parameters

    # To move down, right, left, up
    delta_x = [1, 0, 0, -1]
    delta_y = [0, 1, -1, 0]

    # start is the coordinate
    start = (0, 0)
    # value of where we want to end
    end = 17
    
    graph = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    # edge of the graph/grid
    boundary = len(graph) 
    # no cycles
    visited = set()
    
    # set variables
    x, y = start[0], start[1]
    
    ans = backtrack(x, y)
    print(ans)

main()
