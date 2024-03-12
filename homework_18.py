from random import *


def common_elements():
    lst3, lst5 = [], []

    for _ in range(10):
        lst3.append(randrange(0, 31, 3))
        lst5.append(randrange(0, 31, 5))

    intersection = list(set(lst3) & set(lst5))

    return print(*intersection)


common_elements()
