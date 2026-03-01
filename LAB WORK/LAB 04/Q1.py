from collections import deque

building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

rows = len(building)
cols = len(building[0])

def create_graph_from_grid(grid):
    graph = {}

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 1:
                neighbors = []

                possible_moves = [
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1)
                ]

                for new_r, new_c in possible_moves:
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if grid[new_r][new_c] == 1:
                            neighbors.append((new_r, new_c))

                graph[(r, c)] = neighbors

    return graph


building_graph = create_graph_from_grid(building)

print("Adjacency List Representation:")
print()
for node in building_graph:
    print(node, "->", building_graph[node])
