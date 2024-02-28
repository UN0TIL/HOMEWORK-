lane = list(input())
lane1 = []
if len(lane) != 0:
    lane1.append(lane[-1])
    lane1.extend(lane[:-1])
print(lane1)
