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

    frontier = [(heuristics[start], start, [start], 0)]
    visited = set()
    expanded = 0

    while frontier:

        h, node, path, g = heapq.heappop(frontier)
        expanded += 1

        if node == goal:
            return path, g, expanded

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node].items():

            if neighbor not in visited:
                heapq.heappush(
                    frontier,
                    (
                        heuristics[neighbor],
                        neighbor,
                        path + [neighbor],
                        g + weight
                    )
                )

    return None, float('inf'), expanded


def astar(graph, heuristics, start, goal):

    frontier = [(heuristics[start], 0, start, [start])]
    best_g = {start: 0}
    expanded = 0

    while frontier:

        f, g, node, path = heapq.heappop(frontier)
        expanded += 1

        if node == goal:
            return path, g, expanded

        if g > best_g.get(node, float('inf')):
            continue

        for neighbor, weight in graph[node].items():

            new_g = g + weight

            if new_g < best_g.get(neighbor, float('inf')):

                best_g[neighbor] = new_g

                heapq.heappush(
                    frontier,
                    (
                        new_g + heuristics[neighbor],
                        new_g,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None, float('inf'), expanded


def compare_searches(graph, heuristics, start, goal):

    results = {}

    path, cost, expanded = ucs(graph, start, goal)
    results['UCS'] = (path, cost, expanded)

    path, cost, expanded = greedy_best_first(
        graph, heuristics, start, goal
    )
    results['Greedy'] = (path, cost, expanded)

    path, cost, expanded = astar(
        graph, heuristics, start, goal
    )
    results['A*'] = (path, cost, expanded)

    return results


graph = {
    'S': {'A': 2, 'B': 6},
    'A': {'S': 2, 'C': 3, 'D': 8},
    'B': {'S': 6, 'D': 2, 'E': 7},
    'C': {'A': 3, 'F': 5},
    'D': {'A': 8, 'B': 2, 'F': 1, 'G': 9},
    'E': {'B': 7, 'G': 3},
    'F': {'C': 5, 'D': 1, 'G': 4},
    'G': {'D': 9, 'E': 3, 'F': 4}
}


heuristics = {
    'S': 8,
    'A': 6,
    'B': 5,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 2,
    'G': 0
}


results = compare_searches(
    graph,
    heuristics,
    'S',
    'G'
)


print(f"{'Algorithm':<10}{'Path':<35}{'Cost':<8}{'Expanded':<10}")

for name, (path, cost, expanded) in results.items():

    print(
        f"{name:<10}{str(path):<35}"
        f"{cost:<8}{expanded:<10}"
    )