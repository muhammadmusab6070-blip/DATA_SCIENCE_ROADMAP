import heapq


def ucs(graph, start, goal):

    frontier = [(0, start, [start])]
    visited = set()
    expanded = 0

    while frontier:

        cost, node, path = heapq.heappop(frontier)
        expanded += 1

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


def greedy_best_first(graph, heuristics, start, goal):

    frontier = [(heuristics[start], start, [start])]
    visited = set()

    while frontier:

        h, node, path = heapq.heappop(frontier)

        print(node, "h =", h)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                heapq.heappush(
                    frontier,
                    (heuristics[neighbor], neighbor, path + [neighbor])
                )

    return None


graph = {
    'S': {'A': 3, 'B': 7, 'C': 6},
    'A': {'S': 3, 'D': 4, 'E': 9},
    'B': {'S': 7, 'D': 2, 'F': 5},
    'C': {'S': 6, 'F': 3},
    'D': {'A': 4, 'B': 2, 'G': 7},
    'E': {'A': 9, 'G': 2},
    'F': {'B': 5, 'C': 3, 'G': 4},
    'G': {'D': 7, 'E': 2, 'F': 4}
}


heuristics = {
    'S': 9,
    'A': 6,
    'B': 5,
    'C': 7,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}


greedy_path = greedy_best_first(
    graph,
    heuristics,
    'S',
    'G'
)

greedy_cost = sum(
    graph[a][b]
    for a, b in zip(greedy_path, greedy_path[1:])
)

print("Greedy path:", greedy_path)
print("Greedy true cost:", greedy_cost)


ucs_path, ucs_cost, _ = ucs(graph, 'S', 'G')

print("UCS path:", ucs_path)
print("UCS cost:", ucs_cost)


if greedy_cost == ucs_cost:

    print("Greedy matched the optimal cost")

else:

    print(
        "Greedy is",
        greedy_cost - ucs_cost,
        "units worse than optimal"
    )


