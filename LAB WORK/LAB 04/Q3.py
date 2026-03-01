graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

def depth_limited_search(current_node, goal_node, depth_limit, path_so_far, visited_nodes):

    print("Visiting:", current_node, "Depth left:", depth_limit)

    if current_node == goal_node:
        return path_so_far

    if depth_limit == 0:
        return None

    visited_nodes.add(current_node)

    for neighbor in graph[current_node]:

        if neighbor not in visited_nodes:

            result = depth_limited_search(
                neighbor,
                goal_node,
                depth_limit - 1,
                path_so_far + [neighbor],
                visited_nodes
            )

            if result is not None:
                return result

    return None

def iterative_deepening_search(start_node, goal_node, max_depth):

    for depth in range(max_depth + 1):

        print()
        print("Trying depth:", depth)

        visited_nodes = set()

        result = depth_limited_search(
            start_node,
            goal_node,
            depth,
            [start_node],
            visited_nodes
        )

        if result is not None:
            print()
            print("Goal found at depth:", depth)
            return result

    return None

final_path = iterative_deepening_search('A', 'G', 5)

print()
print("Final Path:", final_path)
