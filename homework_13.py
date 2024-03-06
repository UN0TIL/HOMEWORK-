from string import ascii_letters

a, b = input(), input()
flag = True
for i in ascii_letters:
    if flag == False:
        print(i, end="")
    elif flag:
        if i == a:
            print(i, end="")
            flag = False    
    if i == b:
        break
