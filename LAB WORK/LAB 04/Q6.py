import heapq

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {
    'A': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}

def astar(start, goal):

    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    g_cost = {start: 0}
    parent = {}

    while open_list:

        f, current = heapq.heappop(open_list)

        print("Visiting node:", current)

        if current == goal:
            print("Goal reached!")
            return reconstruct_path(parent, goal), g_cost[goal]

        for neighbor, cost in graph[current].items():

            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (new_f, neighbor))

                print("Updated:", neighbor,
                      "g =", new_g,
                      "f =", new_f)

    return None, float("inf")


def reconstruct_path(parent, node):
    path = [node]
    while node in parent:
        node = parent[node]
        path.append(node)
    path.reverse()
    return path


def update_edge(u, v, new_cost):
    print()
    print("Edge cost changed:", u, "-", v,
          "-> New cost:", new_cost)

    graph[u][v] = new_cost


print("Initial A* Search")

path, cost = astar('A', 'G')

print()
print("Best Path:", path)
print("Total Cost:", cost)

update_edge('A', 'B', 8)
update_edge('B', 'E', 7)

print()
print("Recomputing after cost changes...")

path, cost = astar('A', 'G')

print()
print("New Best Path:", path)
print("New Total Cost:", cost)
