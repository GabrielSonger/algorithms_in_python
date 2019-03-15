def is_power_of_two(num):
    if not isinstance(num, int):
        return False

    # bitwise addition on num's one's complement
    # if num is power of two, it will only have 1 bit 1, e.g 01000
    # and one's complement is 10111, result to zero

    return ((num & (num - 1)) == 0 or (-num & (-num - 1))) == 0 and num != 0


print (is_power_of_two(-2))
print (is_power_of_two(3))
print (is_power_of_two(0))
