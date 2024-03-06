number = int(input())
while number > 9:
    x = 1
    for i in str(number):
        x *= int(i)
    number = x
print(number)