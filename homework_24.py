def prime_generator(end):
    for i in range(end + 1):
        flag = True
        if i < 2:
            continue
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag = False
        if flag:
            yield i


from inspect import isgenerator


gen = prime_generator(1)
assert isgenerator(gen) == True, "Test0"
assert list(prime_generator(10)) == [2, 3, 5, 7], "Test1"
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], "Test2"
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test3"
print("OK")
