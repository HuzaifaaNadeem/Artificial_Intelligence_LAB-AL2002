graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

import heapq

def uniform_cost_search(start_node, goal_node):

    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node, [start_node]))

    visited_cost = {}

    while priority_queue:

        current_cost, current_node, path_so_far = heapq.heappop(priority_queue)

        if current_node == goal_node:
            return path_so_far, current_cost

        if current_node not in visited_cost or current_cost < visited_cost[current_node]:

            visited_cost[current_node] = current_cost

            for neighbor, edge_cost in graph[current_node].items():

                new_cost = current_cost + edge_cost

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor, path_so_far + [neighbor])
                )

    return None, float("inf")

least_cost_path, total_cost = uniform_cost_search('S', 'G')

print("Least Cost Path:", least_cost_path)
print("Total Cost:", total_cost)
