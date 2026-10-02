def dls(tree, node, goal, limit, depth=0, path=None, log=None):

    if path is None:
        path = [node]

    if log is not None:
        log.append(node)

    print(f"depth {depth}: {node}")

    if node == goal:
        return path

    if depth == limit:
        return None

    for child in tree.get(node, []):
        result = dls(
            tree,
            child,
            goal,
            limit,
            depth + 1,
            path + [child],
            log
        )

        if result is not None:
            return result

    return None


def ids(tree, root, goal, max_limit):

    total_visits = 0

    for limit in range(max_limit + 1):

        log = []

        result = dls(
            tree,
            root,
            goal,
            limit,
            log=log
        )

        total_visits += len(log)

        if result is not None:
            return result, total_visits

    return None, total_visits


tree = {
    'Root': ['N1', 'N2', 'N3'],

    'N1': ['N4', 'N5'],
    'N2': ['N6', 'N7'],
    'N3': ['N8', 'N9'],

    'N4': [],
    'N5': [],
    'N6': [],

    'N7': ['N12', 'N15'],

    'N8': [],

    'N9': ['N13', 'N14'],

    'N12': [],
    'N13': [],
    'N14': [],

    'N15': ['GOAL', 'N16'],

    'GOAL': [],
    'N16': []
}


path, total_visits = ids(tree, 'Root', 'GOAL', 5)

print("Path:", path)
print("Total node visits:", total_visits)

print(
    "GOAL found at depth",
    len(path) - 1,
    "so limits 0 to",
    len(path) - 2,
    "were wasted iterations"
)