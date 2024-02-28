lane = [1, 45, 55, 2, 78, 6, 3, 4, 7, 8]
lane1 = []
lane1.append(lane[0])
lane1.extend([lane[2], lane[-2]])
print(lane1)
