

def odd_existance_num_in_list(int_list):
    """
    k^k = 0, k^0 = k.
    xor each element in the list, the value will be the one exist odd times
    xor: (A and not B) or (not A and B)
    """
    if not int_list or not isinstance(int_list, list):
        return None

    # ^ on int is bitwise
    checker = 0

    for num in int_list:
        checker = checker ^ num

    return checker


a = [2, 3, 3, 4, 4, 2, 7, 7, 7]
print (odd_existance_num_in_list(a))
