from random import *


def common_elements():
    lst3, lst5 = [], []
    f_list =  []

    for _ in range(10):
        lst3.append(randrange(0, 31, 3))
        lst5.append(randrange(0, 31, 5))

    for i in range(len(lst3)):
        for j in range(len(lst5)):
            if lst3[i] == lst5[j]:
                if lst3[i] in f_list:   # Я не был уверен, что делать с числами что повторяются, потому решил их отсеивать.
                    continue
                else:
                    f_list.append(lst3[i])

    return print(lst3, lst5, f_list, sep='\n')


common_elements()
