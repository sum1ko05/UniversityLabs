def max_value_backpack(max_weight: int, weights: list[int], values: list[int], n: int) -> int:
    data = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if weights[i - 1] <= w:
                data[i][w] = max(data[i - 1][w], 
                               data[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                data[i][w] = data[i - 1][w]
    
    return data[n][max_weight]
