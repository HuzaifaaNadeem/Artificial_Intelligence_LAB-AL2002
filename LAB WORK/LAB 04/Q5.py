import heapq

graph = {
    'S': {'A': 3, 'B': 6},
    'A': {'D': 9, 'E': 8},
    'B': {'F': 12},
    'C': {'H': 7},
    'D': {},
    'E': {'I': 5},
    'F': {'K': 1},
    'G': {},
    'H': {},
    'I': {},
    'J': {},
    'K': {},
    'L': {},
    'M': {}
}

heuristic_values = {
    'S': 10,
    'A': 7,
    'B': 8,
    'C': 6,
    'D': 0,
    'E': 4,
    'F': 3,
    'G': 5,
    'H': 2,
    'I': 0,
    'J': 4,
    'K': 0,
    'L': 6,
    'M': 7
}

goal_nodes = ['D', 'I', 'K']


def best_first_multiple_goals(start_node, goals):

    remaining_goals = set(goals)
    overall_path = []
    current_start = start_node

    while remaining_goals:

        priority_queue = []
        heapq.heappush(priority_queue, (heuristic_values[current_start], current_start, [current_start]))

        visited_nodes = set()

        while priority_queue:

            h_value, current_node, path_so_far = heapq.heappop(priority_queue)

            if current_node in remaining_goals:
                print("Reached goal:", current_node)
                overall_path += path_so_far
                remaining_goals.remove(current_node)
                current_start = current_node
                break

            visited_nodes.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited_nodes:
                    heapq.heappush(
                        priority_queue,
                        (heuristic_values[neighbor], neighbor, path_so_far + [neighbor])
                    )

    return overall_path


final_path = best_first_multiple_goals('S', goal_nodes)

print()
print("Path covering all goals:", final_path)
