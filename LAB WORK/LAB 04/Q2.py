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

def depth_limited_search(current_node, goal_node, depth_limit, current_path, visited_nodes):

    print("Visiting:", current_node, "| Remaining Depth:", depth_limit)


    if current_node == goal_node:
        return current_path


    if depth_limit == 0:
        return None

    visited_nodes.add(current_node)


    for neighbor in graph[current_node]:

        if neighbor not in visited_nodes:

            result = depth_limited_search(
                neighbor,
                goal_node,
                depth_limit - 1,
                current_path + [neighbor],
                visited_nodes
            )

            if result is not None:
                return result

    return None

print("Running Depth-Limited Search with depth = 2")
print()

path_depth_2 = depth_limited_search(
    'A',
    'H',
    2,
    ['A'],
    set()
)

print()
print("Result Path:", path_depth_2)
print()
print("Running Depth-Limited Search with depth = 3")
print()

path_depth_3 = depth_limited_search(
    'A',
    'H',
    3,
    ['A'],
    set()
)
print()
print("Result Path:", path_depth_3)
