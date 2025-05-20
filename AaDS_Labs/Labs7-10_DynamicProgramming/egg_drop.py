def min_guesses(max_floor: int, eggs: int) -> int:
    data = [[0] * (max_floor + 1) for _ in range(eggs + 1)] # [eggs][floors]

    for i in range(1, eggs + 1):
        data[i][1] = 1
        data[i][0] = 0

    for j in range(1, max_floor + 1):
        data[1][j] = j

    for i in range(2, eggs + 1):
        for j in range(2, max_floor + 1):
            data[i][j] = float('inf')
            for x in range(1, j+1):
                res = 1 + max(data[i-1][x-1], data[i][j-x])
                data[i][j] = min(data[i][j], res)

    return data[eggs][max_floor]