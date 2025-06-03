from typing import List, Tuple

def tsp_with_path(dist_mat: List[List[int]], start: int) -> Tuple[int, List[int]]:
    n = len(dist_mat)
    total_mask = (1 << n) - 1

    data = [[float('inf')] * n for _ in range(total_mask + 1)]
    parent = [[-1] * n for _ in range(total_mask + 1)]
    data[1 << start][start] = 0

    for mask in range(total_mask + 1):
        for i in range(n):
            if not (mask & (1 << i)): # Only with same bitmask
                continue

            for j in range(n):
                if mask & (1 << j): # Other bitmasks
                    continue

                if data[mask][i] != float('inf') and data[mask][i] + dist_mat[i][j] < data[mask | (1 << j)][j]:
                    data[mask | (1 << j)][j] = data[mask][i] + dist_mat[i][j]
                    parent[mask | (1 << j)][j] = i

    min_cost = float('inf')
    last_town = -1
    for i in range(n):
        if i == start:
            continue
        if data[total_mask][i] != float('inf') and data[total_mask][i] + dist_mat[i][start] < min_cost:
            min_cost = data[total_mask][i] + dist_mat[i][start]
            last_town = i

    path = []
    mask = total_mask
    current = last_town
    while current != -1:
        path.append(current)
        prev = parent[mask][current]
        mask ^= (1 << current)
        current = prev
    path.reverse()
    path.append(start)

    return min_cost, path
