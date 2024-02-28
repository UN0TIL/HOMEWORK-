lane = list(input())
x = 0
if len(lane) > 0:
    for i in range(len(lane)):
        if i % 2 == 0:
            x += int(lane[i])
    x *= int(lane[-1])
    print(x)
else:
    print(0)