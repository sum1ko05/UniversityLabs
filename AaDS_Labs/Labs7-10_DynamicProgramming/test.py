from subarray import largest_subarray
from money_exchange import exchange_money
from salesman import tsp_with_path
from egg_drop import min_guesses


if True:
    print(f"Largest subarray: {largest_subarray([2, -1, 2, -1, 2])}")
if True:
    print(f"Possible ways: {exchange_money([1, 2, 5], 100)}")
if True:
    dist_mat = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    min_cost, path = tsp_with_path(dist_mat, 0)

    print("The optimal route:", " -> ".join(map(str, path)))
    print(f"Minimal cost: {min_cost}")
if True:
    print(f"Minimal guesses: {min_guesses(100, 2)}") # You may remain max_floor at 100