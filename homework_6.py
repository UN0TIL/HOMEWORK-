lane = list(input())
lane1 = []
if len(lane) != 0:
    lane1.append(lane[-1])
    for i in range(len(lane)-1):
        lane1.append(lane[i])
print(lane1)
