lane = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for i in range(len(lane)):
    if lane[i] == 0:
        lane.insert(-1, lane[i])
        lane.pop(i)
print(lane)


lane = list(input())
for i in range(len(lane)):
    if lane[i] == "0":
        lane.extend(lane[i])
        lane.pop(i)
print(lane)
