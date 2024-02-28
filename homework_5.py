lane = list(input())
n = len(lane) // 2

if len(lane) % 2 != 0:
    n += 1

lane1 = [lane[:n], lane[n:]]

print(lane1)
