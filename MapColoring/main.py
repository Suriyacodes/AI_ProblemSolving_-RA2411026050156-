def is_valid(node, color, assignment, graph):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack(assignment, graph, colors):
    if len(assignment) == len(graph):
        return assignment

    node = list(graph.keys())[len(assignment)]

    for color in colors:
        if is_valid(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(assignment, graph, colors)
            if result:
                return result
            del assignment[node]

    return None

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

colors = ["Red", "Green", "Blue"]

solution = backtrack({}, graph, colors)

if solution:
    print("Solution found:")
    for region in solution:
        print(region, "->", solution[region])
else:
    print("No solution exists")
