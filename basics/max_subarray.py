"""
Time complexity O(n)
If current sum is negative, there must be a sub array bigger than current sum, reset to 0

"""


def max_subarray(array):
    if not array or not isinstance(array, list):
        return None

    arr_len = len(array)
    max_sum = 0
    cur_sum = 0

    for num in array:

        cur_sum += num

        if cur_sum > max_sum:
            max_sum = cur_sum

        if cur_sum < 0:
            cur_sum = 0

    return max_sum




