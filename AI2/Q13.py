import heapq


def astar(maze, start, goal):

    rows, cols = len(maze), len(maze[0])

    sr, sc = start
    gr, gc = goal

    if maze[sr][sc] == 1 or maze[gr][gc] == 1:
        return None, None

    def h(cell):
        r, c = cell
        return abs(r - gr) + abs(c - gc)

    def step_cost(cell):
        r, c = cell
        return 3 if maze[r][c] == 2 else 1

    frontier = [(h(start), 0, start, [start])]
    best_g = {start: 0}

    while frontier:

        f, g, node, path = heapq.heappop(frontier)

        if node == goal:
            return path, g

        if g > best_g.get(node, float('inf')):
            continue

        r, c = node

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):

            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and maze[nr][nc] != 1
            ):

                neighbor = (nr, nc)
                new_g = g + step_cost(neighbor)

                if new_g < best_g.get(neighbor, float('inf')):

                    best_g[neighbor] = new_g

                    heapq.heappush(
                        frontier,
                        (
                            new_g + h(neighbor),
                            new_g,
                            neighbor,
                            path + [neighbor]
                        )
                    )

    return None, None


maze = [
    [0, 0, 1, 0, 0, 2, 0],
    [0, 1, 1, 0, 1, 2, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 2, 0, 1],
    [0, 2, 2, 0, 0, 0, 0],
]


start = (0, 0)
goal = (6, 6)

path, cost = astar(maze, start, goal)

print("Path:", path)
print("Cost:", cost)