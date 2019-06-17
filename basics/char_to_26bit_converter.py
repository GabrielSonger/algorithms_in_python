from functools import reduce 


def char_to_26(str_in):
    if not str_in:
        return None
    int_list = []
    for char in str_in:
        char_num = ord(char) - ord('a')
        if not 0<=char_num<=25:
            return 0
        int_list.append(char_num)
    
    # (ak+b)k + c = ak^2 +bk + c
    return reduce(lambda x,y:x*26+y, int_list)

instr='bcc'
print(char_to_26(instr))