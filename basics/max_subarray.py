"""
Time complexity O(n)
If current sum is negative, there must be a sub array bigger than current sum, reset to 0

"""

# O(N)
def max_subarray(array):
    if not array or not isinstance(array, list):
        return None

    max_sum = 0
    cur_sum = 0

    for num in array:

        cur_sum += num

        if cur_sum > max_sum:
            max_sum = cur_sum

        if cur_sum < 0:
            cur_sum = 0

    return max_sum

# O(N^2)
def max_subarray_iteration(array):
    if not isinstance(array, list):
        return None
    max_sum = 0
    this_sum = 0
    array_len = len(array)

    for i in range(array_len):
        this_sum = 0
        for j in range(i, array_len - 1, 1):
            this_sum += array[j]

            if this_sum > max_sum:
                max_sum = this_sum

    return max_sum

test_array = [-1, 2, -3, 5, 15, -20]
result = max_subarray_iteration(test_array)
print(result)

