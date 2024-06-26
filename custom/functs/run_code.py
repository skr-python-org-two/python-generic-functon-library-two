import sys
from math_functs import s_add_square , s_sub_square

def __main__() :
    if len(sys.argv) > 1:
        print(s_add_square(int(sys.argv[1]) ,int(sys.argv[2])))
        print(s_add_square(int(sys.argv[1]) ,int(sys.argv[2])))
    else:
        print(s_add_square(5,6))
        print(s_add_square(7,8))


__main__()
