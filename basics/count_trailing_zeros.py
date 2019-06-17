def count_trailing_zeros(num):
    if num <= 0:
        return
    
    sum = 0

    for i in range(1, num+1):
        while i % 5 == 0:
            print(i)
            sum += 1
            i = i / 5
    
    return sum

print(count_trailing_zeros(20))