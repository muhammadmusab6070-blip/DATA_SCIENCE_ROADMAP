import heapq

def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    visited = set()
    expanded = 0

    while frontier:
        cost, node, path = heapq.heappop(frontier)
        expanded += 1
        print(node)

        if node == goal:
            return path, cost, expanded

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(
                    frontier,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return None, float('inf'), expanded


graph = {
    'S': {'A': 4, 'B': 2, 'C': 9},
    'A': {'S': 4, 'D': 5, 'E': 11},
    'B': {'S': 2, 'D': 8, 'F': 7},
    'C': {'S': 9, 'F': 2},
    'D': {'A': 5, 'B': 8, 'G': 6},
    'E': {'A': 11, 'G': 1},
    'F': {'B': 7, 'C': 2, 'G': 5},
    'G': {'D': 6, 'E': 1, 'F': 5}
}

path, cost, expanded = ucs(graph, 'S', 'G')

print("Path:", path)
print("Cost:", cost)
print("Nodes expanded:", expanded)