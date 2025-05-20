def largest_subarray(array: list) -> tuple[list, float]: # (subarray, max_sum)
    max_sum = float('-inf')
    sum = 0
    starting_index, ending_index = 0, 0

    for index, item in enumerate(array): # We have to keep track on indices
        sum += item
        if sum > max_sum:
            max_sum = sum
            ending_index = index
        if sum < 0: # This sum obviously can't be largest, we should reset sum and starting index
            sum = 0
            starting_index = index + 1 # Check this!

    if max_sum > 0:
        return (array[starting_index:ending_index + 1], max_sum)
    else:
        return ([max_sum], max_sum)