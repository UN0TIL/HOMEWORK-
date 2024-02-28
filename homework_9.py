from random import *

lane = []
for i in range(randrange(3, 11)):
    lane.append(randint(1, 100))
lane1 = []
lane1.append(lane[0])
lane1.extend([lane[2], lane[-2]])
print(lane1)