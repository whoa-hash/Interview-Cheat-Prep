# @copyright Shira_Reiss 2024

from collections import defaultdict

# sample problem
# order is abfdelc - b is after/dependent on a, e is after/dependent on f
classes = [('a', 'b'),('f', 'e'), ('d', 'l'), ('f', 'd'), ('f', 'l'), ('b', 'c'), ('b', 'f'), ('e', 'l')]

# Create graph class as a dictionary of type list i.e. {'a':['b']}
class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, n, n2):
        self.graph[n].append(n2)

def helper(key, graph,visited, res):
    # Dependencies
    neighbors = graph.get(key)
    # There might be no such key
    if neighbors:
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                # Recurse until you find no dependencies - which will add to our output first
                helper(neighbor,graph, visited, res)

    # Add the key to the beginning of the list - we'll get the list in the correct order
    res.insert(0, key)

def top_sort(graph):
    res = []
    visited = set()

    # Go through each key
    for key in graph.keys():
        # If it's not already in our 'ouput', add it
        if key not in visited:
            visited.add(key)
            # DFS on the key to find the order
            helper(key, graph,visited, res)

    return res              

def main():
    # Instantiate variables
    classes = [("Comp101", "Advanced Eng"),("Comp101", "Calc1"), ("Calc1", "Speech2"),("Calc1", "Calc2"), ("Speech101", "Speech2"), ("Comp101", "Calc2"), ("Comp101", "Speech2")]
    graph = Graph()
    for tuple_pair  in classes:
        graph.add_edge(tuple_pair[0], tuple_pair[1]) 

    # Output 
    print("Graph",graph.graph)
    print("Answer",top_sort(graph.graph))

main()

    

    