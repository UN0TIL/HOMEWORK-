def find_unique_value(some_list):
    numbers = {}


    for num in some_list:
        if num in numbers:
            numbers[num] += 1
        else:
            numbers[num] = 1

    for num, count in numbers.items():
        if count == 1:
            return num


lst = [1, 2, 3, 2, 1, 4, 3]

print(find_unique_value(lst))

assert find_unique_value([1, 2, 1, 1]) == 2, "Test1"
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, "Test2"
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, "Test3"
print("ОК")
